import time
import json
import serial

from sources.base import (
    BaseReader,
    BaseResultReaderMixin,
    BaseStreamReaderMixin
)


class SerialReader(BaseReader):

    def __init__(self, config, device_id, **kwargs) -> None:
        super(SerialReader, self).__init__(config, device_id, **kwargs)

        self._port = device_id
        self._baud_rate = config.get("BAUD_RATE", None)

    @property
    def get_port(self):
        return self._port

    @property
    def get_baud_rate(self):
        return self._baud_rate

    def _write(self, command):
        with serial.Serial(self.port, self.baud_rate, timeout=1) as ser:
            ser.write(str.encode(command))

    def _read_line(self, flush_buffer=False):
        with serial.Serial(self.port, self.baud_rate, timeout=1) as ser:

            value = ser.readline()
            if flush_buffer:
                value = ser.readline()
            try:
                return value.decode("ascii")
            except:
                return None

    def _read_serial_buffer(self, buffer_size):
        with serial.Serial(self.port, self.baud_rate, timeout=1) as ser:
            return ser.read(buffer_size)

    def _flush_buffer(self):
        with serial.Serial(self.port, self.baud_rate, timeout=1) as ser:
            return ser.reset_input_buffer()

    def get_port_info(self):
        ports = serial.tools.list_ports.comports()
        return [{"id": index, "name": desc, "device_id": port} for index, (port, desc, hwid) in enumerate(sorted(ports))]

    def list_available_devices(self):
        return self.get_port_info()


class SerialStreamReader(SerialReader, BaseStreamReaderMixin):
    def _send_subscribe(self):
        self._write("connect")

    def read_device_config(self):

        try:
            config = json.loads(self._read_line(flush_buffer=True))
        except:
            self._write("disconnect")
            time.sleep(1.0)
            config = json.loads(self._read_line(flush_buffer=True))

        if self._validate_config(config):
            return config

        raise Exception("Invalid Configuration File")

    def _read_source(self):

        try:
            print("Serial: Reading source stream")
            with serial.Serial(self.port, self.baud_rate, timeout=1) as ser:

                self.streaming = True
                ser.reset_input_buffer()
                ser.read(self.source_buffer_size)

                if self.run_sml_model:
                    sml = self.get_sml_model_obj()
                else:
                    sml = None

                while self.streaming:

                    data = ser.read(self.source_buffer_size)

                    self.buffer.update_buffer(data)

                    if self.run_sml_model:
                        model_result = self.execute_run_sml_model(sml, data)
                        if model_result:
                            self.rbuffer.update_buffer([model_result])

                    time.sleep(0.00001)

                print("Serial: Sending disconnect command")
                ser.write(str.encode("disconnect"))

        except Exception as e:
            print(e)
            self.disconnect()
            raise e


class SerialResultReader(SerialReader, BaseResultReaderMixin):
    def set_app_config(self, config):
        config["DATA_SOURCE"] = self.name
        config["DEVICE_ID"] = self.port

    def _read_source(self):

        self._flush_buffer()

        self.streaming = True
        with serial.Serial(self.port, self.baud_rate, timeout=1) as ser:
            while self.streaming:

                try:
                    value = ser.readline()
                    data = [value.decode("ascii")]

                except Exception as e:
                    print(e,)
                    print("value", value)
                    continue

                if "ModelNumber" in data[0]:
                    self.rbuffer.update_buffer(data)
                elif data[0]:
                    print(data[0].rstrip())

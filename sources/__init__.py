from sources.serial import SerialResultReader, SerialStreamReader


def get_fusion_source():
    pass


def get_source(config, data_source, device_id, source_type, **kwargs):

    if source_type == "CAPTURE":
        if data_source == "SERIAL":
            return SerialStreamReader(config, device_id, **kwargs)

    if source_type == "RECOGNITION":
        if data_source == "SERIAL":
            return SerialResultReader(config, device_id, **kwargs)

    raise Exception(f"Invalid Data Source: {data_source}")

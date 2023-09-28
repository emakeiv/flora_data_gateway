import threading

from utilis.buffers import CircularBufferQueue

buffer = CircularBufferQueue(
    threading.Lock(),
    buffer_size=4
)

buffer.get_index(0)


# self.samples_per_packet = config["CONFIG_SAMPLES_PER_PACKET"] = 1

# packet_buffer_size a property of :
# self.samples_per_packet (1) * self.source_buffer_size

# self.source_buffer_size

# 2 or 4 depends on iNt of float

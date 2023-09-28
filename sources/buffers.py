import copy


class CircularBufferQueue():
    def __init__(self, lock, num_buffers: int = 256, buffer_size: int = 128):
        """
        Initialize a CircularBufferQueue instance.

        Args:
            lock (threading.Lock): A lock for thread safety.
            num_buffers (int): Number of circular buffers.
            buffer_size (int): Maximum size of each buffer.
        """
        self._lock = lock
        self._data = [self.get_empty() for _ in range(num_buffers)]
        self._index = 0
        self._maxsize = buffer_size
        self._num_buffers = num_buffers

    def get_empty(self):
        return b""

    def get_buffer_state(self):
        print(
            f'buffer max size: {self._maxsize} \n'
            f'current index: {self._index}'
        )
        for i in range(self._num_buffers):
            print(i, f"len: {len(self._data[i])}")

    def _increment_index(self):
        self._index = (self._index + 1) % self._num_buffers
        self._data[self._index] = self.get_empty()

    def get_index(self, index):
        return index % self._num_buffers

    def get_next_index(self, index):
        return (index + 1) % self._num_buffers

    def update_buffer(self, data):

        with self._lock:
            size = len(self._data[self._index]) + len(data)

            if size > self._num_buffers * self._maxsize:
                print("buffer size is too small: data is overwritten!")

            if size <= self._maxsize:
                self._data[self._index] += data

            elif size >= self._maxsize:

                # top off current index
                taken = self._maxsize - len(self._data[self._index])
                self._data[self._index] += data[:taken]
                self._increment()

                size = len(data) - taken
                while size > self._maxsize:
                    self._data[self._index] = data[-size: -
                                                   (size - self._maxsize)]
                    self._increment()
                    size -= self._maxsize
                self._data[self._index] += data[-size:]

            if self.is_buffer_full(self._index):
                self._increment()

    def is_buffer_full(self, index):
        if len(self._data[self.index]) == self._maxsize:
            return True
        return False

    def get_buffer_iterator(self, index, data_width):
        def buffer_iterator(buffer, data_width):
            for i in range(len(buffer) // (data_width * 2)):
                buffer_index = i * data_width * 2
                yield buffer[buffer_index: buffer_index + data_width * 2]
            yield None

        return buffer_iterator(copy.deepcopy(self._data[index]), data_width)

    def read_buffer(self, buffer_index):
        with self._lock:
            return copy.deepcopy(self._data[buffer_index])

    def reset_buffer(self):
        for i in range(self._num_buffers):
            self._data[i] = self.get_empty()

    def get_latest_buffer(self):
        latest_buffer = self._index - 1
        if self.is_buffer_full(latest_buffer):
            return latest_buffer


class CircularResultsBufferQueue(CircularBufferQueue):
    def get_empty(self):
        return []

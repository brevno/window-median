import bisect
import collections
from io import StringIO


class WindowMedianCalculator:

    def __init__(
            self,
            source_data: StringIO,
            window_size: int
    ):
        self.input_stream = source_data
        self.window_size = window_size

        # store 2 instances of window
        # 1. unsorted, needed to detect the oldest element in window
        self.window = collections.deque()
        # 2. sorted, to optimize median calculation
        self.sorted_window = []

    def results(self):
        for n in map(int, self.input_stream):
            if len(self.window) == self.window_size:
                # the window is moving,
                # the leftmost element falls out of window scope
                old = self.window.popleft()
                pos = bisect.bisect_left(self.sorted_window, old)
                del self.sorted_window[pos]

            # put next element into window
            self.window.append(n)
            bisect.insort(self.sorted_window, n)

            if len(self.window) == 1:
                yield -1
            elif len(self.window) % 2 == 0:
                pos = len(self.window) // 2 - 1
                avg = (self.sorted_window[pos]
                       + self.sorted_window[pos + 1]) / 2
                yield int(avg) if avg % 1 == 0 else avg
            else:
                pos = len(self.window) // 2
                yield self.sorted_window[pos]


if __name__ == '__main__':
    f = open('test_data', 'r')
    wm = WindowMedianCalculator(f, 3)
    for median in wm.results():
        print(median)

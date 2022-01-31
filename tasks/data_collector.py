import time
import datetime
import traceback
import threading
import pandas as pd


class DataCollector:

    def __init__(self, data_type: str):
        self.data_type = data_type
        self.update_time = datetime.datetime.now()

    def start(self):
        if self.data_type == 'klayswap':
            self.start_klayswap_data_collect()

    def start_klayswap_data_collect(self):
        self._update_klayswap_data()

    def _update_klayswap_data(self):
        op = KlayswapOperator()

        time_now = datetime.datetime.now()

        if time_now.minute != self.update_time.minute:
            op.save_current_pool_data()
            self.update_time = time_now
            print(time_now)

        timer = threading.Timer(1, self._update_klayswap_data)
        timer.setDaemon(False)
        timer.start()


if __name__ == '__main__':
    dc = DataCollector('bybit')
    dc.start()

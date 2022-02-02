import sys
from tasks.data_collector import DataCollector

if __name__ == '__main__':
    data_type = sys.argv[1]

    dc = DataCollector(data_type)
    dc.start()
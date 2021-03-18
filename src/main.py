import csv
from loader import load_data as load
from loader import load_win_rate
from generalModel import Model
import psutil
import time
config = {
    'dataset':"../../data/filtered-dataset.csv",
    'win_rate_file': '../../data/win_rate.txt',
    'loading': {
        'by_combination': False,
    }
}

def main():
    data = load(config["dataset"], config['loading']['by_combination'])
    win_rate = load_win_rate(config["win_rate_file"])
    model = Model(data, win_rate, 5)
    print("Predicting.....")
    start_time = time.time()
    res = model.predict(['121', '24', '18'], ['11', '26'])
    finish_time = time.time()
    peak_memory_usage = psutil.Process().memory_info().peak_wset / 1000000
    print("Result for blue team:")
    print(res[0])
    print("Result for red team:")
    print(res[1])
    print('Took', finish_time - start_time, 'seconds and had peak memory usage of', peak_memory_usage, 'megabytes')
main()
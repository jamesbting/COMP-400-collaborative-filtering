import csv
from loader import load_data as load
from loader import load_win_rate
from generalModel import Model
import psutil
import time
config = {
    'dataset':"../data/filtered-dataset.csv",
    'win_rate_file': '../data/win_rate.txt',
    'num_recs': 5
}

def main():
    data = load(config["dataset"])
    win_rate = load_win_rate(config["win_rate_file"])
    model = Model(data, win_rate, config['num_recs'])
    blue_team = ['121', '24', '18']
    red_team = ['11', '26']

    make_prediction(model, blue_team, red_team, model.predict)

def make_prediction(model, blue_team, red_team, prediction_function):
    print("Predicting.....")
    start_time = time.time()
    blue, red = prediction_function(blue_team, red_team)
    finish_time = time.time()
    peak_memory_usage = psutil.Process().memory_info().peak_wset / 1000000
    print("Result for blue team:")
    print(blue)
    print("Result for red team:")
    print(red)
    print('Took', finish_time - start_time, 'seconds and had peak memory usage of', peak_memory_usage, 'megabytes')
main()
import csv
from loader import load_data as load
from loader import load_win_rate
from generalModel import Model
import psutil
import time
from datetime import date

config = { 
    'dataset':"../data/filtered-dataset.csv",
    'win_rate_file': '../data/win_rate.txt',
    'num_recs': 5,
    'num_requests': 1,
    'save_results': True,
    'results_location': 'results'
}

def main():
    run_experiment(config["num_requests"])

def run_experiment(num_requests):
    data = load(config["dataset"])

    win_rate = load_win_rate(config["win_rate_file"])
    model = Model(data, win_rate, config['num_recs'])
    blue_team = ['121', '24', '18']
    red_team = ['11', '26']
    
    results = []
    for i in range(num_requests):
        print(f'iter: {i}')
        results.append(make_prediction(model, blue_team, red_team, model.predict))

    if config['save_results']:
        save_results(results, config['results_location'])

def make_prediction(model, blue_team, red_team, prediction_function):
    start_time = time.time()
    blue, red = prediction_function(blue_team, red_team)
    finish_time = time.time()
    peak_memory_usage = psutil.Process().memory_info().rss / 1000000
    print('Blue recommendations:')
    print(blue)
    print('Red recommendations:')
    print(red)
    return [finish_time - start_time, peak_memory_usage]

def save_results(results, location):
    today = date.today().strftime('%d-%m-%Y')
    curr_time = time.time()
    average_time = 0
    with open(f'{location}/results-{today}-{curr_time}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in results:
            writer.writerow(row)
            average_time += row[0]
    f.close()
    average_time /= len(results)
    print(f'Average time: {average_time}')
main()
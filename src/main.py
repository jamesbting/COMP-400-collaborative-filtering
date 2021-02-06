import csv
from cleaner import clean_data as clean
from loader import load_data as load
config = {
    'filter' : {
        'enabled': False,
        'desired_columns':  [
            'teams.0.win',
            'participants.0.championId',
            'participants.1.championId',
            'participants.2.championId',
            'participants.3.championId',
            'participants.4.championId',
            'participants.5.championId',
            'participants.6.championId',
            'participants.7.championId',
            'participants.8.championId',
            'participants.9.championId',],
        'file_name': "../../data/post-cleaning-dataset.csv",
        'output_file_name':"data/filtered-dataset.csv"
        }
        
}

def main():
    if(config["clean"]["enabled"]):
        clean(config['filter']["file_name"], config['filter']["output_file_name"],config['filter']["desired_columns"])
    data = load(config['filter']["output_file_name"])
main()
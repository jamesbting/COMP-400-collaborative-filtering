import csv

def load_data(file_name, by_combination = False):
    print("Loading data into the program")
    dataset = {}
    with open(file_name,'r') as f:
        reader = csv.reader(f, delimiter = ',')
        next(reader)
        i = 0
        for row in reader:
            if by_combination: 
                add_data_by_combination(dataset, row)  
            else:
                add_data(dataset, row)
            i += 1
        print(i, 'data points loaded')
    f.close()   
    print("Done loading data.")
    if by_combination: 
        with open('data/team_dict_by_combination.txt', 'w') as f:
            f.write(str(dataset))
        f.close()
    else:
        with open('data/team_dict.txt', 'w') as f:
            f.write(str(dataset))
        f.close()
    return dataset

def add_data_by_combination(dataset, row):
    if(len(row) != 11): 
        raise ValueError
    blue_team = tuple(row[0:5])
    red_team = tuple(row[5:10])
    blue_team_victory = True if int(row[10]) == 1 else False
    #check if blue team is already in the dictionary
    if blue_team in dataset:
        if red_team in dataset[blue_team]:
            if blue_team_victory:
                dataset[blue_team][red_team][0] += 1
            dataset[blue_team][red_team][1] += 1
        else:
            dataset[blue_team][red_team] = [1 if blue_team_victory else 0, 1]
    else:
        dataset[blue_team] = {}
        dataset[blue_team][red_team] = [1 if blue_team_victory else 0, 1]

def add_data(dataset, row):
    if(len(row) != 11): 
        raise ValueError
    blue_team = tuple(row[0:5])
    red_team = tuple(row[5:10])
    blue_team_victory = True if int(row[10]) == 1 else False
    #check if blue team is already in the dictionary
    if blue_team not in dataset:
        dataset[blue_team] = [1 if blue_team_victory else 0, 1]
        
    if red_team not in dataset:
        dataset[red_team] = [1 if blue_team_victory else 0, 1]
 
    #update blue team
    dataset[blue_team] = [dataset[blue_team][0] + 1 if blue_team_victory else dataset[blue_team][0], dataset[blue_team][1] + 1]

    #update red team
    dataset[red_team] = [dataset[red_team][0] + 1 if not blue_team_victory else dataset[red_team][0], dataset[red_team][1] + 1]

def list_to_string(row):
    res = ""
    row.sort()
    for element in row:
        res += (str(element) + ',')
    return res[0:len(res)-1]

def calculate_winrate(file_name):
    print("Calculating winrate.")
    dataset = {}
    with open(file_name,'r') as f:
        reader = csv.reader(f, delimiter = ',')
        next(reader)
        blue_wins = 0
        total_games = 0
        for row in reader:
            blue_team_victory = True if int(row[10]) == 1 else False
            if blue_team_victory:
                blue_wins += 1
            total_games += 1
    f.close()   
    print("Done calculating winrate.")
    with open('data/win_rate.txt', 'w') as f:
        f.write(str([blue_wins, total_games]))
    f.close()
    return [blue_wins, total_games]
    
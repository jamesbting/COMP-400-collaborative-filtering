import csv
def load_data(file_name, by_combination = False):
    print("Loading data into the program")
    dataset = {}
    with open(file_name,'r') as f:
        reader = csv.reader(f, delimiter = ',')
        next(reader)
        i = 0
        for row in reader:
            add_data(dataset, row)
            i += 1
        print(i, 'data points loaded')
    f.close()   
    print("Done loading data.")
   
    with open('teams/team_dict.txt', 'w') as f:
        f.write(str(dataset))
    f.close()
    return dataset

def add_data(dataset, row):
    if(len(row) != 11): 
        raise ValueError
    blue_team = tuple(row[0:5])
    red_team = tuple(row[5:10])
    blue_team_victory = True if int(row[10]) == 1 else False
    #check if blue team is already in the dictionary
    if blue_team not in dataset:
        dataset[blue_team] = [1 if blue_team_victory else 0, 1]
    else:
        #update blue team
        dataset[blue_team] = [dataset[blue_team][0] + 1 if blue_team_victory else dataset[blue_team][0], dataset[blue_team][1] + 1]
    
    if red_team not in dataset:
        dataset[red_team] = [1 if blue_team_victory else 0, 1]
    else:
        #update red team
        dataset[red_team] = [dataset[red_team][0] + 1 if not blue_team_victory else dataset[red_team][0], dataset[red_team][1] + 1]

    

def load_win_rate(win_rate_file):
    with open(win_rate_file, 'r') as f:
        content = f.readlines()
        return [int(line) for line in content]


def list_to_string(row):
    res = ""
    row.sort()
    for element in row:
        res += (str(element) + ',')
    return res[0:len(res)-1]

load_win_rate("../data/win_rate.txt")
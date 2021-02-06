import csv

def load_data(file_name):
    print("Loading data into the program")
    dataset = {}
    with open(file_name,'r') as f:
        reader = csv.reader(f, delimiter = ',')
        next(reader)
        i = 0
        for row in reader:
            add_data(dataset, row)
            i += 1
        print(i)
    f.close()   
    print("Done loading data.")
    with open('data/team_dict.txt', 'w') as f:
        f.write(str(dataset))
    f.close()
    return dataset

def add_data(dataset, row):
    if(len(row) != 11): 
        raise ValueError
    blue_team = list_to_string(row[0:5])
    red_team = list_to_string(row[5:10])
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
    
        


def list_to_string(row):
    res = ""
    for element in row:
        res += (str(element) + ',')
    return res[0:len(res)-1]
    
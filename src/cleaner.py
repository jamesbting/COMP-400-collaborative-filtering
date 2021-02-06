import csv


def clean_data(file_name, output_file_name, desired_columns):
    valid_length = 0
    output_file = open(output_file_name, "w")
    with open(file_name, "r") as input_file:
        reader = csv.reader(input_file, delimiter = ',')
        first_row = True
        selected_columns = []
        next(reader)
        for row in reader:
            #read first line from csv to obtain the indexes to obtain
            #store the length of the title line
            if first_row:
                valid_length = len(row)
                selected_columns = get_selected_columns_indexes(row, desired_columns)
                print('The selected indexes are:', selected_columns)
                first_row = False
                output_file.write(','.join(get_selected_columns(row,selected_columns)))
            #read each line and write it to a seperate file
            #verify the length of the line is correct, if incorrect then next
            elif len(row) == valid_length:
                output_file.write('\n')
                output_file.write(','.join(get_selected_columns(row,selected_columns)))
          
    output_file.close()
       
def get_selected_columns_indexes(row, desired_columns):
    selected_columns = []
    for i in range(len(row)):
        col = row[i]
        if col in desired_columns:
            selected_columns.append(i)
    return selected_columns

def get_selected_columns(row, selected_columns):
    result = []
    for i in range(len(row)):
        if i in selected_columns:
            result.append(row[i])
    if(result[0] == 'Win'):
        result.pop(0)
        result.append('1')
    elif(result[0] == 'Fail'):
        result.pop(0)
        result.append('0')
    return result

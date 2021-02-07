# League of Legends Real-Time Champion Prediction using Filtering

### Filtering the data

This program will iterate over the dataset in specified in the config object. It will load the headers from a file called 'headers.txt'. And using this header, it will determine the indexes to get the champion IDs. After getting the specified indexes, it will read those indexes from the dataset. It will filter this data into a row of 10 champion IDs and a binary value representing if the blue team won or not. The first 5 champions are the blue team and the second 5 champions are the red team. 



The program will only filter the data if the value in the config object is flagged as true.



### Loading the data

The program will load the data into memory for usage to start the model. There are 2 ways that the program will load the model:

- By team combination
- By red and blue team combinations

#### Team Combination

Loading by team combination will mean that the program will select red and blue teams, and will store the win rate regardless of the opponent's team. The reason that this is enabled, is that I found by the other method, most team compositions only occurred once. 



#### Red and Blue Team Combination

Leading by the red an team combinations means that the program will read the blue team and red team combinations and for each blue team combination, it will map to all the red team combinations that were encountered against that blue team. The red teams are then mapped to win rates.

One disadvantage of this method is that it is difficult to find repeated team combinations, and will require far more data points than 300,000 points. 
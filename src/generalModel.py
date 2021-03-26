class Model:
    def __init__(self, data, win_rate, num_of_recommendations):
        self.data = data
        self.win_rate = win_rate
        self.num_of_recommendations = num_of_recommendations

    def predict(self, blue_team, red_team):
        
        blue_team.sort()
        red_team.sort()
        
        blue_team = tuple(blue_team)
        red_team = tuple(red_team)

        blue_team_recommendations = {}
        red_team_recommendations = {}
        for team_combination in self.data.keys():
            if self.is_sub_team(team_combination, blue_team):
                blue_team_recommendations[team_combination] = self.data[team_combination][0] / self.data[team_combination][1]
            if self.is_sub_team(team_combination, red_team):
                red_team_recommendations[team_combination] = self.data[team_combination][0] / self.data[team_combination][1]
        return self.sort_dictionary(blue_team_recommendations), self.sort_dictionary(red_team_recommendations)

    def sort_dictionary(self, dict):
        list_of_items = sorted(dict.items(), reverse=True, key = lambda x: x[1])
        res = {}
        for i in range(self.num_of_recommendations):
            key, value = list_of_items[i]
            res[key] = value
        return res

    def is_sub_team(self, team, subteam):
        team_set = set(team)
        team_subset = set(subteam)
        return team_subset.issubset(team_set)

        

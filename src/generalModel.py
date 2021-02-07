class Model:
    def __init__(self, data, win_rate):
        self.data = data
        self.win_rate = win_rate

    def predict(self, blue_team, red_team):
        if len(blue_team) != 2 and len(red_team) != 2:
            raise ValueError
        if abs(len(blue_team) - len(red_team)) != 1:
            raise ValueError
        
        blue_team.sort()
        red_team.sort()
        
        blue_team = tuple(blue_team)
        red_team = tuple(red_team)

        blue_team_recommendations = {}
        red_team_recommendations = {}
        for team_combination in self.data.keys():
            if self.is_sub_team(team_combination, blue_team):
                blue_team_recommendations[team_combination] = self.data[team_combination]
            if self.is_sub_team(team_combination, red_team):
                red_team_recommendations[team_combination] = self.data[team_combination]
        return [blue_team_recommendations, red_team_recommendations]
    
    def is_sub_team(self, team, subteam):
        team_set = set((team))
        team_subset = set((subteam))
        return team_subset.issubset(team_set)

        

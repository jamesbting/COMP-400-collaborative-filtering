from math import inf
import numpy as np
class Model:
    def __init__(self, data, win_rate, num_of_recommendations):
        self.data = data
        self.win_rate = win_rate
        self.num_of_recommendations = num_of_recommendations

    def predict(self, blue_team, red_team):
        blue_team = Model.append_zeroes([int(el) for el in blue_team])
        red_team = Model.append_zeroes([int(el) for el in red_team])
        blue_team_recs = self.sort_dictionary(self.data, key = lambda x: Model.cosine(blue_team, x[0]))
        red_team_recs = self.sort_dictionary(self.data,key = lambda x: Model.cosine(red_team, x[0]))

        return blue_team_recs, red_team_recs
        # blue_team.sort()
        # red_team.sort()
        
        # blue_team = tuple(blue_team)
        # red_team = tuple(red_team)

        # blue_team_recommendations = {}
        # red_team_recommendations = {}
        # for team_combination in self.data.keys():
        #     if self.is_sub_team(team_combination, blue_team):
        #         blue_team_recommendations[team_combination] = self.data[team_combination][0] / self.data[team_combination][1]
        #     if self.is_sub_team(team_combination, red_team):
        #         red_team_recommendations[team_combination] = self.data[team_combination][0] / self.data[team_combination][1]
        # return self.sort_dictionary(blue_team_recommendations), self.sort_dictionary(red_team_recommendations)

    def sort_dictionary(self, dict, key = lambda x: x[1]):
        list_of_items = sorted(dict.items(), reverse=True, key = key)
        res = {}
        for i in range(self.num_of_recommendations):
            key, value = list_of_items[i]
            res[key] = value
        return res

    def is_sub_team(self, team, subteam):
        team_set = set(team)
        team_subset = set(subteam)
        return team_subset.issubset(team_set)
        
    @staticmethod
    def append_zeroes(x, n = 5):
        if len(x) == n:
            return x
        res = [el for el in x]
        for i in range(len(res), n):
            res.append(0)
        return res
        
    @staticmethod
    def cosine(a, b):
        a = np.array(a)
        b = np.array(b)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        return np.dot(a, b) / (norm_a * norm_b)
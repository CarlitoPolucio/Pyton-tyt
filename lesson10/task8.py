players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

a_rest = {player_num: inf for player_num, inf in players_dict.items() if inf["team"] == "A" and inf["status"] == "Rest"}
b_train = {player_num: inf for player_num, inf in players_dict.items() if inf["team"] == "B" and inf["status"] == "Training"}
c_travel = {player_num: inf for player_num, inf in players_dict.items() if inf["team"] == "C" and inf["status"] == "Travel"}
print(a_rest, "\n", b_train, "\n", c_travel)
def sport(people, need_in_team):
    if len(people) % need_in_team == 0:
        teams = len(people) / need_in_team
    else:
        return f"Need also {need_in_team - (len(people) % need_in_team)} person"
    whole_teams = []
    while teams != 0:
        teams -= 1
        new_team_lists = []
        for person in range(0, int(need_in_team)):
            new_team_lists.append(people[0])
            people.remove(people[0])
        whole_teams.append(new_team_lists)
    return whole_teams


members = [1, 3, 4, 67, 44, 67, 345, 45, 23, 10, 11, 12, 13, 14, 45]
team_size = 4

print(sport(members, team_size))






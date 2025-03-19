def sport(people, teams):
    if len(people) % teams == 0:
        people_in_team = len(people) / teams
    else:
        return f"Need also {teams - (len(people) % teams)} person"
    whole_teams = []
    while teams != 0:
        teams -= 1
        new_team_lists = []
        for person in range(0, int(people_in_team)):
            new_team_lists.append(people[0])
            people.remove(people[0])
        whole_teams.append(new_team_lists)
    return whole_teams


members = [1, 3, 4, 67, 44, 67, 345, 45, 23, 10]
need_teams = 7

print(sport(members, need_teams))






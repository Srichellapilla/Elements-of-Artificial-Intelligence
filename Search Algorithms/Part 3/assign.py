#!/usr/local/bin/python3
# assign.py : Assign people to teams
#
# Code by: Sri Varsha Chellapilla (srchell),  Roopank Kohli (rookohli) and Akash Bhapkar (abhapkar)
#
# Based on skeleton code by D. Crandall and B551 Staff, September 2021
#
import itertools
import sys
import random


#read input file into dictionary
def read_data(input_file):
    data = []
    users_list = []
    with open(input_file, "r") as f:
        for line in f.read().split("\n"):
            if line != '':
                line = line.split(" ")
                username = line[0]
                preferredList, nonPreferredList = [], []
                preferredList = line[1].split("-") if "-" in line[1] else [line[1]]
                teamSize = len(preferredList)
                if line[2] != "_":
                    nonPreferredList = line[2].split(",") if "," in line[2] else [line[2]]

                user_data = {
                    'userID': username,
                    'teamSize': teamSize,
                    'preferred': preferredList,
                    'nonPreferred': nonPreferredList
                }
                data.append(user_data)
                users_list.append(username)
    return users_list, data

#Calculate cost for all teams
def calculate_cost(teams, data):
    cost = 0

    #5 minutes for each team
    num_of_teams = len(teams)
    cost += num_of_teams * 5

    # teams pref time
    for team in teams:
        for user in team:
            user_record = [item for item in data if item['userID'] == user]

            #print(user_record)
            team_size = len(team)
            #different team size
            if user_record[0]['teamSize'] != team_size:
                cost += 2

            #didnt get preferred
            for pref in user_record[0]['preferred']:
                if pref not in ['xxx','zzz']:
                    if pref not in team:
                        cost += 3
                    else:
                        continue

            #got non preferred
            for nonpref in user_record[0]['nonPreferred']:
                if nonpref in team:
                    cost += 10
                else:
                    continue

    return cost

# old function
# def create_groups(users_list, data):
#     visited = []
#     while True:
#         unassigned_users = users_list.copy()
#         team, assigned_users = [], []
#         random_list = list(range(0, len(users_list)))
#         k = 0
#         random.shuffle(random_list)
#         for j in random_list:
#             if users_list[j] in unassigned_users:
#                 if not team:
#                     team.append([users_list[j]])
#                     unassigned_users.remove(users_list[j])
#                 else:
#                     if len(team[k]) < 3:
#                         team[k].append(users_list[j])
#                         unassigned_users.remove(users_list[j])
#                     else:
#                         k += 1
#                         team.append([users_list[j]])
#                         unassigned_users.remove(users_list[j])
#         if team not in visited:
#             visited.append(team)
#             yield team

    # print(f_groups)

def create_groups(users_list, data):
    visited = []
    while True:
        unassigned_users = users_list.copy()
        team, assigned_users = [], []
        k = 0
        random.shuffle(users_list)
        while unassigned_users:
            for user in users_list:
                if user not in assigned_users:
                    if not team:
                        team.append([user])
                        unassigned_users.remove(user)
                        assigned_users.append(user)
                    else:
                        if len(team[k]) < 3:
                            if check_for_nonpreferrence(data, team[k], user):
                                team[k].append(user)
                                unassigned_users.remove(user)
                                assigned_users.append(user)
                            elif check_for_pref(data, team[k], user):
                                team[k].append(user)
                                unassigned_users.remove(user)
                                assigned_users.append(user)
                            else:
                                k += 1
                                team.append([user])
                                unassigned_users.remove(user)
                                assigned_users.append(user)
                        else:
                            k += 1
                            team.append([user])
                            unassigned_users.remove(user)
                            assigned_users.append(user)
        if team not in visited:
            visited.append(team)
            yield team

    # print(f_groups)
#check if user is in non preferrence list in users in team and vice versa
def check_for_nonpreferrence(data, team, user):
    user_rec = [item for item in data if item['userID'] == user]
    for team_user in team:
        team_user_rec = [item for item in data if item['userID'] == team_user]
        if user in team_user_rec[0]['nonPreferred']:
            return False
        elif team_user in user_rec[0]['nonPreferred']:
            return False
    return True

def check_for_pref(data, team, user):
    user_rec = [item for item in data if item['userID'] == user]
    for team_user in team:
        team_user_rec = [item for item in data if item['userID'] == team_user]
        if user in team_user_rec[0]['preferred']:
            return True
        elif team_user in user_rec[0]['preferred']:
            return True
    return False

#return groups in printable format i.e for [djcran, sahmaini, fanjun] will return 'djcran-sahmaini-fanjun'
def create_group_format(group):
    sol = []
    for team in group:
        str_team = ''
        for i in range(len(team)):
            if i == 0:
                str_team = team[i]
            else:
                str_team = str_team + '-' + team[i]
        sol.append(str_team)
    return sol

def solver(input_file):
    """
    1. This function should take the name of a .txt input file in the format indicated in the assignment.
    2. It should return a dictionary with the following keys:
        - "assigned-groups" : a list of groups assigned by the program, each consisting of usernames separated by hyphens
        - "total-cost" : total cost (time spent by instructors in minutes) in the group assignment
    3. Do not add any extra parameters to the solver() function, or it will break our grading and testing code.
    4. Please do not use any global variables, as it may cause the testing code to fail.
    5. To handle the fact that some problems may take longer than others, and you don't know ahead of time how
       much time it will take to find the best solution, you can compute a series of solutions and then
       call "yield" to return that preliminary solution. Your program can continue yielding multiple times;
       our test program will take the last answer you 'yielded' once time expired.
    """
    users_list, data = read_data(input_file)
    #print(users_list)
    #print(data)
    group = []
    group_size = len(users_list)//3 if len(users_list)%3 == 0 else len(users_list)//3 + 1
    #start_time = time.time()
    assigned_users, visited_group = [], []
    for i in range(group_size):
        team = []
        if len(assigned_users) == len(users_list):
            break
        for user in users_list:
            if user not in assigned_users and len(team) < 3:
                team.append(user)
                assigned_users.append(user)
        group.append(team)
    visited_group.append(group)
    initial_cost = calculate_cost(group, data)

    # Simple example. First we yield a quick solution
    yield ({"assigned-groups": create_group_format(group),
            "total-cost": initial_cost})

    # Then we think a while and return another solution:
    assigned_users = []

    new_cost = 0
    group1 = []
    for i in range(group_size):
        team = []
        if len(assigned_users) == len(users_list):
            break
        for user in users_list:
            if user not in assigned_users and len(team) < 3:
                if check_for_nonpreferrence(data, team, user): #checking non preferece
                    team.append(user)
                    assigned_users.append(user)
        group1.append(team)
    visited_group.append(group1)

    new_cost = calculate_cost(group1, data)

    if new_cost < initial_cost:
        group = group1.copy()
        initial_cost = new_cost
        yield ({"assigned-groups": create_group_format(group),
                "total-cost": initial_cost})


    # This solution will never befound, but that's ok; program will be killed eventually by the
    for t in create_groups(users_list, data):
        new_cost = calculate_cost(t, data)
        if new_cost < initial_cost:
            initial_cost = new_cost
            group = t.copy()
            yield ({"assigned-groups": create_group_format(group),
                    "total-cost": initial_cost})


if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected an input filename"))

    for result in solver(sys.argv[1]):
        print("----- Latest solution:\n" + "\n".join(result["assigned-groups"]))
        print("\nAssignment cost: %d \n" % result["total-cost"])

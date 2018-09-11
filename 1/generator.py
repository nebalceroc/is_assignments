import random
from test import *
import os


solved_problem = MasterballProblem(( (0, 1, 2, 3, 4, 5, 6, 7),
                              (0, 1, 2, 3, 4, 5, 6, 7),
                              (0, 1, 2, 3, 4, 5, 6, 7),
                              (0, 1, 2, 3, 4, 5, 6, 7)))

action_limit = 10
required_states = 5

generated_states = []
for s in range(required_states):
    r_i = random.randint(0,len(actions))
    i_state = solved_problem.getSuccessors(solved_problem.getStartState())[r_i-1]
    for i in range(action_limit):
        r_i = random.randint(0,len(actions))
        i_state = solved_problem.getSuccessors(list(i_state)[0])[r_i-1]

    generated_states.append(i_state)

# for s in generated_states:
#     for a in s[0]:
#         print(a)
#
#     print("DDDDDDDDDDDDDDDDDDDDDDD")

file = open("states.txt","w")

for s in generated_states:
    # for a in s[0]:
    #file.write(str(s[0])+"\n")
    problem = MasterballProblem(s[0])
    a, t = aStarSearch(problem, myHeuristic)
    print(str(len(a)) + " " + str(a) + " " + str(problem.getStartState()))

    #file.write("\n")

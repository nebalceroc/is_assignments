import random
from test import *
import os
import time

solved_problem = MasterballProblem(( (0, 1, 2, 3, 4, 5, 6, 7),
                              (0, 1, 2, 3, 4, 5, 6, 7),
                              (0, 1, 2, 3, 4, 5, 6, 7),
                              (0, 1, 2, 3, 4, 5, 6, 7)))

action_limit = 1
required_states = 5

generated_states = []
for l in range(5):
    for s in range(required_states):
        r_i = random.randint(0,len(actions))
        i_state = solved_problem.getSuccessors(solved_problem.getStartState())[r_i-1]
        for i in range(l-1):
            r_i = random.randint(0,len(actions))
            i_state = solved_problem.getSuccessors(list(i_state)[0])[r_i-1]

        generated_states.append(i_state)
        print(i_state)

# for s in generated_states:
#     for a in s[0]:
#         print(a)
#
#     print("DDDDDDDDDDDDDDDDDDDDDDD")

file = open("states.txt","w")

# for s in generated_states:
#     # for a in s[0]:
#     #file.write(str(s[0])+"\n")
#     problem = MasterballProblem(s[0])
#     #a, t = aStarSearch(problem, myHeuristic)
#     b, u = iterativeDeepeningSearch(problem)
#     #print(str(len(a)) + " " + str(a) + " " + str(problem.getStartState()))
#     print(str(len(b)) + " " + str(u) + " " + str(problem.getStartState()))

    #file.write("\n")

#problem = MasterballProblem(((5, 1, 2, 3, 4, 0, 7, 6), (4, 1, 2, 3, 4, 7, 6, 5), (5, 0, 1, 2, 3, 0, 7, 6), (5, 1, 2, 3, 4, 0, 7, 6)))
for s in generated_states:
    print("SOLVING")
    print(s[0])
    problem = MasterballProblem(s[0])
    a_time = time.time()
    a, t, na = aStarSearch(problem, myHeuristic)
    a_time =  time.time() - a_time

    a2_time = time.time()
    a2, t2, na2 = aStarSearch(problem, myHeuristic2)
    a2_time =  time.time() - a2_time

    d_time = time.time()
    b, u, nb = iterativeDeepeningSearch(problem)
    d_time =  time.time() - d_time
    print(str(a) + " " + str(a_time) + " " + str(problem.getStartState()))
    print(na)
    print(str(a2) + " " + str(a2_time) + " " + str(problem.getStartState()))
    print(na2)
    print(str(b) + " " + str(d_time) + " " + str(problem.getStartState()))
    print(nb)

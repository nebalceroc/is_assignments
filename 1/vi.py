from test import *

actions = ['Vertical 6', 'Vertical 2', 'Right 3', 'Vertical 3',
'Vertical 6', 'Right 1', 'Right 1', 'Vertical 6',
'Vertical 3', 'Right 1', 'Right 1', 'Vertical 3',
'Right 1', 'Right 1', 'Right 1', 'Right 1',
'Right 1', 'Right 1', 'Right 1']
problem = MasterballProblem(((0, 1, 2, 3, 4, 5, 6, 7),
  (0, 1, 2, 3, 4, 5, 6, 7),
  (7, 0, 1, 2, 3, 4, 5, 6),
  (0, 1, 2, 3, 4, 5, 6, 7)
))

# print(actions)
#
# i_state = problem.getStartState()
# for s in i_state:
#     print(s)
# print('#############')
# for action in reversed(actions):
#     i_state = problem.execute_action(action, i_state)
#     print(action)
#     for s in i_state:
#         print(s)
#     print('\n')

for s in problem.getStartState():
    print(s)
print('\n')
i_state = problem.execute_action('Vertical 1', problem.getStartState())
for s in i_state:
    print(s)
print('\n')

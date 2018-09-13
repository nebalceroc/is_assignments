from graphviz import Graph, Digraph
from IPython.display import display
import search
import util
import os
import itertools
'''
This variables MUST not be changed.
They represent the movements of the masterball.
'''
R_0 = "Right 0"
R_1 = "Right 1"
R_2 = "Right 2"
R_3 = "Right 3"

V_0 = "Vertical 0"
V_1 = "Vertical 1"
V_2 = "Vertical 2"
V_3 = "Vertical 3"
V_4 = "Vertical 4"
V_5 = "Vertical 5"
V_6 = "Vertical 6"
V_7 = "Vertical 7"

actions = [R_0,R_1,R_2,R_3,V_0,V_1,V_2,V_3,V_4,V_5,V_6,V_7]

def getInv(pos):
    if pos == 0:
        return 3
    elif pos == 1:
        return 2
    elif pos == 2:
        return 1
    elif pos == 3:
        return 0

class MasterballProblem(search.SearchProblem):

    def __init__(self, startState):
        '''
        Store the initial state in the problem representation and any useful
        data.
        Here are some examples of initial states:
        [[0, 1, 4, 5, 6, 2, 3, 7], [0, 1, 3, 4, 5, 6, 3, 7], [1, 2, 4, 5, 6, 2, 7, 0], [0, 1, 4, 5, 6, 2, 3, 7]]
        [[0, 7, 4, 5, 1, 6, 2, 3], [0, 7, 4, 5, 0, 5, 2, 3], [7, 6, 3, 4, 1, 6, 1, 2], [0, 7, 4, 5, 1, 6, 2, 3]]
        [[0, 1, 6, 4, 5, 2, 3, 7], [0, 2, 6, 5, 1, 3, 4, 7], [0, 2, 6, 5, 1, 3, 4, 7], [0, 5, 6, 4, 1, 2, 3, 7]]
        '''
        self.expanded = 0
        ### your code here ###
        self.startState = startState


    def isGoalState(self, state):
        '''
        Define when a given state is a goal state (A correctly colored masterball)
        '''
        ### your code here ###
        base_vector = []
        i_0 = None
        #for lat in state:
        for idx, lat in enumerate(state):
            i_vector = list(lat)
            if idx == 0:
                base_vector = list(lat)
                try:
                    i_0 = base_vector.index(0)
                except:
                    return False
            for i in range(1,len(i_vector)):
                if i != i_vector[(i_0+i)%8]:
                    return False
        return True

    def getStartState(self):
        '''
        Implement a method that returns the start state according to the SearchProblem
        contract.
        '''
        ### your code here ###
        return self.startState

    def getSuccessors(self, state):
        '''
        Implement a successor function: Given a state from the masterball
        return a list of the successors and their corresponding actions.

        This method *must* return a list where each element is a tuple of
        three elements with the state of the masterball in the first position,
        the action (according to the definition above) in the second position,
        and the cost of the action in the last position.

        Note that you should not modify the state.
        '''

        self.expanded += 1
        successors = []
        ### your code here ###
        s_state = []
        dummy_state = []
        for layer in state:
            s_state.append(list(layer))
            dummy_state.append(list(layer))

        for action in actions:
            s_state = []
            dummy_state = []
            for layer in state:
                s_state.append(list(layer))
                dummy_state.append(list(layer))

            action_type, orientation = action.split(" ")
            orientation = int(orientation)
            if action_type == "Right":
                dummy_state[orientation] = [s_state[orientation][-1]] + s_state[orientation][:-1]
            elif action_type == "Vertical":
                lat = 0
                while lat < len(s_state):
                    aux_arr = [s_state[lat][(orientation+3)%8],s_state[lat][(orientation+2)%8],s_state[lat][(orientation+1)%8],s_state[lat][orientation]]
                    dummy_state[getInv(lat)][orientation] = aux_arr[0]
                    dummy_state[getInv(lat)][(orientation+1)%8] = aux_arr[1]
                    dummy_state[getInv(lat)][(orientation+2)%8] = aux_arr[2]
                    dummy_state[getInv(lat)][(orientation+3)%8] = aux_arr[3]
                    lat += 1


            tupled_layers = []
            for layer in dummy_state:
                tupled_layers.append(tuple(layer))

            tupled_state = tuple(tupled_layers)

            successors.append(tuple((tupled_state,action,1)))
        return successors

    def execute_action(self,action,state):
        s_state = []
        dummy_state = []
        for layer in state:
            s_state.append(list(layer))
            dummy_state.append(list(layer))

        action_type, orientation = action.split(" ")
        orientation = int(orientation)
        if action_type == "Right":
            dummy_state[orientation] = [s_state[orientation][-1]] + s_state[orientation][:-1]
        elif action_type == "Vertical":
            lat = 0
            while lat < len(s_state):
                aux_arr = [s_state[lat][(orientation+3)%8],s_state[lat][(orientation+2)%8],s_state[lat][(orientation+1)%8],s_state[lat][orientation]]
                dummy_state[getInv(lat)][orientation] = aux_arr[0]
                dummy_state[getInv(lat)][(orientation+1)%8] = aux_arr[1]
                dummy_state[getInv(lat)][(orientation+2)%8] = aux_arr[2]
                dummy_state[getInv(lat)][(orientation+3)%8] = aux_arr[3]
                lat += 1


        tupled_layers = []
        for layer in dummy_state:
            tupled_layers.append(tuple(layer))

        tupled_state = tuple(tupled_layers)

        return tupled_state

class search_tree():
    def __init__(self):
        self.graph = Digraph(graph_attr = {'size':'9'})

    def addNode(self, name, label):
        self.graph.node(name, label)

    def addEdge(self, source, action, target):
        self.graph.edge(source, target, action)

    def getDot(self):
        return self.graph

def graphDot(g_prob, color):
    dot = Graph(graph_attr = {'size':'3.5'})
    for node in g_prob.G:
        if not node in color:
            dot.node(node)
        else:
            dot.node(node, style = 'filled', color = color[node])
    for n1 in g_prob.G:
        for n2 in g_prob.G[n1]:
            if n1 < n2:
                dot.edge(n1, n2)
    return dot

def iterativeDeepeningSearch(problem):
    for depth in itertools.count():
        visited = {}
        frontier = util.Queue()
        state = problem.getStartState()
        frontier.push((state, [], 0))
        tree = search_tree()
        tree.addNode(str(state)+"[]",str(state))
        while not frontier.isEmpty():
            u, actions, path_cost = frontier.pop()
            if problem.isGoalState(u):
                return  actions, tree
            if not u in visited:
                for v, action, cost in problem.getSuccessors(u):
                    tree.addNode(str(v) + str(actions+[action]), str(v))
                    tree.addEdge(str(u) + str(actions), str(cost), str(v) + str(actions+[action]))
                    if path_cost < depth:
                        frontier.push((v, actions + [action], path_cost + cost))
            visited[u] = 'black'
    return [], tree

def aStarSearch(problem, heuristic):
    def f_cost(item):
        return item[2] + heuristic(item[0])
    visited = {}
    frontier = util.PriorityQueueWithFunction(f_cost)
    state = problem.getStartState()
    frontier.push((state, [], 0))
    tree = search_tree()
    tree.addNode(str(state)+"[]",str(state))
    while not frontier.isEmpty():
        u, actions, path_cost = frontier.pop()
        if problem.isGoalState(u):
            return  actions, tree
        if not u in visited:
            for v, action, cost in problem.getSuccessors(u):
                tree.addNode(str(v) + str(actions+[action]), str(v))
                tree.addEdge(str(u) + str(actions), str(cost), str(v) + str(actions+[action]))
                frontier.push((v, actions + [action], path_cost + cost))
        visited[u] = 'black'
    return [], tree

def myHeuristic(state):
    ### your code here ###
    error_count = 0
    for lat in state:
        i = 0
        for ipos in lat:
            if ipos != i:
                error_count+=1
            i+=1
    return error_count

def myHeuristic2(state):
    ### your code here ###
    error_count = 0

    for idx, lat in enumerate(state):
        for x in range(8):
            try:
                i_x = base_vector.index(x)
            except:
                return False
            
            if lat.count(x) == 0 or lat.count() > 1:
                error_count=+2
            else:
                i = lat.index(x)

    base_vector = []
    i_0 = None
    #for lat in state:
    for idx, lat in enumerate(state):
        i_vector = list(lat)
        if idx == 0:
            base_vector = list(lat)
            try:
                i_0 = base_vector.index(0)
            except:
                return False
        for i in range(1,len(i_vector)):
            if i != i_vector[(i_0+i)%8]:
                return False
    return True

        return error_count

#problem = MasterballProblem((((5, 1, 4, 6, 7, 0, 3, 2), (0, 5, 3, 7, 6, 1, 2, 4), (0, 6, 7, 1, 4, 3, 5, 2), (4, 5, 3, 2, 0, 6, 7, 1))))


#print(problem.isGoalState(((1, 2, 3, 4, 5, 6, 7, 0),
                            # (1, 2, 3, 4, 5, 6, 7, 0),
                            # (0, 1, 2, 3, 4, 5, 6, 7),
                            # (0, 1, 2, 3, 4, 5, 6, 7))))

#print(myHeuristic(problem.getStartState()))
# problem = MasterballProblem(((5, 7, 2, 1, 4, 0, 6, 3),
# (1, 0, 3, 2, 5, 4, 7, 6),
# (5, 1, 2, 6, 4, 3, 0, 7),
# (1, 0, 3, 2, 5, 4, 7, 6)
# ))
#problem = MasterballProblem(( (0, 1, 2, 3, 4, 5, 6, 7),
#                              (0, 1, 2, 3, 4, 5, 6, 7),
#                              (0, 1, 2, 3, 4, 5, 6, 7),
#                              (0, 1, 2, 3, 4, 5, 6, 7)))

#print(aStarSearch(problem, myHeuristic)[0])
#for l in problem.getStartState():
#    print(l)

#print("ASDADASDASD")
#suc = problem.getSuccessors(problem.getStartState())
#for s in suc:
    #for a in s[0]:
    #    print(a)

#    print(str(s[1]))

#    print("DDDDDDDDDDDDDDDDDDDDDDD")
#print(suc)

#print(iterativeDeepeningSearch(problem))
# file = open("states.txt", "r")
# for line in file:
#     problem = MasterballProblem(tuple(line.split(",")))
#     a, t = aStarSearch(problem, myHeuristic)
#     print(str(len(a)) + " " + str(a) + " " + str(problem.getStartState()))

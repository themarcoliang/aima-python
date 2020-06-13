# from a2_q1 import rand_graph

def check_teams(graph, csp_sol):
    for key in graph:
        team = csp_sol[key]
        for person in graph[key]:
            if(csp_sol[person] == team):
                return False
    return True

# graph = rand_graph(0.2,5)
# print(graph)
# X = {0:1, 1:1, 2:1, 3:1, 4:1}
# print(check_teams(graph, X))

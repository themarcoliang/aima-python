from a2_q1 import rand_graph
from a2_q2 import check_teams
import csp
import time

# This is a class that adds a variable to track unassignments of a CSP problem
# References InstrucCSP(CSP) in csp.ipynb notebook
class unassignCSP(csp.CSP):
    def __init__(self,variables, domains, neighbors, constraints):
        super().__init__(variables,domains,neighbors,constraints)
        self.unassignments = 0
    
    def unassign(self, var, assignment):
        super().unassign(var,assignment)
        self.unassignments += 1

def edge_count(graph):
    edge = 0
    for i in graph:
        edge += sum(j > i for j in graph[i])
    return edge

def run_q3():
    graphs = [rand_graph(0.1,31), rand_graph(0.2,31), rand_graph(0.3,31),
    rand_graph(0.4, 31), rand_graph(0.5,31), rand_graph(0.6,31)]
    count = 0
    print("Solving the Erdos-Renyi Random Graphs with Backtracking and AC3 and Forward Checking Inference")
    for g in graphs:
        numPeople = 31
        elapsedTime = 0
        assigns = 0
        unassigns = 0
        teamLimit = 1
        count += 1
        while(True):
            domain = csp.UniversalDict([i for i in range(1, teamLimit+1)])
            tempCSP = csp.CSP(list(g.keys()), domain, g, csp.different_values_constraint)
            problem = unassignCSP(tempCSP.variables, tempCSP.domains, tempCSP.neighbors, tempCSP.constraints)
            csp.AC3(problem,removals=[])
            startTime = time.time()
            result = csp.backtracking_search(problem, order_domain_values=csp.lcv, select_unassigned_variable=csp.mrv, inference=csp.forward_checking)
            elapsedTime += time.time() - startTime
            assigns += problem.nassigns
            unassigns += problem.unassignments
            teamLimit += 1
            # print("Increasing teamsize to", teamLimit)
            if(result != None and check_teams(g,result)): #correct result is found
                break
        
        print("=================================================")
        print("Run", count)
        print("Probability:", count * 0.1)
        print("Number of People:", numPeople)
        print("Number of Edges:", edge_count(g))
        print("Number of Teams:", len(set(result.values())))
        print("Elapsed Time(in seconds):", elapsedTime)
        print("Total Number of Assignments:", assigns)
        print("Total Number of Unassignments", unassigns)         

# run_q3()
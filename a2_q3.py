#Assignment 2, Q3
#CMPT 310, Summer 2020
#Created by Marco Liang 301308414

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
    numPeople = 31
    graphs = [rand_graph(0.1,numPeople), rand_graph(0.2,numPeople), rand_graph(0.3,numPeople),
    rand_graph(0.4, numPeople), rand_graph(0.5,numPeople), rand_graph(0.6,numPeople)]
    results = []
    count = 0
    print("Solving the Erdos-Renyi Random Graphs with Backtracking and AC3 and Forward Checking Inference")
    for g in graphs:
        elapsedTime = 0
        assigns = 0
        unassigns = 0
        teamLimit = 1
        count += 1
        while(True):
            # domain = csp.UniversalDict([i for i in range(1, teamLimit+1)])
            domain = list(range(0,teamLimit))
            tempCSP = csp.MapColoringCSP(domain,g)
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
        
        results.append(result)
        print("=================================================")
        print("Probability:", count / 10)
        print("Number of People:", numPeople)
        print("Number of Edges:", edge_count(g))
        print("Number of Teams:", len(set(result.values())))
        print("Elapsed Time(in seconds):", elapsedTime)
        print("Total Number of Assignments:", assigns)
        print("Total Number of Unassignments:", unassigns)
        print("Optimal Number of Assignments:", problem.nassigns)
        print("Optimal Number of Unassignments:", problem.unassignments)
        
    print("Friendship Graphs:")
    for g in graphs:
        print(g)

    print("Results:")
    for r in results:
        print(r)
 
# for i in range(1,6):
#     print("Run", i)
#     run_q3()
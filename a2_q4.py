from a2_q1 import rand_graph
from a2_q2 import check_teams
from a2_q3 import edge_count
import csp
import time

def run_q4():
    graphs = [rand_graph(0.1,105), rand_graph(0.2,105), rand_graph(0.3,105),
    rand_graph(0.4, 105), rand_graph(0.5,105), rand_graph(0.6,105)]
    count = 0
    print("Approximating Solution to Erdos-Renyi Random Graphs Using Min Conflicts Algorithm (max-steps = 1000)")
    for g in graphs:
        numPeople = 105
        elapsedTime = 0
        assigns = 0
        teamLimit = 1
        count += 1
        while(True):
            domain = csp.UniversalDict([i for i in range(1, teamLimit+1)])
            problem = csp.CSP(list(g.keys()), domain, g, csp.different_values_constraint)
            # problem = unassignCSP(tempCSP.variables, tempCSP.domains, tempCSP.neighbors, tempCSP.constraints)
            csp.AC3(problem,removals=[])
            startTime = time.time()
            result = csp.min_conflicts(problem, max_steps=1000)
            elapsedTime += time.time() - startTime
            assigns += problem.nassigns
            teamLimit += 1
            print("Increasing teamsize to", teamLimit)
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

for i in range(1,6):
    print("========NEW RUN========")
    print("\n\n\n")
    run_q4()
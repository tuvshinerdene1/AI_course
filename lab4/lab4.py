from collections import deque
import heapq

class UndirectedGraph:
    def __init__(self, graph_dict):
        self.graph_dict = graph_dict
        for node in list(self.graph_dict.keys()):
            for neighbor, distance in self.graph_dict[node].items():
                if neighbor not in self.graph_dict:
                    self.graph_dict[neighbor] = {}
                self.graph_dict[neighbor][node] = distance
    def get(self,node):
        return self.graph_dict.get(node, {})
    
class Node:
    def __init__(self, state, parent=None, path_cost = 0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
    
    def __lt__(self, other):
        return False
    
    def path(self):
        node = self
        path_back = []
        while node:
            path_back.append(node.state)
            node = node.parent
        return list(reversed(path_back))

data = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))

euclidian_distance = dict(
    Arad=366,
    Bucharest=0,
    Craiova = 160,
    Drobeta = 242,
    Eforie = 161,
    Fagaras = 176,
    Giurgiu = 77,
    Hirsova = 151,
    Iasi = 226,
    Lugoj = 244,
    Mehadia = 241,
    Neamt = 234,
    Oradea = 380,
    Pitesti = 100,
    Rimnicu = 193,
    Sibiu = 253, 
    Timisoara = 329,
    Urziceni = 80,
    Vaslui= 199,
    Zerind = 374
)

def heuristic(node):
    return euclidian_distance[node]

def greedySearch(graph, start, goal):
    frontier = []
    start_node = Node(start)
    heapq.heappush(frontier, ((heuristic(start),start_node)))
    visited = {start}

    while frontier:
        _, current_node = heapq.heappop(frontier)
        if current_node.state == goal:
            return current_node.path(), current_node.path_cost
        
        for neighbor, weight in graph.get(current_node.state).items():
            if neighbor not in visited:
                visited.add(neighbor)
                new_node = Node(neighbor, parent=current_node,path_cost=current_node.path_cost+weight)
                heapq.heappush(frontier, (heuristic(neighbor),new_node))
    return None,0

def aStarSearch(graph, start, goal):
    frontier = []
    start_node = Node(start)
    heapq.heappush(frontier, ((heuristic(start), start_node)))
    
    best_g_costs = {start:0}
    while frontier:
        _, current_node= heapq.heappop(frontier)

        if current_node.state == goal:
            return current_node.path(), current_node.path_cost
        
        for neighbor, weight in graph.get(current_node.state).items():
            new_g_cost = current_node.path_cost + weight
            if neighbor not in best_g_costs or new_g_cost < best_g_costs[neighbor]:
                best_g_costs[neighbor] = new_g_cost
                new_node = Node(neighbor, parent=current_node, path_cost=new_g_cost)
                f_cost = new_g_cost + heuristic(neighbor)
                heapq.heappush(frontier, (f_cost, new_node))
    return None, 0

path, total_cost = greedySearch(data, 'Arad', 'Bucharest')
print("Greedy search")
if path:
    print(f"Path found: {' -> '.join(path)}")
    print(f"Total distance: {total_cost}")
else:
    print("No path found.")

path, total_cost = aStarSearch(data, 'Arad', 'Bucharest')
print("A* search")
if path:
    print(f"Path found: {' -> '.join(path)}")
    print(f"Total distance: {total_cost}")
else:
    print("No path found.")

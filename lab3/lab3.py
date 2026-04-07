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
    
    def get(self, node):
        return self.graph_dict.get(node, {})
    
class Node:
    def __init__(self, state, parent=None, path_cost = 0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
    
    def __lt__(self, other):
        return self.path_cost < other.path_cost
    
    def path(self):
        node = self
        path_back = []
        while node:
            path_back.append(node.state)
            node = node.parent
        return list(reversed(path_back))
    
def depth_first_search(graph, start , goal):
    stack = [Node(start)]
    visited = {start}

    while stack:
        current_node = stack.pop()

        if current_node.state == goal:
            return [current_node.path(), current_node.path_cost]
        
        neighbors = graph.get(current_node.state)
        for neighbor, distance in neighbors.items():
            if neighbor not in visited:
                visited.add(neighbor)
                new_cost = current_node.path_cost + distance
                stack.append(Node(neighbor, current_node, new_cost))

    return None
def breadth_first_search(graph, start, goal):
    queue = deque([Node(start)])
    visited = {start}

    while queue:
        current_node = queue.popleft()

        if current_node.state == goal:
            return [current_node.path(), current_node.path_cost]
        neighbors = graph.get(current_node.state)
        for neighbor, distance in neighbors.items():
            if neighbor not in visited:
                visited.add(neighbor)
                new_cost = current_node.path_cost + distance
                queue.append(Node(neighbor, current_node, new_cost))
    return None

def uniform_cost_search(graph, start, goal):
    frontier = [Node(start, None, 0)]
    heapq.heapify(frontier)

    explored = set()

    while frontier:
        current_node = heapq.heappop(frontier)

        if current_node.state == goal:
            return [current_node.path(), current_node.path_cost] 
        
        if current_node.state not in explored:
            explored.add(current_node.state)
            neighbors = graph.get(current_node.state)
            for neighbor, distance in neighbors.items():
                new_cost = current_node.path_cost + distance
                new_node = Node(neighbor, current_node, new_cost)

                if neighbor not in explored:
                    heapq.heappush(frontier, new_node)
    return None

# def total_distance()
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

print("DFS : ")  
result_path = depth_first_search(data, 'Arad', 'Bucharest')
print(f"Path found: {result_path[0]}, total distance : {result_path[1]}")

print("BFS : ")  
result_path = breadth_first_search(data, 'Arad', 'Bucharest')
print(f"Path found: {result_path[0]}, total distance : {result_path[1]}")

print("UCS : ")
result_path = uniform_cost_search(data, 'Arad', 'Bucharest')
print(f"Path found: {result_path[0]}, total distance : {result_path[1]}")

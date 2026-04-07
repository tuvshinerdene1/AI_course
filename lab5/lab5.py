import ast
import random
import math

with open('Mongolian_map.txt', 'r', encoding='utf-8') as f:
    file_content = f.read()
    graph_data = ast.literal_eval(file_content)

distances = {node:{} for node in graph_data['nodes']}

for u,v, attributes in graph_data['edges']:
    weight = attributes['weight']
    distances[u][v] = weight
    distances[v][u] = weight

START_CITY = 'Ulaanbaatar'
other_cities = [c for c in graph_data['nodes'] if c!= START_CITY]

def calculate_total_distance(tour):
    total = 0
    for i in range(len(tour)):
        city_a = tour[i]
        city_b = tour[(i+1)%len(tour)]
        total += distances[city_a][city_b]
    return total


def get_best_neighbor(current_tour):
    current_dist = calculate_total_distance(current_tour)
    n = len(current_tour)
    for i in range(1,n):
        for j in range(i+1, n):
            neighbor = current_tour[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

            neighbor_dist = calculate_total_distance(neighbor)

            if neighbor_dist < current_dist:
                return neighbor, neighbor_dist
    return None, None


def hill_climbing():
    random.shuffle(other_cities)
    current_tour = [START_CITY] + other_cities
    current_dist = calculate_total_distance(current_tour)

    print(f"starting at {START_CITY}")
    print(f"initial random distance: {current_dist}")

    steps = 0

    while True:
        next_tour, next_dist = get_best_neighbor(current_tour)
        if next_tour is not None:
            current_tour = next_tour
            current_dist = next_dist
            steps += 1
            print(f"step {steps}: found shorter path ({current_dist})")
        else:
            break
    return current_tour, current_dist

def simulated_annealing(temp = 1000.0, cooling_rate = 0.99, min_temp = 0.1):

    random.shuffle(other_cities)
    current_tour = [START_CITY] + other_cities
    current_dist = calculate_total_distance(current_tour)

    best_tour = current_tour[:]
    best_dist = current_dist

    while temp > min_temp:
        i, j = random.sample(range(1, len(current_tour)), 2)

        neighbor = current_tour[:]
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

        neighbor_dist = calculate_total_distance(neighbor)

        diff = neighbor_dist - current_dist

        if diff < 0:
            current_tour = neighbor
            current_dist = neighbor_dist

        else:
            probability = math.exp(-diff/temp)
            if random.random() < probability:
                current_tour = neighbor
                current_dist = neighbor_dist

        if current_dist < best_dist:
            best_dist = current_dist
            best_tour = current_tour[:]

        temp *= cooling_rate
    return best_tour, best_dist


def hill_climbing_test(restarts = 10):
    best_overall_dist = float('inf')
    best_overall_route = []

    print(f"running hill climbing {restarts} times")

    for i in range(restarts):
        route, dist = hill_climbing()
        if dist < best_overall_dist:
            best_overall_dist = dist
            best_overall_route = route

    print("FINAL RESULTS")
    print(f"best distance: {best_overall_dist}")
    print(" -> ".join(best_overall_route) + f" -> {START_CITY}")

def simulated_annealing_test(restarts = 10):
    best_overall_dist = float('inf')
    best_overall_route = []
    print(f"running simulated annealling {restarts} times")
    for i in range(restarts):
        sa_route, sa_dist = simulated_annealing(1000, 0.9, 0.1)
        print(f"{i+1}th time : {sa_dist}")
        if sa_dist < best_overall_dist:
            best_overall_dist = sa_dist
            best_overall_route = sa_route
    
    print(f"Final SA Distance: {best_overall_dist}")
    print(" -> ".join(best_overall_route) + f" -> {START_CITY}")



# hill_climbing_test(10)
simulated_annealing_test(1000)

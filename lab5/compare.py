import ast
import random
import math
import matplotlib.pyplot as plt

with open('Mongolian_map.txt', 'r', encoding='utf-8') as f:
    file_content = f.read()
    graph_data = ast.literal_eval(file_content)

distances = {node: {} for node in graph_data['nodes']}
for u, v, attributes in graph_data['edges']:
    weight = attributes['weight']
    distances[u][v] = weight
    distances[v][u] = weight

START_CITY = 'Ulaanbaatar'
other_cities = [c for c in graph_data['nodes'] if c != START_CITY]


def calculate_total_distance(tour):
    total = 0
    for i in range(len(tour)):
        city_a = tour[i]
        city_b = tour[(i + 1) % len(tour)]
        total += distances[city_a][city_b]
    return total

def get_best_neighbor(current_tour):
    current_dist = calculate_total_distance(current_tour)
    n = len(current_tour)
    for i in range(1, n):
        for j in range(i + 1, n):
            neighbor = current_tour[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbor_dist = calculate_total_distance(neighbor)
            if neighbor_dist < current_dist:
                return neighbor, neighbor_dist
    return None, None

def hill_climbing():
    random.shuffle(other_cities)
    current_tour = [START_CITY] + other_cities
    while True:
        next_tour, _ = get_best_neighbor(current_tour)
        if next_tour:
            current_tour = next_tour
        else:
            break
    return calculate_total_distance(current_tour)

def simulated_annealing():
    temp = 1000.0
    cooling_rate = 0.995
    min_temp = 0.1
    random.shuffle(other_cities)
    current_tour = [START_CITY] + other_cities
    current_dist = calculate_total_distance(current_tour)
    best_dist = current_dist

    while temp > min_temp:
        i, j = random.sample(range(1, len(current_tour)), 2)
        neighbor = current_tour[:]
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        neighbor_dist = calculate_total_distance(neighbor)
        diff = neighbor_dist - current_dist

        if diff < 0 or random.random() < math.exp(-diff / temp):
            current_tour = neighbor
            current_dist = neighbor_dist
        
        if current_dist < best_dist:
            best_dist = current_dist
        temp *= cooling_rate
    return best_dist


def run_comparison(iterations=50):
    hc_results = []
    sa_results = []

    print(f"Running {iterations} trials for each algorithm...")

    for i in range(iterations):
       
        hc_results.append(hill_climbing())
        sa_results.append(simulated_annealing())
        
        if (i + 1) % 10 == 0:
            print(f"Completed {i + 1} trials...")


    
    plt.figure(figsize=(10, 6))
    
    plt.plot(hc_results, label='Hill Climbing', color='red', alpha=0.6, linestyle='--')
    plt.plot(sa_results, label='Simulated Annealing', color='blue', alpha=0.6)
    
    avg_hc = sum(hc_results) / iterations
    avg_sa = sum(sa_results) / iterations
    plt.axhline(y=avg_hc, color='red', linestyle='-', label=f'HC Average: {avg_hc:.1f}')
    plt.axhline(y=avg_sa, color='blue', linestyle='-', label=f'SA Average: {avg_sa:.1f}')

    plt.title(f"Comparison of TSP Algorithms ({iterations} Trials)")
    plt.xlabel("Trial Number")
    plt.ylabel("Total Distance (Lower is Better)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.savefig('algorithm_comparison.png')
    print("\nComparison complete! Graph saved as 'algorithm_comparison.png'")
    plt.show()

if __name__ == "__main__":
    run_comparison(1000)
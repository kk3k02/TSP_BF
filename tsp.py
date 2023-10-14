import itertools

class Tsp:
    def __init__(self, n, cost):
        self.n = n
        self.cost = cost

    def calculate_total_distance(self, path):
        total_distance = 0
        for i in range(self.n - 1):
            start_node = path[i]
            end_node = path[i + 1]
            total_distance += self.cost[start_node][end_node]
        total_distance += self.cost[path[-1]][path[0]]
        return total_distance

    def start(self):
        if self.n <= 2:
            return (list(range(self.n)), 0)

        vertices = list(range(self.n))

        min_distance = float('inf')
        best_tour = None

        for tour in itertools.permutations(vertices):
            total_distance = self.calculate_total_distance(tour)
            if total_distance < min_distance:
                min_distance = total_distance
                best_tour = tour

        best_tour = list(best_tour)  # Konwertuj na listę tylko na końcu
        best_tour = best_tour + [best_tour[0]]  # Dodaj wierzchołek startowy na koniec trasy

        return min_distance, best_tour

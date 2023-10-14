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
            return list(range(self.n)), 0

        vertices = list(range(self.n))

        min_dist = float('inf')
        best_path = None

        for path in itertools.permutations(vertices):
            total_dist = self.calculate_total_distance(path)
            if total_dist < min_dist:
                min_dist = total_dist
                best_path = path

        best_path = list(best_path)  # Konwertuj na listę tylko na końcu
        best_path = best_path + [best_path[0]]  # Dodaj wierzchołek startowy na koniec trasy

        return int(min_dist), best_path

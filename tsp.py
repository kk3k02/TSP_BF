import itertools

class Tsp:
    def __init__(self, num_ver, graph):
        self.num_ver = num_ver
        self.graph = graph

    def calculate_total_distance(self, path):
        total_distance = 0
        for i in range(len(path) - 1):
            start_node = path[i]
            end_node = path[i + 1]
            total_distance += self.graph[start_node][end_node]
        total_distance += self.graph[path[-1]][path[0]]
        return total_distance

    def brute_force_tsp(self):
        if self.num_ver <= 2:
            return (list(range(self.num_ver)), 0)

        vertex_permutations = itertools.permutations(range(self.num_ver))

        min_distance = float('inf')
        best_path = None

        for path in vertex_permutations:
            total_distance = self.calculate_total_distance(path)
            if total_distance < min_distance:
                min_distance = total_distance
                best_path = list(path)

        return best_path, min_distance

    def start(self):
        tsp_solver = Tsp(self.num_ver, self.graph)
        best_path, min_distance = tsp_solver.brute_force_tsp()
        return best_path, min_distance
import math

room_dict = {
    0: "blue room",
    1: "hall",
    2: "store",
    3: "king's chamber",
    4: "knight room",
    5: "garden",
    6: "dungeon",
    7: "kitchen"
}

directions_to_move = {
    "blue room": {"e": 1, "s": 6},
    "hall": {"ne": 2, "e": 3, "se": 4, "sw": 5, "w": 6, "nw": 0},
    "store": {"w": 1, "s": 3},
    "king's chamber": {"n": 2, "w": 1, "s": 4},
    "knight room": {"n": 3, "nw": 1, "w": 5},
    "garden": {"ne": 1, "nw": 6, "s": 7},
    "dungeon": {"n": 0, "s": 5, "e": 1},
    "kitchen": {}
}

directions = {
    'n': 'North',
    'ne': 'North East',
    'e': 'East',
    'se': 'South East',
    's': 'South',
    'sw': 'South West',
    'w': 'West',
    'nw': 'North West'
}

room_desc = {
    "blue room": "You have entered the Blue Room",
    "hall": "You have entered the Hall",
    'store': "You have entered the Store Room",
    "king's chamber": "You have entered the King's Chamber",
    "knight room": "You have entered the Knight's Room",
    "garden": "You have entered the Garden",
    "dungeon": "You have entered the Dungeon",
    "kitchen": "You have reached the end!!!!!!!"
}

class Graph():
    def min_distance(self, queue, dist):
        minimum = math.inf
        min_index = -1
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    def print_path(self, parent, j):
        if parent[j] == -1:
            print(room_dict[j])
            return
        self.print_path(parent, parent[j])
        print(room_dict[j])
    
    def print_solution(self, parent, j):
        print("The shortest path to Garder from blue room is: ")
        self.print_path(parent, 7)

    def djikstra(self, graph, src):
        row = len(graph)
        column = len(graph[0])
        dist = [math.inf] * row
        parent = [-1]*row
        dist[src] = 0
        queue = []
        for i in range(row):
            queue.append(i)
        while queue:
            u = self.min_distance(queue, dist)
            queue.remove(u)
            for i in range(column):
                if graph[u][i] and i in queue:
                    if dist[u]+graph[u][i]<dist[i]:
                        dist[i] = dist[u]+graph[u][i]
                        parent[i] = u
        self.print_solution(parent, dist)

g = Graph()
graph = [[0, 1, 0, 0, 0, 0, 5, 0],
         [1, 0, 3, 2, 1, 3, 0, 0],
         [0, 3, 0, 5, 0, 0, 0, 0],
         [0, 2, 5, 0, 1, 0, 0, 0],
         [0, 1, 0, 1, 0, 1, 0, 0],
         [0, 3, 0, 0, 1, 0, 2, 1],
         [5, 0, 0, 0, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0]   
        ]
g.djikstra(graph, 0)


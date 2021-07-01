def h(n):
    fh = {
        'Arad': 366,
        'Bucharest': 0,
        'Craiova': 160,
        'Dobreta': 242,
        'Eforie': 161,
        'Fagaras': 176,
        'Giurgiu': 77,
        'Hirsova': 151,
        'Iasi': 226,
        'Lugoj': 244,
        'Mehadia': 241,
        'Neamt': 134,
        'Oradea': 380,
        'Pitesti': 100,
        'Rimnicu Vilcea': 193,
        'Sibiu': 253,
        'Timisoara': 329,
        'Urziceni': 80,
        'Vaslui': 199,
        'Zerind': 374,

    }

    return fh[n]


class Graph:
    def __init__(self, adj):
        self.adjac_lis = adj

    def get_neighbors(self, v):
        return self.adjac_lis[v]

    # This is heuristic function which is having equal values for all nodes

    def a_star_algorithm(self, start, stop):
        # In this open_lst is a list of nodes which have been visited, but who's
        # neighbours haven't all been always inspected, It starts off with the start
        # node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = {start}
        closed_lst = set([])
        actual_node = start

        # poo has present distances from start to all other nodes
        # the default value is +infinity
        distances = {start: 0}

        # par contains an adjac mapping of all nodes
        map = {start: start}


        while len(open_lst) > 0:
            n = None

            if actual_node!=start:
                print("\nExpanding",actual_node, "")
            for v in open_lst:
                print(v," with a cost of: ",distances[v] + h(v))
                if n is None or distances[v] + h(v) < distances[n] + h(n):
                    n = v
            print("Choosen node: ", n)
            if n is None:
                print('Path does not exist!')
                return None
            actual_node=n
            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []
                while map[n] != n:
                    reconst_path.append(n)
                    n = map[n]

                reconst_path.append(start)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))

                return reconst_path

            # for all the neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    map[m] = n
                    distances[m] = distances[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if distances[m] > distances[n] + weight:
                        distances[m] = distances[n] + weight
                        map[m] = n

                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)

            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)

        print('Path does not exist!')
        return None


adjac_lis = {
    'Arad': [("Zerind", 75), ("Timisoara", 118), ("Sibiu", 140)],
    'Bucharest': [("Fagaras", 211), ("Pitesti", 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Craiova': [("Dobreta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)],
    'Dobreta': [("Mehadia", 75), ("Craiova", 120)],
    'Eforie': [("Hirsova", 86)],
    'Fagaras': [("Sibiu", 99), ("Bucharest", 211)],
    'Giurgiu': [("Giurgiu", 90)],
    'Hirsova': [("Urziceni", 98), ("Eforie", 86)],
    'Iasi': [("Neamt", 87), ("Vaslui", 92)],
    'Lugoj': [("Timisoara", 111), ("Mehadia", 70)],
    'Mehadia': [("Lugoj", 70), ("Dobreta", 75)],
    'Neamt': [("Iasi", 87)],
    'Oradea': [("Zerind", 71), ("Sibiu", 151)],
    'Pitesti': [("Rimnicu Vilcea", 97), ("Bucharest", 211), ("Craiova", 118)],
    'Rimnicu Vilcea': [("Sibiu", 80), ("Pitesti", 97), ("Craiova", 146)],
    'Sibiu': [("Oradea", 151), ("Arad", 140), ("Rimnicu Vilcea", 60), ("Fagaras", 99)],
    'Timisoara': [("Arad", 118), ("Lugoj", 111)],
    'Urziceni': [("Bucharest", 85), ("Vaslui", 142), ("Hirsova", 98)],
    'Vaslui': [("Iasi", 92), ("Urziceni", 142)],
    'Zerind': [("Arad", 75), ("Oradea", 71)]
}
graph1 = Graph(adjac_lis)
graph1.a_star_algorithm('Lugoj', 'Bucharest')

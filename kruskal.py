class Graph:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.edges = []  # List to store all edges

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))  # Store edges as (weight, u, v)

    def find_parent(self, parent, node):
        if parent[node] != node:
            parent[node] = self.find_parent(parent, parent[node])
        return parent[node]

    def union_sets(self, parent, rank, u_root, v_root):
        if rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        elif rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        else:
            parent[v_root] = u_root
            rank[u_root] += 1

    def kruskal_mst(self):
        # Sort edges by weight
        self.edges.sort()
        parent = [i for i in range(self.V)]
        rank = [0] * self.V
        mst = []
        total_cost = 0

        for weight, u, v in self.edges:
            u_root = self.find_parent(parent, u)
            v_root = self.find_parent(parent, v)

            if u_root != v_root:
                mst.append((u, v, weight))
                total_cost += weight
                self.union_sets(parent, rank, u_root, v_root)

        print("Edges in Minimum Spanning Tree:")
        for u, v, weight in mst:
            print(f"{u} -- {v} == {weight}")
        print("Total cost of MST:", total_cost)


# Example usage
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal_mst()

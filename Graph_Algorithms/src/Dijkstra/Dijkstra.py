from collections import defaultdict
import math

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes:
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      try:
          weight = current_weight + graph.distances[(min_node, edge)]
      except:
          weight = current_weight + math.inf
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path


def main():

    #initializing values
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')

    g.add_edge('a', 'b', 10)
    g.add_edge('b', 'c', 2)
    g.add_edge('a', 'c', 1)
    g.add_edge('c', 'd', 1)
    g.add_edge('b', 'd', 8)

    #output
    print(dijkstra(g, 'a'))

main()

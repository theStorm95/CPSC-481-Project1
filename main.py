from bfs import bfs
from graph import build_graph

def main():
  graph = build_graph()
  
  print(graph)
  bfs(graph, 'A', 'F')
  
if __name__ == "__main__":
  main()
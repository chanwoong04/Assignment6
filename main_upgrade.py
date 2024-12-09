from module_b import Graph
from module_a import Categorylist


cat=Categorylist()
cat.create_json_files()

graph = Graph()
subject = graph.input()
graph.LineGraph(subject)

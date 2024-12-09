from module_b_upgrade5 import Graph
from module_a_upgrade3 import Categorylist


cat=Categorylist()
cat.create_json_files()

graph = Graph()
subject = graph.input()
graph.LineGraph(subject)
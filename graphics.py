# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.

import matplotlib.pyplot as plt



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import numpy as np
import networkx as nx
import matplotlib
import networkx as nx

bde = nx.DiGraph()
bde.add_nodes_from(["A", "B", "C"])
bde.add_edges_from([("A", "B"), ("B", "C")])
nx.draw_networkx(bde, arrows=True, node_size=1600, node_color='y')
nx.circular_layout(bde)
plt.show()

jt = nx.junction_tree(bde)
nx.draw_networkx(jt, node_size=1050, node_color='y')
nx.planar_layout(jt)
plt.show()

ea = nx.DiGraph()
ea.add_nodes_from(["B", "E", "A", "J", "M"], )
ea.add_edges_from([("B", "A"), ("E", "A"), ("A", "J"), ("A", "M")])
nx.draw_networkx(ea, arrows=True, node_size=1050, node_color='r')
plt.show()

jt2 = nx.junction_tree(ea)
nx.draw_networkx(jt2, node_size=1050, node_color='r')
nx.circular_layout(jt2)
plt.show()

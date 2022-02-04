# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import Inference as I


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Memorizzo la rete del file .bn , abrrevio il nome dei nodi alla iniziale

bde = I.BeliefNetwork(["B", "E", "A", "J", "M"], {"B": [], "E": [], "A": ["E", "B"], "J": ["A"],
                                                  "M": ["A"]}, {"B": [0.99, 0.01], "E": [0.98, 0.02],
                                                                "A":
                                                                    [0.999, 0.06, 0.71, 0.05, 0.001, 0.94, 0.29, 0.95],
                                                                "J": [0.95, 0.1, 0.05, 0.9],
                                                                "M": [0.99, 0.3, 0.01, 0.7]})

# Memorizzo la rete simple.bn

simple = I.BeliefNetwork(["A", "B", "C"], {"A": [], "B": ["A"], "C": []},
                         {"A": [0.3, 0.7], "B": [0.4, 0.6, 0.1, 0.9], "C": [0.4, 0.6, 0.1, 0.9]})

# Memorizzo il Junction Tree del file bde_test.bn , https://github.com/francescobaio/Elaborato_AI/blob/main/JunctionTree%20EarthQuake.bn.png


Jt1 = I.JunctionTree(["AJ", "AM", "ABE"], ["A"], [("AJ", "A", "AM"), ("ABE", "A", "AJ"), ("ABE", "A", "AM")], bde)

# Memorizzo il Junction Tree del file simple_bn , https://github.com/francescobaio/Elaborato_AI/blob/main/JunctionTree%20simple.bn.png


Jt2 = I.JunctionTree(["AB", "BC"], ["B"], ["AB", "B", "BC"], simple)

# Esempi relativi all'uso della definizione di probabilità condizionale

# Calcolo della probabilità congiuntà tramite la def. di questa per una Belief NetWork

for i in range(len(Jt1.clusters)):
    print(Jt1.CPTc[Jt1.clusters[i]])

print("____")

for i in range(len(bde.nodes)):
    print(bde.cpt[bde.nodes[i]])

print("____")

print(Jt1.CPTc["AJ"])

print("____")

Jt1.inizialization()

print("____")

for i in range(len(Jt1.clusters)):
    print(Jt1.CPTc[Jt1.clusters[i]])

print("_____")

for i in range(len(Jt1.separators)):
    print(Jt1.CPTs[Jt1.separators[i]])

print("_____")

for i in range(len(Jt1.clusters)):
    print(Jt1.CPTc[Jt1.clusters[i]])

print("_____")

sum = bde.joint_probability()
print(bde.joint_p)
print(sum)

print("_____")

for i in range(len(Jt1.clusters)):
    print(Jt1.CPTc[Jt1.clusters[i]])

print("_____")

for i in range(len(Jt1.clusters)):
    print(Jt1.CPTc[Jt1.clusters[i]])

print("_____")

cpt = bde.calculate_cp("B", ["J", "M"], {"J": 1, "M": 0})
print(cpt)

CPT1 = bde.marginalize("B", cpt)
print(CPT1)

print("_____")

Jt1.give_evidence(["J", "M"], {"J": 1, "M": 0})

for i in range(len(Jt1.clusters)):
    print(Jt1.CPTc[Jt1.clusters[i]])

Jt1.collect_evidence("AJ")
Jt1.distribute_evidence("AJ")

bcpt = Jt1.marginalize("B")
print(bcpt)

# B = true e J = true

"""
print("_____")

Jt1.CPTc["ABE"][1][3] = 0
Jt1.CPTc["ABE"][2][3] = 0
Jt1.CPTc["ABE"][5][3] = 0
Jt1.CPTc["ABE"][6][3] = 0
Jt1.CPTc["AJ"][1][2] = 0
Jt1.CPTc["AJ"][3][2] = 0

print("_____")

for i in range(len(Jt1.clusters)):
    print(Jt1.CPTc[Jt1.clusters[i]])

print("_____")
Jt1.collect_evidence("ABE")

print("_____")
for i in range(len(Jt1.clusters)):
    print(Jt1.CPTc[Jt1.clusters[i]])

print("_____")
Jt1.distribute_evidence("ABE")

print("_____")
for i in range(len(Jt1.clusters)):
    print(Jt1.CPTc[Jt1.clusters[i]])

print("_____")

# cpt2 = bde.marginalize("J",["A"])
# print(cpt2)


# print("_____")
"""

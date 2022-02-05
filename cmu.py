import Inference as I

bde = I.BeliefNetwork(["B", "E", "A", "J", "M"], {"B": [], "E": [], "A": ["E", "B"], "J": ["A"],
                                                  "M": ["A"]}, {"B": [0.99, 0.01], "E": [0.98, 0.02],
                                                                "A":
                                                                    [0.999, 0.71, 0.06, 0.05, 0.001, 0.29, 0.94, 0.95],
                                                                "J": [0.95, 0.1, 0.05, 0.9],
                                                                "M": [0.99, 0.3, 0.01, 0.7]})

Jt1 = I.JunctionTree(["AJ", "AM", "ABE"], ["A"], [("AJ", "A", "AM"), ("ABE", "A", "AJ"), ("ABE", "A", "AM")], bde)

for i in range(len(Jt1.clusters)):
    print(Jt1.CPTc[Jt1.clusters[i]])

print("____")

for i in range(len(bde.nodes)):
    print(bde.cpt[bde.nodes[i]])

""""
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

print("-----")

Jt1.absorption(Jt1.CPTc["AJ"], Jt1.CPTs["A"], Jt1.CPTc["AM"])

print(Jt1.CPTc["AJ"])
print(Jt1.CPTc["AM"])
print(Jt1.CPTs["A"])


list = Jt1.find_leafs("AJ")
print(list)

print("_____")

for i in range(len(Jt1.clusters)):
    print(Jt1.CPTc[Jt1.clusters[i]])

print("_____")

sum = bde.joint_probability()
print(bde.joint_p)
print(sum)

print("_____")

Jt1.CPTc["AJ"][2][2] = 0
Jt1.CPTc["AJ"][4][2] = 0

Jt1.collect_evidence("AJ")

print("_____")

for i in range(len(Jt1.clusters)):
    print(Jt1.CPTc[Jt1.clusters[i]])

print("_____")


Jt1.distribute_evidence("AJ")

for i in range(len(Jt1.clusters)):
   print(Jt1.CPTc[Jt1.clusters[i]])



cpt = bde.calculate_cp("A", ["J"])
print(cpt)


#cpt2 = bde.marginalize("J",["A"])
#print(cpt2)



# print("_____")
"""

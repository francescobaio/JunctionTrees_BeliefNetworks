import Inference as I

simple = I.BeliefNetwork(["A", "B", "C"], {"A": [], "B": ["A"], "C": ["B"]},
                         {"A": [0.3, 0.7], "B": [0.4, 0.6, 0.1, 0.9], "C": [0.4, 0.6, 0.1, 0.9]})

Jt2 = I.JunctionTree(["AB", "BC"], ["B"], [("AB", "B", "BC")], simple)

for i in range(len(Jt2.clusters)):
    print(Jt2.CPTc[Jt2.clusters[i]])

print("____")

for i in range(len(simple.nodes)):
    print(simple.cpt[simple.nodes[i]])

print("____")

sum = simple.joint_probability()
print(simple.joint_p)
print(sum)

cpt = simple.marginalize("B", ["A"])
print(cpt)

""""

print("____")

Jt2.inizialization()


for i in range(len(Jt2.clusters)):
    print(Jt2.CPTc[Jt2.clusters[i]])

print("____")

for i in range(len(Jt2.separators)):
    print(Jt2.CPTs[Jt2.separators[i]])

print("-----")

Jt2.absorption(Jt2.CPTc["AB"],Jt2.CPTs["B"], Jt2.CPTc["BC"])

print(Jt2.CPTc["AB"])
print(Jt2.CPTc["BC"])
print(Jt2.CPTs["B"])


list = Jt2.find_leafs("AB")
print(list)

print("_____")

for i in range(len(Jt2.clusters)):
    print(Jt2.CPTc[Jt2.clusters[i]])

print("_____")

sum = simple.joint_probability()
print(simple.joint_p)
print(sum)

print("_____")
print(Jt2.CPTc["AB"])

Jt2.CPTc["AB"][1][2] = 0
Jt2.CPTc["AB"][3][2] = 0

print(Jt2.CPTc["AB"])


for i in range(len(Jt2.clusters)):
    print(Jt2.CPTc[Jt2.clusters[i]])

for j in range(len(Jt2.separators)) :
    print(Jt2.CPTs[Jt2.separators[j]])

Jt2.collect_evidence("AB")

print("_____")

for i in range(len(Jt2.clusters)):
    print(Jt2.CPTc[Jt2.clusters[i]])

for j in range(len(Jt2.separators)) :
    print(Jt2.CPTs[Jt2.separators[j]])
print("_____")



Jt2.distribute_evidence("AB")

for i in range(len(Jt2.clusters)):
   print(Jt2.CPTc[Jt2.clusters[i]])


for j in range(len(Jt2.separators)) :
    print(Jt2.CPTs[Jt2.separators[j]])


cpt = bde.marginalize("A", ["J"])
print(cpt)


cpt2 = bde.marginalize("J",["A"])
print(cpt2)

"""

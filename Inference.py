import math
import random

import numpy as np
import python_algorithms.basic.union_find as uf


class BeliefNetwork:
    def __init__(self, nodes, parents, cpt):
        self.nodes = nodes
        # Parents è un dizionario che associa a una variabile (nodo) i suoi parents.
        self.parents = parents
        #  Cpt è un dizionario che associa a una variabile (chiave) la sua tabella cpt.
        self.cpt = cpt
        # Variables è un dizionario che associa a una variabile(chiave) un valore intero
        self.variables = {}

        self.joint_p = np.zeros((2 ** len(self.nodes) + 1, len(self.nodes) + 1))

        for i in range(len(self.nodes)):
            self.variables[nodes[i]] = i + 1

        for i in range(len(self.nodes)):
            CPT = self.cpt[self.nodes[i]].copy()
            self.cpt[self.nodes[i]] = np.zeros(
                ((2 ** ((len(self.parents[self.nodes[i]])) + 1)) + 1, (len(self.parents[self.nodes[i]])) + 2))
            self.cpt[self.nodes[i]][0][0] = self.variables[self.nodes[i]]
            for j in range(len(self.parents[self.nodes[i]])):
                self.cpt[self.nodes[i]][0][j + 1] = self.variables[self.parents[self.nodes[i]][j]]

            for k in range((2 ** (len(self.parents[self.nodes[i]]) + 1))):
                quoziente = k
                for t in range(len(self.parents[self.nodes[i]]), -1, -1):
                    self.cpt[self.nodes[i]][k + 1][t] = quoziente % 2
                    quoziente = math.floor(quoziente / 2)

            for p in range((2 ** ((len(self.parents[self.nodes[i]])) + 1))):
                self.cpt[self.nodes[i]][p + 1][(len(self.parents[self.nodes[i]])) + 1] = CPT[p]

    def joint_probability(self):
        for j in range(len(self.nodes)):
            self.joint_p[0][j] = self.variables[self.nodes[j]]
        for k in range(2 ** len(self.nodes)):
            self.joint_p[k + 1][len(self.nodes)] = 1
            quoziente = k
            # parto dal termine della matrice si prende l'indice della riga e si fa modulo 2 .
            for t in range(len(self.nodes) - 1, -1, -1):
                self.joint_p[k + 1][t] = quoziente % 2
                quoziente = math.floor(quoziente / 2)

        # for per capire quali nodi non hanno i padri
        # list -> lista con indici dove sono i nodi nelle joint_p
        # queue -> nodi
        for i in range(len(self.nodes)):
            table = JunctionTree.product(self, self.joint_p, self.cpt[self.nodes[i]])




class JunctionTree:
    def __init__(self, clusters, separators, egdes, beliefNetwork):
        # Clusters è una lista di stringhe ognuna rappresenta un gruppo di variabili originali "ABC"
        self.clusters = clusters
        self.separators = separators
        self.beliefNetwork = beliefNetwork
        # CPTs e CPTc sono due dizionari che associano rispettivamente la stringa corrispondente al separatore/cluster
        # alla sua CPT
        self.CPTs = {}
        self.CPTc = {}
        # Edges è la liste degli archi del Jt , questi sono delle triplette (cluster,separatore,cluster)
        self.edges = egdes
        for i in range(len(self.clusters)):
            self.CPTc[self.clusters[i]] = np.zeros((2 ** len(self.clusters[i]) + 1, len(self.clusters[i]) + 1))
            for j in range(len(self.clusters[i])):
                self.CPTc[self.clusters[i]][0][j] = beliefNetwork.variables[self.clusters[i][j]]
            for k in range(2 ** len(self.clusters[i])):
                quoziente = k
                # parto dal termine della matrice si prende l'indice della riga e si fa modulo 2 .
                for t in range(len(self.clusters[i]) - 1, -1, -1):
                    self.CPTc[self.clusters[i]][k + 1][t] = quoziente % 2
                    quoziente = math.floor(quoziente / 2)

        for i in range(len(self.separators)):
            self.CPTs[self.separators[i]] = np.zeros((2 ** len(self.separators[i]) + 1, len(self.separators[i]) + 1))
            for j in range(len(self.separators[i])):
                self.CPTs[self.separators[i]][0][j] = beliefNetwork.variables[self.separators[i][j]]
            for k in range(2 ** len(self.separators[i])):
                quoziente = k
                for t in range(len(self.separators[i]) - 1, -1, -1):
                    self.CPTs[self.separators[i]][k + 1][t] = quoziente % 2
                    quoziente = math.floor(quoziente / 2)

    def inizialization(self):
        # inizializzo le cpt dei cluster e separatori a tutti elementi a 1
        for i in range(len(self.clusters)):
            for j in range((2 ** len(self.clusters[i]))):
                #   for k in range(len(self.clusters[i]) + 1):
                self.CPTc[self.clusters[i]][j + 1][len(self.clusters[i])] = 1

        for i in range(len(self.separators)):
            for j in range((2 ** len(self.separators[i]))):
                #   for k in range(len(self.separators[i]) + 1):
                self.CPTs[self.separators[i]][j + 1][len(self.separators[i])] = 1

        found = True

        for i in range(len(self.beliefNetwork.variables)):
            for j in range(len(self.clusters)):
                if self.clusters[j].find(self.beliefNetwork.nodes[i]) != -1:
                    for k in range(len(self.beliefNetwork.parents[self.beliefNetwork.nodes[i]])):
                        if self.clusters[j].find(self.beliefNetwork.parents[self.beliefNetwork.nodes[i]][k]) == -1:
                            found = False
                    if found == True:
                        self.product(self.CPTc[self.clusters[j]],
                                     self.beliefNetwork.cpt[self.beliefNetwork.nodes[i]])
                        break
                    else:
                        found = True

    def product(self, tv, ts):
        # Trovo le colonne delle variabili in comune tra i due cluster
        # list è una variabile che contiene gli indici delle colonne delle variabili in comune
        list = []
        # found è un var booleana che mi dice se tutta la riga della prima tabella ha negli
        # attributi in comune gli stessi valori di una delle tuple della seconda tabella
        found = True
        for i in range(tv.shape[1] - 1):
            for j in range(ts.shape[1] - 1):
                if tv[0][i] == ts[0][j]:
                    list.append((i, j))

        for k in range(tv.shape[0] - 1):
            for y in range(ts.shape[0] - 1):
                for t in range(len(list)):
                    if tv[k + 1][list[t][0]] != ts[y + 1][list[t][1]]:
                        found = False
                if found == True:
                    tv[k + 1][tv.shape[1] - 1] = tv[k + 1][tv.shape[1] - 1] * ts[y + 1][ts.shape[1] - 1]
                else:
                    found = True

    def division(self, tv, ts):
        list = []
        # found è un var booleana che mi dice se tutta la riga della prima tabella ha negli
        # attributi in comune gli stessi valori di una delle tuple della seconda tabella
        found = True
        for i in range(tv.shape[1] - 1):
            for j in range(ts.shape[1] - 1):
                if tv[0][i] == ts[0][j]:
                    list.append((i, j))

        for k in range(tv.shape[0] - 1):
            for y in range(ts.shape[0] - 1):
                for t in range(len(list)):
                    if tv[k + 1][list[t][0]] != ts[y + 1][list[t][1]]:
                        found = False
                if found == True:
                    if round(tv[k + 1][tv.shape[1] - 1] / ts[y + 1][ts.shape[1] - 1]) != 0:
                        tv[k + 1][tv.shape[1] - 1] = tv[k + 1][tv.shape[1] - 1] / ts[y + 1][ts.shape[1] - 1]
                else:
                    found = True

    def absorption(self, tv, ts, tw):
        # uso il metodo copy di Numpy per creare una nuova tabella con i valori di ts
        ts_new = ts.copy()
        list = []
        found = True
        check = True
        for i in range(tv.shape[1] - 1):
            for j in range(ts.shape[1] - 1):
                if tv[0][i] == ts[0][j]:
                    list.append((i, j))
        # utilizzo la funzione Union Find per creare dei gruppi nelle righe di tv
        # all'inizio sets contiene tanti gruppi quanti sono le righe di UF
        sets = uf.UF(tv.shape[0] - 1)
        while sets.count() > ts.shape[0] - 1:
            # itero prendendo una riga della tabella e tutte le successive sulle variabili(colonne) in comune
            for i in range(tv.shape[0] - 2):
                for j in range(i + 2, tv.shape[0]):
                    for k in range(len(list)):
                        if tv[i + 1][list[k][0]] != tv[j][list[k][0]]:
                            found = False
                        # nel caso in cui ho trovato un riga valori uguali negli attributi
                        # in comune con ts, verifico se non fa parte già del set con la funzione
                        # connected
                        # i sets partono da zero
                    if found == True and not sets.connected(i, j - 1):
                        sets.union(i, j - 1)
                        for y in range(ts.shape[0] - 1):
                            for x in range(len(list)):
                                if tv[i + 1][list[x][0]] != ts[y + 1][list[x][1]]:
                                    check = False
                            if check == True:
                                ts[y + 1][ts.shape[1] - 1] = tv[i + 1][tv.shape[1] - 1] + tv[j][tv.shape[1] - 1]
                            else:
                                check = False
                    else:
                        found = True

        self.division(ts, ts_new)
        self.product(tw, ts)

    def distribute_evidence(self, root):
        # ricevo un nodo arbitrario,lo considero come la radice dell'albero
        queue = self.edges

        list = []
        list.append(root)
        edges = []

        while len(queue) > 0:
            for i in range(len(list)):
                size = len(list)
                noedges = self.find_edges(list[i])
                for k in range(len(noedges)):
                    if noedges[k] in queue:
                        edges.append(noedges[k])

                for j in range(len(edges)):
                    if list[i] in edges[j]:
                        if list[i] == edges[j][0]:
                            self.absorption(self.CPTc[list[i]], self.CPTs[edges[j][1]], self.CPTc[edges[j][2]])
                            if edges[j][2] not in list:
                                list.append(edges[j][2])
                            queue.remove(edges[j])
                        else:
                            self.absorption(self.CPTc[edges[j][0]], self.CPTs[edges[j][1]], self.CPTc[list[i]])
                            if edges[j][0] not in list:
                                list.append(edges[j][0])
                            queue.remove(edges[j])

                edges.clear()
                if len(list) > size:
                    list.remove(list[i])

    def find_leafs(self, root):

        queue = []
        for i in range(len(self.edges)):
            queue.append(self.edges[i])

        list = []
        list.append(root)

        edges = []

        while len(queue) > 0:
            for i in range(len(list)):
                size = len(list)
                noedges = self.find_edges(list[i])
                for k in range(len(noedges)):
                    if noedges[k] in queue:
                        edges.append(noedges[k])

                for j in range(len(edges)):
                    if list[i] in edges[j]:
                        if list[i] == edges[j][0]:
                            if edges[j][2] not in list:
                                list.append(edges[j][2])
                            queue.remove(edges[j])
                        else:
                            if edges[j][0] not in list:
                                list.append(edges[j][0])
                            queue.remove(edges[j])

                edges.clear()
                if len(list) > size:
                    list.remove(list[i])

        return list

    def collect_evidence(self, root):

        list = self.find_leafs(root)

        for i in range(len(list)):
            while list[i] != root:
                for j in range(len(self.edges)):
                    if list[i] in self.edges[j]:
                        if list[i] == self.edges[j][0]:
                            self.absorption(self.CPTc[list[i]], self.CPTs[self.edges[j][1]],
                                            self.CPTc[self.edges[j][2]])
                            list[i] = self.edges[j][2]
                        else:
                            self.absorption(self.CPTc[self.edges[j][0]], self.CPTs[self.edges[j][1]],
                                            self.CPTc[list[i]])

                            list[i] = self.edges[j][0]

    def find_edges(self, node):

        list = []

        for i in range(len(self.edges)):
            if node in self.edges[i]:
                list.append(self.edges[i])

        return list

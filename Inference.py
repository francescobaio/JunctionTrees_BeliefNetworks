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
            quoziente = k
            # parto dal termine della matrice si prende l'indice della riga e si fa modulo 2 .
            for t in range(len(self.nodes) - 1, -1, -1):
                self.joint_p[k + 1][t] = quoziente % 2
                quoziente = math.floor(quoziente / 2)

        # for i in range(2 ** len(self.nodes)):
        #  list = []
        # for j in range(len(self.nodes)-1):

        # Manca fare il join tra le cpt iniziali


class JunctionTree:
    def __init__(self, clusters, separators, egdes, beliefNetwork):
        # Clusters è una lista di stringhe ognuna rappresenta un gruppo di variabili originali "ABC"
        self.clusters = clusters
        self.separators = separators
        self.beliefNetwork = beliefNetwork
        # CPTs e CPTc sono due dizionari che associano rispettivamente la stringa corrispondente al separatore/cluster
        # a una lista , la sua cpt
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
                    if (tv[k + 1][tv.shape[1] - 1] / ts[y + 1][ts.shape[1] - 1]) != 0:
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

    def distribute_evidence(self, root, queue):
        # ricevo un nodo arbitrario,lo considero come la radice dell'albero
        if np.size(queue) > 0:
            for i in range(len(queue)):
                if root in queue[i]:
                    if queue[i][0] == root:
                        self.absorption(self.CPTc[root], self.CPTs[queue[i][1]], self.CPTc[queue[i][2]])
                        cls = queue[i][2]
                        queue.remove(i)
                        self.distribute_evidence(cls, queue)
                    else:
                        self.absorption(self.CPTc[queue[i][0]], self.CPTs[queue[i][1]], root)
                        cls = queue[i][0]
                        queue.remove(i)
                        self.division(cls, queue)

    def find_leafs(self, root):

        queue = self.edges
        list = []
        list.append(root)
        found = True
        j = 0

        while len(queue) > 0:
            for i in range(len(list)):
                while len(queue) > 0:
                    if list[i] in queue[j]:
                        if list[i] == queue[j][0]:
                            list.append(queue[j][2])
                            queue.remove(queue[j])
                            for k in range(len(queue)):
                                if list[i] in queue[k]:
                                    found = False
                            if found == True:
                                list.remove(queue[j][0])
                            j = j - 1
                        else:
                            list.append(queue[j][0])
                            queue.remove(queue[j])
                            for t in range(len(queue)):
                                if list[i] in queue[t]:
                                    found = False
                            if found == True:
                                list.remove(queue[j][2])
                            j = j - 1

                    j = j + 1

        return list

    def collect_evidence(self, root):

        list = self.find_leafs(root)

        for i in range(len(list)):
            while list[i] != root:
                for j in range(len(self.edges)):
                    if list[i] in self.edges[j]:
                        if list[i] == self.edges[j][0]:
                            self.absorption(self.CPTc[list[i]], self.CPTc[self.edges[j][1]],
                                            self.CPTc[self.CPTc[self.edges[j][2]]])
                            list[i] = self.edges[j][2]
                        else:
                            self.absorption(self.CPTc[self.edges[j][0]], self.CPTc[self.edges[j][1]],
                                            self.CPTc[self.CPTc[list[i]]])
                            list[i] = self.edges[j][0]

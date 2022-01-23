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

        for i in range(len(self.nodes)):
            self.variables[nodes[i]] = i

    def joint_probability(self):
        joint = np.zeros(2 ** len(self.nodes) + 1, len(self.nodes) + 1)
        for j in range(len(self.nodes)):
            joint[0][j] = self.nodes[j]
        for k in range(2 ** len(self.nodes) + 1):
            quoziente = k
            # parto dal termine della matrice si prende l'indice della riga e si fa modulo 2 .
            for t in range(len(self.nodes), -1, -1):
                joint[k + 1][t] = quoziente % 2
                quoziente = math.floor(quoziente / 2)

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

    # Questo è il metodo che definisce la propagazione dei messaggi.
    def inizialization(self):
        # inizializzo le cpt dei cluster e separatori a tutti elementi a 1
        for i in range(len(self.clusters)):
            self.CPTc[self.clusters[i]][:] = 1
        for j in range(len(self.separators)):
            self.CPTs[self.separators][j][:] = 1

        found = True

        for i in range(len(self.beliefNetwork.variables)):
            for j in range(len(self.clusters)):
                if self.clusters[j].find(self.beliefNetwork.nodes[i]) != -1:
                    for k in range(len(self.beliefNetwork.parents[self.beliefNetwork.nodes[i]])):
                        if self.clusters[j].find(self.beliefNetwork.parents[self.beliefNetwork.nodes[i]][k]) == -1:
                            found = False
                    if found == True:
                        self.product(self, self.CPTc[self.clusters[j]],
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
                for i in range(len(tv.shape[0]) - 2):
                    for j in range(i + 2, len(tv.shape[0])):
                        for k in range(len(list)):
                            if tv[i + 1][list[k][0]] != tv[j][list[k][0]]:
                                found = False
                        # nel caso in cui ho trovato un riga valori uguali negli attributi
                        # in comune con ts, verifico se non fa parte già del set con la funzione
                        # connected
                        if found == True and not sets.connected(i, j):
                            sets.union(i, j)
                            for y in range(len(ts.shape[0]) - 1):
                                for x in range(len(list)):
                                    if tv[i + 1][list[x][0]] != ts[y + 1][list[x][1]]:
                                        check = False
                                if check == True:
                                    ts[y][ts.shape[1] - 1] += (tv[i + 1][tv.shape[1] - 1] + tv[j][tv.shape[1] - 1])
                                else:
                                    check = False
                        else:
                            found = False

            self.division(self, ts, ts_new)
            self.product(self, tw, ts)

        def distribute_evidence(self, root):
            # ricevo un nodo arbitrario,lo considero come la radice dell'albero
            for i in range(len(self.egdes)):
                if root in self.egdes[i]:
                    if self.egdes[0] == root:
                        absorption(self, self.CPTc[root], self.CPTs[self.egdes[1]], self.CPTc[self.egdes[2]])
                        distribute_evidence(self, self.egdes[2])
                    else:
                        absorption(self, self.CPTc[self.egdes[0]], self.CPTs[self.egdes[1]], root)
                        distribute_evidence(self, self.egdes[0])

        def find_leaf(self, root):
            list = []
            for i in range(len(self.egdes)):
                if root in self.egdes[i]:
                    if self.egdes[0] == root:
                        find_leaf(self, self.egdes[2])
                    else:
                        find_leaf(self, self.egdes[0])

        #  Fix this

        # def collect_evidence(self, root):
    # chiama la distribute una volta che dalle foglie è ritornato alla root

    #  Fix me

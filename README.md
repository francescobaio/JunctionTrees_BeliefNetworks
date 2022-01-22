# Elaborato_AI
Repository per Elaborato esame Intelligenza Artificiale . \\
Argomento : Inferenza con Junction Trees sui Belief Networks

BRANCH Main : Informazioni sul dataset usato , come graficare , Relazione descrittiva del codice.  ||
BRANCH Master : Modulo Software : Inference.py -> contiene le classi Junction Tree e Belief Network , i metodi per l'inferenza probabilistica (presenti bug e fix me)
                                  Main.py -> utilizzo del software di inferenza

Questo repository contiene un modulo software utile alla propagazione dell'informazione all'interno delle Belief Networks.
L'algoritmo di propagazione usa l'idea dello scambio di messaggi nel Junction Tree associato alla Belief Network stessa costruito manualmente e già fornito 
in pasto al modulo software stesso.

Non è quindi presente la parte di algoritmo che porti da una Belief Network al suo corrispondente Junction Tree ma questa può essere svolta autonomamente per reti molto piccole.


Il funzionamento del modulo è testato sulle reti https://github.com/ncullen93/pyBN/blob/master/data/earthquake.bn e https://github.com/ncullen93/pyBN/blob/master/data/simple.bn.
E' presente una cartella aggiuntiva che presenta la forma dei Junction Tree associati a queste semplici reti.




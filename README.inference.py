Questo file di testo spiega lo scopo del file Inference.py.

Al suo interno sono presenti due classi : la classe Belief Network e la classe Junction Tree.
  
CLASSE Belief Network :

Questa classe serve alla rappresentazione di una Rete Bayesiana. Il suo costruttore riceve come parametri la lista dei nodi della rete e dei rispettivi padri,le cpt (conditional probability table)
ad essi associate e un dizionario Variables che associa un intero ad ogni variabile della rete.(utile per avere un riferimento di tipo hashable).
E' presente inoltre l'attributo che rappresenta la tabella della probabilità congiunta della rete (joint_p)

Metodi della classe e loro funzionalità : 
  
- JOINT_PROBABILITY : questo metodo crea la tabella della joint probability,inserisce con il metodo delle divisioni le interpretazioni delle variabili e calcola la probabilità congiunta
                      inserendola nell'ultima colonna della jpt attraverso il prodotto delle cpt delle variabili. Si utilizza il metodo product() della classe Junction Tree per fare questo . (vedere sotto)
- MARGINALIZE  :  questo metodo applica la definizione di probabilità condizionale , ricevendo una variabile della rete e una lista di variabili su cui viene fatta evidenza, 
                  va a utilizzare una copia della tabella della probabilità congiunta che viene marginalizzata (attraverso l'uso della creazione di gruppi di righe con UF union find) 
                  sull'unione delle variabili passate.
                                                                                                               
                                                             
- NORMALIZE : metodo utile all'interno del MARGINALIZE al fine di normalizzare i risultati ottenuti, questo viene fatto a sua volta marginalizzando la tabella della probabilità 
              congiunta sulle variabili su cui è fatta evidenza.
                                                                                                                
                                                                                                               
                                                                                                              

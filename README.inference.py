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
                                                                                                               
                                                             
- CALCULATE_JP : metodo all'interno del quale attraverso il metodo MARGINALIZE si calcola sia la marginalizzazione della probabilità congiunta rispetto all'unione dell'insieme
                 dato dalla variabile e la lista delle variabili su cui si fa evidenza. Calcolata le due cpt marginalizzate si usa il metodo DIVISION della classe Junction Tree 
                 che applica una divisione nell'algebra delle belief tables.
                                                                                                                
     
-- GIVE_EVIDENCE : questo metodo serve a poter dare evidenza andando a porre a zero tutte le righe della jpt che non hanno risultati concordi all'evidenza data.                                                                                                                
                                                                                                                
                                                                                                                
-------------------------------------------------------------------------------------------------------------                                                                                                         
                                                                                                              
CLASSE JUNCTION TREE : 
                                                                                                            
Questa classe permette la rappresentazione di un Junction Tree definito su una Belief Network, ha lo scopo di calcolare le probabilità condizionali propagando l'informazione
attraverso lo scambio di messaggi nella rete.                                                                                                               
                                                                                                                
I parametri che la classe riceve sono : 

- lista dei clusters 
- lista dei separatori 
- lista degli archi  -> triplette (cluster,separatore,cluster)                                            ì
-  Belief Network -> la rete su cui questo Jt è definito 
- un dizionario CPTc che associa a ogni cluster la sua CPT corrispondente 
. un dizionario CPTs che associa a ogni separatore la sua CPT corrispondente 
                                                                                                                
                                                                                                                
 I metodi presenti nella classe sono :
                                                                                                                
                                                                                                                
 - INIZIALIZATION : questo metodo serve a inizializzare con degli uno le CPT dei clusters e dei separatori. 
                    Successivamente per ogni variabile trova un cluster che contiene sia lui che i suoi padri nella Bayesian Network associata e usa il metodo PRODUCT
                    per fare il prodotto tra la CPTc di quel cluster e la cpt della data variabile che contiene la probabilità condizionata di quella variabile dati i suoi padri.                                                                                            
                                                                                                                
                                                                                                                
                                                                                                                
 - PRODUCT :  Questo metodo viene utilizzato per eseguire il prodotto di tabelle di probabilità. Emula il Join dell'algebra relazionale, 
                riceve due tabelle in ingresso, seleziona tramite la prima riga quelle che sono le variabili in comune (si utilizza 
               il proprio intero associato). Queste vengono inserite in una lista e riga per riga si controlla se le righe delle due tabelle hanno gli stessi valori sulle variabili e se questo 
              accade si fa il prodotto delle probabilità. Il risultato è salvato nella prima tabella passata, essendo in tutte le situazioni un contenitore rispetto alla seconda. (ad es. cluster e separatore)
                                                                                                             
                                                                                                                
 - DIVISION : scopo analogo alla funzione PRODUCT.  
                                                                                                                
 - FIND _LEAFS : metodo che serve dato una root per il Junction Tree a trovarne le sue foglie. Il metodo ritorna la lista con le foglie del Junction Tree data la scelta fatta per la root.
                                                                                                                
-  FIND_EDGES : metodo che dato un cluster del Junction Tree ritorna una lista con all'interno gli archi ad esso connessi.
                                                                                                                
- FIND_NEIGHBOURS  : metodo che dato un cluster del Junction Tree ritorna una lista con i cluster a lui vicini nel Junction Tree.
                                                                                                                
Metodi finalizzati alla propagazione dei belief : 
                                                                                                                
- ABSORPTION : questo metodo serve per lo scambio dell'informazione tra due cluster della rete. Attraverso la marginalizzazione della Cpt del primo cluster,
               si trova l'informazione che il primo cluster conosce sulle variabili del separatore ovvero su quelle a comune con l'altro cluster dell'arco.
               La marginalizzazione viene svolta attraverso la creazione di gruppi di tuple sulla CPTc del cluster che hanno sugli attributi in comune con il separatore gli stessi valori, 
               si cercano poi le righe della CPTs del separatore che abbiano gli stessi valori e se trovate si sommano le probabilità memorizzandole nella CPT del separatore.
               Si memorizza poi nella CPTc dell'altro cluster il prodotto tra il suo valore originale e la divisione tra messaggio appena memorizzato e la tabella CPTs del separatore 
               originale.                                                                                                 
                                                                                                           
- DISTRIBUTE_EVIDENCE : questo metodo serve fissata una radice a distribuire l'informazione attraverso la ripetizione dell'ABSORPTION dalla radice stessa alle foglie.                                                                                                             
                                                                                                                
  
- COLLECT_EVIDENCE : questo metodo data una radice del Junction Tree , trova la lista delle foglie associate attraverso il FIND_LEAFS ed esegue degli ABSORPTION da ogni 
                     foglia fino alla radice scelta ,  rendendo cosi la rete informata.                                                                                       
                                                                                                                

  
- GIVE_EVIDENCE : questo metodo serve a poter dare evidenza andando a porre a zero tutte le righe della jpt che non hanno risultati concordi all'evidenza data. 
                                                                                                                
                                                                                                       
 - MARGINALIZE : marginalizza una CPTc di un cluster e trova come risultato una cpt associata a una variabile appartenente al cluster stesso.                                                                                                            -
                                                                                                                
                                                                                                                
                                                                                                                
                                                                                                                
                                                                                                               

import multiprocessing as mp
import traitement
from comm.testsParallelisme import communication

'''
Initialisation de tous les process/threads
- Gestionnaires de communication : LIDAR et STM32
- Processus de traitement de données : Répartition entre plusieurs fonctions gérant chacune un type de capteur
- Processus de prise de décision / parcours de graphe : A partir du graphe fourni dans la BD NoSQL, génère 
    instructions ensuite transmises par la Queue.
- Web app (django) : Communique par un socket avec la Queue d'instructions / lit son affichage dans la BD
- Socket
'''

if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    sem = mp.Semaphore(0)

    # Process traitement donnée capteur
    p1 = ctx.Process(target=traitement.demultiplexeur, args=q)
    p2 = ctx.Process(target=communication.comStm, args=(sem, q))

    # Process socket
    p1.start()
    p1.join()


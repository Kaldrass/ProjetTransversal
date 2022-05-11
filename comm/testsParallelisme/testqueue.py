import multiprocessing as mp
from mysite import manage


def web(q, s):
    s.release()
    q.put("instru1")


def traitement(q, s):
    s.release()
    q.put("instru2")


def gestCom(q, s):
    i = 0
    while i < 2:
        i += 1
        s.acquire()
        print(q.get())


if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    sem = mp.Semaphore(0)
    p = ctx.Process(target=web, args=(q, sem))
    p2 = ctx.Process(target=traitement, args=(q, sem))
    p3 = ctx.Process(target=gestCom, args=(q, sem))
    p.start()
    p2.start()
    p3.start()
    p.join()
    p2.join()
    p3.start()

import threading
import random

DIM_BUFFER = 7
N_PRODUTTORI = 4
N_CONSUMATORI = 3
N_RICHIESTE = 4

buffer = [None] * DIM_BUFFER
metti = 0
togli = 0

vuoto = threading.Semaphore(DIM_BUFFER)
pieno = threading.Semaphore(0)
mutexP = threading.Semaphore(1)
mutexC = threading.Semaphore(1)


def genera_drone():
    return f"DRN-{random.randint(100, 999)}"


class ProduttoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx
    selfdato=idx*100+1
    def run(self)
    global metti
    vuoto.aquire()
    mutexP.aquire()
    i_metti=metti
    metti= (metti+1)%DIM_BUFFER
    mutexP.release()
    buffer(i_metti)=selfdato
    print(PROD-(self.idx))prodotto(selfdato) in buffer(i_metti)
    self.dato+=1
    pieno.release()


class ConsumatoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx
        def.run(self)
        global togli
        While True:
        pieni.aquire()
        mutexC.aquire()
        i_togli=togli
        togli=(togli+1)% DIM_BUFFER
        mutexC.release()
        dato.buffer(i_togli)
         print(PROD-(self.idx))prodotto(selfdato) in buffer(i_togli)
    self.dato+=1


def main():
    global metti

    produttori = [ProduttoreThread(i + 1) for i in range(N_PRODUTTORI)]
    consumatori = [ConsumatoreThread(i + 1) for i in range(N_CONSUMATORI)]

    for c in consumatori:
        c.start()
        for p in produttori:
            p.start()
            for p in produttori:
                p.join()
    print("Tutti i sensori hanno terminato. Chiusura piste...")
    for_inrange (N_CONSUMATORI)
    for _ in range(N_CONSUMATORI):
     vuoto.acquire()
    buffer(metti)=None
    metti=(metti+1)%DIM_BUFFER
    pieno.release()
    for c in consumatori:
        c.join()
        pass

    # DA IMPLEMENTARE: join di tutti i consumatori

    print("Torre operativa chiusa.")


if __name__ == "__main__":
    main()

import queue
import threading
import time

def producent(q, limit):
    print("[Producent] Rozpoczynam generowanie liczb...")
    for i in range(1, limit + 1):
        print(f"[Producent] Dodał do kolejki liczbę: {i}")
        q.put(i)
        time.sleep(0.1)
    q.put(None)
    print("[Producent] Zakończył pracę.")

def konsument_parzyste(q):
    while True:
        item = q.get()
        
        if item is None:
            q.put(None) 
            print("[Konsument 1] Kończy pracę (koniec nasłuchu).")
            break
            
        if item % 2 == 0:
            print(f"[Konsument 1 - PARZYSTE] Pomyślnie przetworzono: {item}")
            time.sleep(0.3)
        else:
            q.put(item)
            time.sleep(0.01)

def konsument_nieparzyste(q):
    while True:
        item = q.get()
        
        if item is None:
            q.put(None)
            print("[Konsument 2] Kończy pracę (koniec nasłuchu).")
            break
            
        if item % 2 != 0:
            print(f"[Konsument 2 - NIEPARZYSTE] Pomyślnie przetworzono: {item}")
            time.sleep(0.3)
        else:
            q.put(item)
            time.sleep(0.01)


LIMIT_LICZB = 10
wspolna_kolejka = queue.Queue()

t_producent = threading.Thread(target=producent, args=(wspolna_kolejka, LIMIT_LICZB))
t_kons1 = threading.Thread(target=konsument_parzyste, args=(wspolna_kolejka,))
t_kons2 = threading.Thread(target=konsument_nieparzyste, args=(wspolna_kolejka,))

t_kons1.start()
t_kons2.start()
t_producent.start()

t_producent.join()
t_kons1.join()
t_kons2.join()
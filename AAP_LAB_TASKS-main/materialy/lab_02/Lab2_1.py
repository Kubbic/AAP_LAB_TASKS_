import requests
import time
import concurrent.futures

CAT_API_URL = "https://catfact.ninja/fact"

def get_fact(_=None):
    return requests.get(CAT_API_URL).json().get('fact')

start_seq = time.time()
facts_seq = [get_fact() for _ in range(20)]
time_seq = time.time() - start_seq

start_thr = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    facts_thr = list(executor.map(get_fact, range(20)))
time_thr = time.time() - start_thr

if time_thr < time_seq:
    roznica = time_seq - time_thr
    wspolczynnik = time_seq / time_thr
    print(f"Zaoszczędzony czas: {roznica:.2f} sekundy.") 
else:
    print("Nieoczekiwany czas wykonania")
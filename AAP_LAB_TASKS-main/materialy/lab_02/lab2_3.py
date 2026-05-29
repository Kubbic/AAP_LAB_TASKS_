import multiprocessing
import time
from lab2_functions import calculate_power_sum

if __name__ == "__main__":
    zakres_liczb = range(1, 10001)

    cores = multiprocessing.cpu_count()
    m_czas = time.time()
    
    with multiprocessing.Pool(processes=cores) as pool:
        wyniki_mp = pool.map(calculate_power_sum, zakres_liczb)
        
    czas_mp = time.time() - m_czas
    
    print(f"Przetworzono z powodzeniem: {len(wyniki_mp)} elementów.")
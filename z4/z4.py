import logging
import multiprocessing
import math

logging.basicConfig(level = logging.INFO)

def is_prime(num):
    if num == 2:
        return True
    elif num < 2 or num % 2 == 0:
        return False
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def find_twin_primes(start, end):
    twin_primes = []
    for num in range(start, end):
        if is_prime(num) and is_prime(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes

def worker(start, end, result_list):
    result_list.extend(find_twin_primes(start, end))

def main():
    start = 1
    end = 9999999
    number_of_processes = 6
    batch_size = (end - start) // number_of_processes


    manager = multiprocessing.Manager()
    results = manager.list()

    processes = []
    for i in range( number_of_processes):
        st = start + i * batch_size
        ed = st + batch_size if i <  number_of_processes - 1 else end
        p = multiprocessing.Process(target=worker, args=(st, ed, results))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    twin_primes = list(results)

    for pair in twin_primes:
        logging.info(f"{pair}")

if __name__ == "__main__":
    main()
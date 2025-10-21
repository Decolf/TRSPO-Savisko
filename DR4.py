import multiprocessing as mp
import time

# Савісько Андрій КІ-33

# Функція для обчислення кількості кроків за гіпотезою Колаца
def collatz_steps(n: int) -> int:
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def main():
    N = 10000000            # кількість чисел
    processes = mp.cpu_count()
    chunk = 20000            # розмір чанку для кожного процесу

    print(f"Обчислюємо для чисел від 1 до {N} на {processes} процесах.")
    t0 = time.time()

    total_steps = 0
    count = 0

    # Паралельні обчислення без синхронізації
    with mp.Pool(processes=processes) as pool:
        for s in pool.imap_unordered(collatz_steps, range(1, N + 1), chunksize=chunk):
            total_steps += s
            count += 1

    avg_steps = total_steps / N
    t1 = time.time()

    print(f"Кількість чисел: {count}")
    print(f"Середня кількість кроків: {avg_steps:.2f}")
    print(f"Час виконання: {t1 - t0:.2f} секунд")
    

if __name__ == "__main__":
    main()

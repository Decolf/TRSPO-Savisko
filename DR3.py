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
    N = 10000000   # кількість чисел
    processes = mp.cpu_count()  # можна вручну задати кількість процесів

    print(f"Обчислюємо для чисел від 1 до {N} на {processes} процесах.")

    numbers = range(1, N + 1)

    t0 = time.time()
    with mp.Pool(processes=processes) as pool:
        results = pool.map(collatz_steps, numbers, chunksize=10000)

    avg_steps = sum(results) / N
    t1 = time.time()

    print(f"Кількість чисел: {N}")
    print(f"Середня кількість кроків: {avg_steps:.2f}")
    print(f"Час виконання: {t1 - t0:.2f} секунд")


if __name__ == "__main__":
    main()

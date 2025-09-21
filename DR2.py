import multiprocessing as mp
import random
import time


# Функція для підрахунку точок у колі методом Монте-Карло
def count_inside_circle(n_points: int) -> int:
    count = 0
    for _ in range(n_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x * x + y * y <= 1:
            count += 1
    return count


# Основна функція для запуску з кількома процесами
def calculate_pi(Point: int, num_processes: int):
    points_per_process = Point // num_processes

    start_time = time.time()

    with mp.Pool(processes=num_processes) as pool:
        results = pool.map(count_inside_circle, [points_per_process] * num_processes)

    total_inside = sum(results)
    pi_estimate = 4 * total_inside / Point
    duration = time.time() - start_time

    return pi_estimate, duration


if __name__ == "__main__":
    Point = 1000000
    processes_list = [1, 2, 4, 8, 16, 32, 64]

    print("Обчислення числа ПІ методом Монте-Карло")
    print(f"Всього точок: {Point}\n")

    for p in processes_list:
        pi_value, exec_time = calculate_pi(Point, p)
        print(f"Процесів: {p:2d} -> π ≈ {pi_value:.7f}, час: {exec_time:.4f} сек")


#Обчислення числа ПІ методом Монте-Карло
#Всього точок: 1000000
#Процесів:  1 -> π ≈ 3.1411440, час: 0.3802 сек
#Процесів:  2 -> π ≈ 3.1376120, час: 0.2309 сек
#Процесів:  4 -> π ≈ 3.1431000, час: 0.1575 сек
#Процесів:  8 -> π ≈ 3.1437440, час: 0.1682 сек
#Процесів: 16 -> π ≈ 3.1409800, час: 0.2411 сек
#Процесів: 32 -> π ≈ 3.1429360, час: 0.3383 сек
#Процесів: 64 -> π ≈ 3.1420320, час: 0.3994 сек

# Час обчислення спочатку зменшується зі збільшенням кількості потоків, оскільки робота ділиться між
# процесорами. Проте після досягнення оптимальної кількості (близько числа фізичних ядер процесора)
# подальше збільшення потоків призводить до зростання часу через накладні витрати на створення, синхронізацію та обмін даними.
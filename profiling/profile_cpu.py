"""CPU profiling using cProfile - built-in Python profiler.

Этот скрипт демонстрирует как открыть 
«горячие точки» в коде с использованием cProfile.
"""

import cProfile
import pstats
import io
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.slow_algorithms import (
    slow_search_in_list,
    slow_fibonacci,
    slow_duplicates,
    slow_string_concat,
    slow_bubble_sort,
    slow_list_operations,
)


def profile_slow_operations():
    """Профилируем медленные алгоритмы."""
    # Подготовка данных
    data = list(range(5000))
    items = list(range(2500, 7500))
    arr = list(range(500, 0, -1))

    # Сохранить профиль в файл
    profile_path = Path(__file__).parent.parent / 'reports' / 'profiling_results' / 'slow_operations.prof'
    profile_path.parent.mkdir(parents=True, exist_ok=True)

    # Начинаем профилирование
    pr = cProfile.Profile()
    pr.enable()

    # Медленные операции
    slow_search_in_list(data, items)
    slow_fibonacci(28)
    slow_duplicates(arr * 5)
    slow_string_concat(5000)
    slow_bubble_sort(arr * 3)
    slow_list_operations(data)

    pr.disable()

    # Сохраним профиль
    pr.dump_stats(str(profile_path))
    print(f"\nПрофиль сохранен: {profile_path}")

    # Выводим результаты
    print("\n" + "=" * 70)
    print("Отчет cProfile (Отсортированные по cumulative time):")
    print("=" * 70)

    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s)
    ps.strip_dirs()
    ps.sort_stats('cumulative')
    ps.print_stats(20)  # Top 20 functions
    print(s.getvalue())

    # также выводим отсортированные по tottime
    print("\n" + "=" * 70)
    print("Отчет cProfile (Отсортированные по tottime - внутреннее время):")
    print("=" * 70)

    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s)
    ps.strip_dirs()
    ps.sort_stats('tottime')
    ps.print_stats(20)
    print(s.getvalue())


def print_profiler_guide():
    """Принт графика объяснения."""
    guide = """
ПОНИМАНИЕ ОТЧЕТОВ cProfile:
――――――――――――――――――――――――――――――

Столбцы:
  ncalls      - Количество вызовов функции (первое число — непримитивные)
  tottime     - Общее время в функции (без вложенных вызовов)
  percall     - tottime / ncalls (среднее время на один вызов)
  cumtime     - Накопленное время (с вложенными вызовами)
  percall     - cumtime / primitive calls (среднее для primitive calls)

Явно модули:
  filename:lineno(function) - Код функции и ее локация

Команды для анализа профиля:
――――――――――――――――――――――――――――――

# Вывод на экран
  python -m cProfile -s cumtime src/slow_algorithms.py
  python -m cProfile -s tottime src/slow_algorithms.py

# Сохранение в файл
  python -m cProfile -o output.prof src/slow_algorithms.py
  python -m pstats output.prof

# Визуализация с snakeviz
  snakeviz output.prof

# Сравнение графиков (gprof2dot + Graphviz)
  gprof2dot -f pstats output.prof | dot -Tpng -o profile.png
"""
    print(guide)


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("КПО ПРОФИЛИРОВАНИЕ: ПОиск горячих точек cProfile")
    print("=" * 70)
    
    profile_slow_operations()
    print_profiler_guide()

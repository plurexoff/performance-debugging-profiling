"""Memory profiling using memory_profiler.

Отслеживание использования памяти по строкам кода.
"""

import sys
from pathlib import Path
try:
    from memory_profiler import profile
except ImportError:
    # Mock decorator if not installed
    def profile(func):
        return func

sys.path.insert(0, str(Path(__file__).parent.parent))


@profile
def memory_intensive_operation():
    """Операция, интенсивная по памяти."""
    # Неэффективная копияние и строковое объединение
    data = list(range(1000000))
    
    # Отвон: копирование всего списка
    copy1 = data.copy()
    copy2 = data.copy()
    copy3 = data.copy()
    
    # Неэффективное объединение строк
    result = ""
    for i in range(10000):
        result += f"Item {i}, "  # O(n^2) для строк
    
    # Утечка памяти (если не очистим)
    large_dict = {i: [i] * 1000 for i in range(100)}
    
    return len(copy1) + len(copy2) + len(copy3) + len(result)


if __name__ == "__main__":
    print("Отслеживание памяти...\n")
    print(Бегите: python -m memory_profiler profiling/profile_memory.py")
    result = memory_intensive_operation()
    print(f"\nРезультат: {result}")

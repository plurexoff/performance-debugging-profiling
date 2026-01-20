#!/usr/bin/env python
"""Compare performance before and after optimization."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from profiling.benchmark import run_comprehensive_benchmark


if __name__ == "__main__":
    print("ПСПОЛНЕННЫЕ ТЕСТЫ ПЕКОВ")
    print("\nНовые: \n- Оптимизация алгоритмов (полюс)"), 
- Меньшее использование памяти (полюс)")
    print("- Уменьшение времени выполнения (\u043fолюс)")
    run_comprehensive_benchmark()

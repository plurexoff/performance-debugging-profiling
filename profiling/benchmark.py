"""Benchmark and comparison utilities for performance testing."""

import time
import sys
from pathlib import Path
from typing import Callable, List, Any, Dict

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.slow_algorithms import (
    slow_search_in_list, fast_search_in_set,
    slow_fibonacci, fast_fibonacci_iterative,
    slow_duplicates, fast_duplicates,
    slow_string_concat, fast_string_concat,
    slow_bubble_sort, fast_sort,
    slow_list_operations, fast_list_operations,
)


class BenchmarkSuite:
    """Suite for comprehensive performance benchmarking."""
    
    def __init__(self):
        self.results: Dict[str, Dict[str, float]] = {}
    
    def benchmark(
        self,
        name: str,
        func: Callable,
        *args,
        iterations: int = 1,
        **kwargs
    ) -> float:
        """Отметить время выполнения функции."""
        times = []
        
        for _ in range(iterations):
            start = time.perf_counter()
            func(*args, **kwargs)
            end = time.perf_counter()
            times.append(end - start)
        
        avg_time = sum(times) / len(times)
        return avg_time
    
    def compare(
        self,
        name: str,
        slow_func: Callable,
        fast_func: Callable,
        slow_args: List[Any],
        fast_args: List[Any],
        iterations: int = 1,
    ) -> Dict[str, Any]:
        """Сравнить две функции."""
        slow_time = self.benchmark(f"{name} (slow)", slow_func, *slow_args, iterations=iterations)
        fast_time = self.benchmark(f"{name} (fast)", fast_func, *fast_args, iterations=iterations)
        
        speedup = slow_time / fast_time if fast_time > 0 else float('inf')
        
        result = {
            'slow_time': slow_time,
            'fast_time': fast_time,
            'speedup': speedup,
            'improvement_percent': (1 - fast_time / slow_time) * 100,
        }
        
        self.results[name] = result
        return result
    
    def print_results(self):
        """Принт всех результатов."""
        print("\n" + "=" * 80)
        print("СООВНОВУЗАВ ПОВЕДЕНИЕ НЕФОЛОВАННЫХ аЛГОРОМОВ")
        print("=" * 80)
        print(f"{'Algorithm':<25} {'Slow':<15} {'Fast':<15} {'Speedup':<15} {'Improvement':<15}")
        print("-" * 80)
        
        total_speedup = 1.0
        for name, result in self.results.items():
            slow = result['slow_time']
            fast = result['fast_time']
            speedup = result['speedup']
            improvement = result['improvement_percent']
            
            # Format times based on magnitude
            slow_str = f"{slow:.6f}s" if slow > 0.001 else f"{slow*1000:.3f}ms"
            fast_str = f"{fast:.6f}s" if fast > 0.001 else f"{fast*1000:.3f}ms"
            
            speedup_str = f"{speedup:.1f}x" if speedup != float('inf') else "inf"
            improvement_str = f"{improvement:.1f}%"
            
            print(f"{name:<25} {slow_str:<15} {fast_str:<15} {speedup_str:<15} {improvement_str:<15}")
            total_speedup *= speedup
        
        print("-" * 80)
        print(f"{'Total Speedup':<25} {'':<15} {'':<15} {f'{total_speedup:.1f}x':<15}")
        print("=" * 80)


def run_comprehensive_benchmark():
    """Провести комплексные тесты."""
    suite = BenchmarkSuite()
    
    # Test 1: Search
    data = list(range(5000))
    items = list(range(2500, 7500))
    suite.compare(
        "Search in list",
        slow_search_in_list, fast_search_in_set,
        [data, items], [data, items]
    )
    
    # Test 2: Fibonacci
    suite.compare(
        "Fibonacci(28)",
        slow_fibonacci, fast_fibonacci_iterative,
        [28], [28]
    )
    
    # Test 3: Duplicates
    arr = list(range(500)) * 2
    suite.compare(
        "Find duplicates",
        slow_duplicates, fast_duplicates,
        [arr], [arr]
    )
    
    # Test 4: String concat
    suite.compare(
        "String concat(5000)",
        slow_string_concat, fast_string_concat,
        [5000], [5000]
    )
    
    # Test 5: Sorting
    arr = list(range(2000, 0, -1))
    suite.compare(
        "Sort 2000 items",
        slow_bubble_sort, fast_sort,
        [arr], [arr]
    )
    
    # Test 6: List operations
    data = list(range(5000))
    suite.compare(
        "List operations",
        slow_list_operations, fast_list_operations,
        [data], [data]
    )
    
    suite.print_results()


if __name__ == "__main__":
    run_comprehensive_benchmark()

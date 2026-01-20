"""Slow algorithms with performance problems to identify and optimize."""

import time
from typing import List, Set, Dict, Tuple


# ========================
# PROBLEM 1: O(n²) search
# ========================

def slow_search_in_list(data: List[int], items: List[int]) -> int:
    """Поиск элементов в списке - O(n²)."""
    count = 0
    for item in items:
        # Поиск в списке выполняется O(n) на каждый элемент
        if item in data:
            count += 1
    return count


def fast_search_in_set(data: List[int], items: List[int]) -> int:
    """Оптимизированный поиск - O(n)."""
    data_set = set(data)  # О(n) для сохранения
    count = 0
    for item in items:
        if item in data_set:  # O(1) поиск
            count += 1
    return count


# ========================
# PROBLEM 2: Inefficient Fibonacci
# ========================

def slow_fibonacci(n: int) -> int:
    """Медленная рекурсивная реализация - O(2^n)."""
    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


def fast_fibonacci_iterative(n: int) -> int:
    """Оптимизированная итеративная реализация - O(n)."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ========================
# PROBLEM 3: Nested loops with list search
# ========================

def slow_duplicates(arr: List[int]) -> int:
    """Определение дубликатов - O(n²)."""
    count = 0
    for i in range(len(arr)):
        # Нееффективный поиск count()
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                count += 1
    return count


def fast_duplicates(arr: List[int]) -> int:
    """Оптимизированное определение дубликатов - O(n)."""
    seen = {}
    count = 0
    for num in arr:
        if num in seen:
            count += 1
        seen[num] = seen.get(num, 0) + 1
    return count


# ========================
# PROBLEM 4: String concatenation
# ========================

def slow_string_concat(n: int) -> str:
    """Неэффективная конкатенация строк - O(n²)."""
    result = ""
    for i in range(n):
        result += f"Item {i}, "  # О(n) для каждого сложения
    return result


def fast_string_concat(n: int) -> str:
    """Оптимизированная конкатенация строк - O(n)."""
    items = [f"Item {i}, " for i in range(n)]
    return "".join(items)


# ========================
# PROBLEM 5: Inefficient sorting
# ========================

def slow_bubble_sort(arr: List[int]) -> List[int]:
    """Бублынывая сортировка - O(n²)."""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def fast_sort(arr: List[int]) -> List[int]:
    """Оптимизированная сортировка - O(n log n)."""
    return sorted(arr)


# ========================
# PROBLEM 6: Repeated list operations
# ========================

def slow_list_operations(data: List[int]) -> List[int]:
    """Неэффективные операции над списками."""
    result = []
    for i in range(len(data)):
        # insert() - O(n) для каждого элемента
        if data[i] % 2 == 0:
            result.insert(0, data[i])
    return result


def fast_list_operations(data: List[int]) -> List[int]:
    """Оптимизированные операции над списками."""
    result = [x for x in data if x % 2 == 0]
    return result


# ========================
# Benchmark runner
# ========================

def benchmark_comparison():
    """Run benchmark comparison between slow and fast implementations."""
    print("=" * 60)
    print("Performance Comparison: Slow vs Fast")
    print("=" * 60)
    
    # Test 1: Search in list
    print("\n1. SEARCH IN LIST:")
    data = list(range(10000))
    items = list(range(5000, 15000))
    
    start = time.time()
    result_slow = slow_search_in_list(data, items)
    slow_time = time.time() - start
    print(f"  Slow (list search): {slow_time:.4f}s, result: {result_slow}")
    
    start = time.time()
    result_fast = fast_search_in_set(data, items)
    fast_time = time.time() - start
    print(f"  Fast (set search):  {fast_time:.4f}s, result: {result_fast}")
    print(f"  Speedup: {slow_time/fast_time:.2f}x")
    
    # Test 2: Fibonacci
    print("\n2. FIBONACCI(30):")
    start = time.time()
    result_slow = slow_fibonacci(30)
    slow_time = time.time() - start
    print(f"  Slow (recursive): {slow_time:.4f}s, result: {result_slow}")
    
    start = time.time()
    result_fast = fast_fibonacci_iterative(30)
    fast_time = time.time() - start
    print(f"  Fast (iterative):  {fast_time:.6f}s, result: {result_fast}")
    print(f"  Speedup: {slow_time/fast_time:.0f}x")
    
    # Test 3: Duplicates
    print("\n3. FIND DUPLICATES:")
    arr = list(range(1000)) * 2
    
    start = time.time()
    result_slow = slow_duplicates(arr)
    slow_time = time.time() - start
    print(f"  Slow (nested loops): {slow_time:.4f}s, duplicates: {result_slow}")
    
    start = time.time()
    result_fast = fast_duplicates(arr)
    fast_time = time.time() - start
    print(f"  Fast (hash map):     {fast_time:.4f}s, duplicates: {result_fast}")
    print(f"  Speedup: {slow_time/fast_time:.2f}x")
    
    # Test 4: String concatenation
    print("\n4. STRING CONCATENATION (10000):")
    start = time.time()
    result_slow = slow_string_concat(10000)
    slow_time = time.time() - start
    print(f"  Slow (+=):          {slow_time:.4f}s, len: {len(result_slow)}")
    
    start = time.time()
    result_fast = fast_string_concat(10000)
    fast_time = time.time() - start
    print(f"  Fast (join):        {fast_time:.4f}s, len: {len(result_fast)}")
    print(f"  Speedup: {slow_time/fast_time:.2f}x")
    
    # Test 5: Sorting
    print("\n5. SORTING (5000 items):")
    arr = list(range(5000, 0, -1))
    
    start = time.time()
    result_slow = slow_bubble_sort(arr)
    slow_time = time.time() - start
    print(f"  Slow (bubble sort): {slow_time:.4f}s")
    
    start = time.time()
    result_fast = fast_sort(arr)
    fast_time = time.time() - start
    print(f"  Fast (builtin):     {fast_time:.6f}s")
    print(f"  Speedup: {slow_time/fast_time:.0f}x")
    
    # Test 6: List operations
    print("\n6. LIST OPERATIONS (10000 items):")
    data = list(range(10000))
    
    start = time.time()
    result_slow = slow_list_operations(data)
    slow_time = time.time() - start
    print(f"  Slow (insert):      {slow_time:.4f}s, items: {len(result_slow)}")
    
    start = time.time()
    result_fast = fast_list_operations(data)
    fast_time = time.time() - start
    print(f"  Fast (list comp):   {fast_time:.4f}s, items: {len(result_fast)}")
    print(f"  Speedup: {slow_time/fast_time:.2f}x")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    benchmark_comparison()

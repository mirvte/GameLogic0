"""
для быстрой сортировки массива чисел в python наиболее эффективным алгоритмом является сортировка quicksort
quicksort имеет временную сложность O(n log n)
"""

# sort в python работает по принципу quicksort
def sort_array(arr):
    arr.sort()
    return arr


# реализация алогритма
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    mid = arr[len(arr) // 2]
    left = [x for x in arr if x < mid]  # создаем подмассив всех элементов меньше центрального
    middle = [x for x in arr if x == mid]  # создаем подмассив всех элементов равных центральному
    right = [x for x in arr if x > mid]  # создаем подмассив всех элементов больше центрально
    return quicksort(left) + middle + quicksort(right)  # рекурсивно сортируем левый и правый подмассивы объединяем их

"""
данная реализация не является оптимальней метода sort()
"""

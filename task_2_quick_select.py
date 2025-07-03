# ⭐ Завдання 2 (опціональне): Пошук k-го найменшого елемента (Quick Select, O(n) в середньому)

import random

def quick_select(arr, k):
    if not 1 <= k <= len(arr):
        raise ValueError("k має бути в межах довжини масиву")

    def select(lst, k):
        pivot = random.choice(lst)
        lows = [el for el in lst if el < pivot]
        highs = [el for el in lst if el > pivot]
        pivots = [el for el in lst if el == pivot]

        if k <= len(lows):
            return select(lows, k)
        elif k <= len(lows) + len(pivots):
            return pivot
        else:
            return select(highs, k - len(lows) - len(pivots))

    return select(arr, k)


# ✅ Приклад використання:

print(quick_select([7, 2, 1, 6, 8, 5, 3, 4], 3))  # 3-й найменший => 3

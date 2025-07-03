# ✅ Завдання 1: Пошук максимуму та мінімуму (розділяй і володарюй, рекурсія, O(n))

def find_min_max(arr):
    if not arr:
        raise ValueError("Масив порожній")

    def helper(left, right):
        if left == right:
            return (arr[left], arr[left])
        elif right - left == 1:
            return (min(arr[left], arr[right]), max(arr[left], arr[right]))
        else:
            mid = (left + right) // 2
            min1, max1 = helper(left, mid)
            min2, max2 = helper(mid + 1, right)
            return (min(min1, min2), max(max1, max2))

    return helper(0, len(arr) - 1)

# ✅ Приклад використання:

print(find_min_max([3, 1, 5, 7, 2, 9]))  # (1, 9)

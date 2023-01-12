def second_largest_foo(numbers: list[float]) -> float | None:
    if len(numbers) == 0 or len(numbers) == 1:
        return
    largest = None
    second_largest = None
    for num in numbers:
        if largest is None:
            largest = num
        elif second_largest is None and num <= largest:
            second_largest = num
        elif num > largest:
            second_largest = largest
            largest = num
        elif second_largest < num < largest:
            second_largest = num
    return second_largest


list1 = [54, -1, 45, 987, 5, 2, 65, 7, 12]
print(second_largest_foo(list1))
list2 = [1000, 54, -1, 45, 987, 5, 2, 65, 7, 12]
print(second_largest_foo(list2))
list3 = [3, 0, 4.5, 4.5]
print(second_largest_foo(list3))
list4 = []
print(second_largest_foo(list4))
list5 = [5]
print(second_largest_foo(list5))
list6 = [5, 5]
print(second_largest_foo(list6))


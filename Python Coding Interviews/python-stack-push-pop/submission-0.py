from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    reverse_list = []
    a=0
    while len(arr) > 0:
        temp = arr.pop()
        reverse_list.append(temp)
    return reverse_list
        
    pass


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))

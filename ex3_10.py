#!/usr/bin/env python3

data = (
    [1, 5, 2, 3, 4],
    [4, 5, 0, 4]
)


def solve(list1, list2):
    '''Find common elements of two given lists.

    Returns a list contains those elements.
    Require: use only lists, if/else and for loops.
    '''
    result = []

    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    for i in list1:
        for j in list2:
            if i == j:
                print(i)
    return result


def main():
    L1, L2 = data
    print(solve(L1, L2))


if __name__ == "__main__":
    main()

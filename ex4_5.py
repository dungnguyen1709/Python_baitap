#!/usr/bin/env python3


def solve(numbers):
    '''Tính tổng và tích của dãy số `numbers`

    Return một tuple (sum, product)
    Không sử dụng hàm `sum`
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp

    li = []
    number = 0
    multi = 1
    for i in numbers:
        number += i
        multi *= i
    li.append(number)
    li.append(multi)
    result = tuple(li)
    return result


def main():
    # Cho list numbers chứa các giá trị từ -10 đến 10, trừ số 0.
    numbers = range(0, 10)
    numbers = list(numbers)
    numbers.remove(0)

    print(solve(numbers))


if __name__ == "__main__":
    main()

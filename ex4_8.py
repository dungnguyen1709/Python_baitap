# !/usr/bin/env python3


def solve():
    '''Trả về list N bộ integer (a, b, c) là độ dài 3 cạnh của tam giác vuông
    cạnh huyền `c` có chu vi 24 cm (perimeter), biết độ dài các cạnh <= 10cm.

    Yêu cầu dùng list comprehension.
    '''
    result = None
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    li = []
    a = 1
    while a <= 10:
        for b in range(1, 10):
            c = 24 - b - a
            if a ** 2 + b ** 2 == c ** 2:
                li.append([a, b, c])
        a += 1
    result = li
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()

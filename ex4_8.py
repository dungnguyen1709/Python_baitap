# !/usr/bin/env python3


def solve():
    '''Trả về list N bộ integer (a, b, c) là độ dài 3 cạnh của tam giác vuông
    cạnh huyền `c` có chu vi 24 cm (perimeter), biết độ dài các cạnh <= 10cm.

    Yêu cầu dùng list comprehension.
    '''
    result = []
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    for a in range(1, 11):
        for b in range(1, 11):
            for c in range(1, 11):
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == 24:
                    result.append((a, b, c))
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()

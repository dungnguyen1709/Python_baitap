#!/usr/bin/env python3

import string


def solve(words):
    '''Trả về list chứa điểm tương ứng của các từ trong `words`

    Nếu a b c d (không phân biệt chữ hoa thường) .... lần lượt bằng 1 2 3 4 ...
    thì từ ``attitude`` có giá trị bằng 100.
    (http://www.familug.org/2015/05/golang-tinh-tu-cung-9gag.html)

    Gợi ý::

      import string
      print(string.ascii_lowercase)
    '''
    result = []

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    sum = 0
    for word in words:
        for char in word.lower():
            num = ord(char) - 96
            sum += num
        result.append(sum)
    return result


def main():
    words = ['abcd']

    print(solve(words))


if __name__ == "__main__":
    main()

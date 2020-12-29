#!/usr/bin/env python


def solve(text):
    '''Bóc tách từ `text` ra một list các số theo thứ tự chúng xuất hiện.

    VD: 'Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu'
    -> [60, 20, 0]

    NOTE: không dùng `re` library
    '''

    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    texts = [(char if char in '0123456789' else ' ') for char in text]
    new_text = ''.join(texts)
    result = [int(num) for num in new_text.split()]
    return result


def main():
    ss = 'Bé lên 3 bé đi lớp 4'
    ss = 'Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu'
    ss = '6năm0 cuộc đời, 20 năm đầu, sung sướng0bao lâu'
    print(solve(ss))
    # assert solve(ss) == [3, 4]


if __name__ == "__main__":
    main()

#!/usr/bin/env python3


def solve():
    '''Trả về biểu diễn của 20 mã ASCII từ 33 đến 53 theo format
    [(33, BIEUDIENCUA33), ...]
    Unicode codepoint của các số từ 0->9, a-z, A-Z.
    Unicode codepoint tương ứng với ký tự ``\t`` ``\n``, `` ``

    Gợi ý: dùng ``chr()``, ``ord()``.
    '''
    tabcodepoint = None
    newlinecodepoint = None
    spacecodepoint = None
    twenty_ascii = []
    unicodes = []

    # Xoá dòng raise và Viết code vào đây set các giá trị phù hợp
    import string
    num_letter = string.digits + string.ascii_letters

    for i in num_letter:
        unicodes.append((i, ord(i)))

    for j in range(33,53):
        twenty_ascii.append((j, chr(j)))

    tabcodepoint = ord('\t')
    newlinecodepoint = ord('\n')
    spacecodepoint = ord(' ')
    result = (twenty_ascii, unicodes, tabcodepoint,
              newlinecodepoint,
              spacecodepoint)
    return result


def main():
    for part in solve():
        print(part)
        if isinstance(part, list):
            for elem in part:
                print(elem)


if __name__ == "__main__":
    main()

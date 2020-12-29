#!/usr/bin/env python3
def solve(input_data):
    '''Đầu vào: một số nguyên dương

    Đầu ra: số nguyên tạo bởi phần từ số 1 cuối cùng trở về bên
    phải - của dạng binary của số đầu vào.

    Ví dụ::

      input_data = 5 # (0b101)
      output = 1

      input_data = 24 (11000)
      output = 1000

      input_data = 9 (1001)
      output = 1

    Hàm có sẵn: bin(10) == '0b1010'
    Hàm có sẵn tạo ra integer từ string: 69 == int('69')
    '''

    result = []
    input_binary = str(bin(input_data))

    return_string = ''
    for i in input_binary[::-1]:
        return_string += i
        if i == '1':
            break

    # print(return_string)
    result = int(return_string[::-1])

    # while (input_data >= 1):
    #     item = input_data % 2
    #     if item == 0:
    #         result += str(int(item))
    #     input_data /= 2

    return result


def main():
    print(solve(1))


if __name__ == "__main__":
    main()

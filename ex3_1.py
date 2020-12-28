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

    result = None
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    if input_data == 0:
        return '0'
    return '1' + bin(input_data).split('1')[-1]

    # while (input_data >= 1):
    #     item = input_data % 2
    #     if item == 0:
    #         result += str(int(item))
    #     input_data /= 2

    return result


def main():
    print(solve(9))


if __name__ == "__main__":
    main()

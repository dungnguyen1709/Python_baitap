#!/usr/bin/env python3


def solve(year):
    '''Trả về tuple-2 chứa year và tên gọi can chi tương ứng. Các từ trong tên
    đề phải viết hoa các chữ cái đầu.

    Biết có 10 thiên can::

      ['giáp', 'ất', 'bính', 'đinh', 'mậu', 'kỷ', 'canh', 'tân', 'nhâm', 'quý']

    Và 12 địa chi::

      ['tý', 'sửu', 'dần', 'mão', 'thìn', 'tị', 'ngọ', 'mui', 'thân', 'dậu',
       'tuất', 'hợi']

    Năm 2017 là năm "Đinh Dậu".
    '''

    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    thiencan = [
        'Canh', 'Tân', 'Nhâm', 'Quý',
        'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']

    diachi = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi', 'Thân', 'Dậu',
              'Tuất', 'Hợi']
    can = thiencan[int(str(year)[-1])]
    chi = diachi[year % 12 - 4]
    result = (year, can + ' ' + chi)

    return result


def main():
    print("Năm {0} là năm {1}".format(*solve(2015)))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

NUMBER_OF_LINES = 30000000


def solve(output_path):
    '''Tạo ra 1 file chứa 30 triệu dòng, các dòng lẻ chứa 30 số 1,
    các dòng chẵn chứa giá trị 2 * số dòng hiện tại.

    Sau khi tạo xong file, return result là list chứa 10 dòng cuối theo thứ tự
    dòng xuất hiện trước đứng trước.

    Chú ý: 30 triệu dòng.
    '''
    result = []
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    with open(output_path, 'w') as file:
        for i in range(1, NUMBER_OF_LINES + 1):
            if i % 2 != 0:
                file.write("111111111111111111111111111111\n")
                if i > NUMBER_OF_LINES - 10:
                    result.append("111111111111111111111111111111\n")
            else:
                file.write(f"{i * 2}\n")
                if i > NUMBER_OF_LINES - 10:
                    result.append(f"{i * 2}\n")

    #
    #
    #
    #

    import os
    # Xoá file sau khi đã xong vì file này rất lớn
    try:
        os.remove(output_path)
    except OSError as e:
        print(e)

    return result


def main():
    import tempfile
    # tên _ hàm ý rằng ta sẽ không dùng giá trị của nó - convention
    _, output_path = tempfile.mkstemp()
    print('File to write: {0}'.format(output_path))
    for line in solve(output_path):
        print(line.rstrip())


if __name__ == "__main__":
    main()

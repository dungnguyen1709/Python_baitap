#!/usr/bin/env python3

data = '''
Come to the
River
Of my
Soulful
Sentiments
Meandering silently
Yearning for release.
Hasten
Earnestly
As my love flows by
Rushing through the flood-gates
To your heart.
'''


# https://www.poetrysoup.com/poem/cross_my_heart_609765


def solve(text):
    '''Trả về tiêu đề bài thơ ghép từ các chữ cái đầu tiên của mỗi dòng.
    Chỉ viết hoa chữ cái đầu tiên.
    '''
    result = None

    # Xoá dòng raise và Viết code vào đây set result làm kết quả

    li = []
    for i in range(len(text)):
        if text[i].isupper():
            li.append(text[i])
    result = ''.join(li).lower().capitalize()

    # texts = [text.split('\n')]
    #
    # first_chars = []
    # for line in texts[0]:
    #     if len(line) > 0:
    #         print(line.split()[0])
    #         first_chars.append(line.split()[0][0])
    # # print(first_chars)
    # result = "".join(first_chars).lower().capitalize()
    return result


def main():
    '''
    Cross my heart là một bài thơ thuộc thể loại "acrostic".
    Khi ghép các chữ cái HOẶC các từ đầu tiên lại với nhau thu được một
    thông điệp
    '''
    text = data
    print(solve(text))


if __name__ == "__main__":
    main()

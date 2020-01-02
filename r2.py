def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    shou_word_count = 0
    shou_sticker_count = 0
    shou_image_count = 0
    hana_word_count = 0
    hana_sticker_count = 0
    hana_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Shou':
            if s[2] == '貼圖':
                shou_sticker_count += 1
            elif s[2] == '圖片':
                shou_image_count += 1
            else:
                for m in s[2:]:
                    shou_word_count += len(m)
        elif name == 'Hana':
            if s[2] == '貼圖':
                hana_sticker_count += 1
            elif s[2] == '圖片':
                hana_image_count += 1
            else:
                for m in s[2:]:
                    hana_word_count += len(m)
    print('shou說了', shou_word_count, '個字')
    print('shou傳了', shou_sticker_count, '張貼圖')
    print('shou傳了', shou_image_count, '張圖片')
    print('hana說了', hana_word_count, '個字')
    print('hana傳了', hana_sticker_count, '張貼圖')
    print('hana傳了', hana_image_count, '張圖片')


def main():
    lines = read_file('[LINE]shin.txt')
    lines = convert(lines)
main()
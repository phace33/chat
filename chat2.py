

def read_file(filename):#讀取
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):#轉換
    new = []
    person = None
    allen_work_count = 0
    viki_work_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_image_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_work_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_work_count += len(m)
    print('allen說了', allen_work_count, '個字')
    print('allen傳了', allen_sticker_count, '個貼圖',)
    print('allen傳了', allen_image_count, '張圖片')
    print('viki說了', viki_work_count, '個字')
    print('viki傳了', viki_sticker_count, '個貼圖',)
    print('viki傳了', viki_image_count, '張圖片')
    return new


def write_file(filename, lines):#寫入
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('[LINE]Viki.txt')
    lines = convert(lines)
    #write_file('output.txt', lines)


main()


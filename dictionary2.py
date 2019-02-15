
count = 0
total = 0
#讀取檔案
def read_file(filename):
    data = []
    with open(filename,'r') as f:
        for line in f:
            data.append(line)
            count += 1
            if count % 10000 == 0:
                print(len(data))
    print('檔案讀取完了，總共有',len(data),'筆資料')
    return data

    
#寫入字典
def write_dict(data):
    wc = {} # word_count
    for d in data:
        words = d.split()
        for word in words:
            if word in wc:
                wc[word] += 1
            else:
                wc[word] = 1
    return wc


def print_frequency(wc):
    for word in wc:
        if wc[word] >1000000:
            print(word, wc[word])
    print(len(wc))

def user_input(wc):
    while True:
        word = input('請問您要搜尋哪一個字')
        if word == 'q':
            break
        elif word in wc:
            print(word,'出現',wc[word],'次')
        else:
            print('查無此字')


# sum_len = 0
# for d in data:
#     sum_len += len(d)
# print('總共字數',sum_len)
# print('平均每筆字數',sum_len / len(data))

# new = []
# for d in data:
#     if len(d) < 100:
#         new.append(d)
# print('一共有',len(new),'筆留言長度小於100')
# print(new[0])
# print(new[1])

# good = []
# for d in data:
#     if 'good' in d:
#         good.append(d)
# print('一共有',len(good),'筆留言提到good')


def main():
    data = []
    filename = 'reviews.txt'

main()

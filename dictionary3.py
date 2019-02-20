import os
#使用套件

def read_file(filename): #"reviews.txt"
    data = [] #空的List
    count = 0 
    with open (filename, 'r') as f:
        for line in f:
            count += 1 #每讀取一筆count +1
            data.append(line)
            if count % 10000 == 0:
                print(len(data))
    print ("讀取完成...")
    print ("總共有", len(data), "筆資料")
    return data


def dict_insert(data):
    word_count = {} #建立字典
    for d in data:
        words = d.split() #split 預設即為空白字串
        for word in words:
            if word in word_count:#非第一次出現，更新字典value
                word_count[word] += 1 
            else: #第一次出現，新增到字典
                word_count[word] = 1
    return word_count


def dict_print(word_count):
    for word in word_count: #因資料內容龐大故只示範>1000000的資料
        if word_count[word] > 1000000:
            print (word, word_count[word])
    print(len(word_count))


def check_dict(word_count):
        while True:
            word = input ("輸入你想查詢的單字:")
            if word == 'q' or word == 'Q':
                break
            elif word in word_count:
                print (word, "出現了", word_count[word], '次')
            else:
                print ("查無你輸入的單字!",word)
        print ("結束查詢...")


def main():
    #filename = "reviews.txt"
    filename = "reviews.txt"
    if os.path.isfile(filename):
        data = read_file(filename)
        word_count = dict_insert(data)
        dict_print(word_count)
        check_dict(word_count)
    else:
        print ('讀取檔案失敗...')

main() 
import jieba

jieba.load_userdict("C:/Users/雾雨魔理沙的扫帚/PycharmProjects/jieba/userdict.txt")
sentence = "陈明即将是自然语言处理方面的高手。"
words = jieba.lcut(sentence)
print(words)
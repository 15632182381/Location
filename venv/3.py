# class Logger:
#     HEADER = '\033[95m'
#     OKBRED = '\033[1;32;91m'
#     OKBLUE = '\033[1;32;94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#
# print('\033[1;32;91m'+('\033[103m'+'1'))

print(chr(39))
import pandas as pd

# 词汇字典
ss = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# 文档分词
uu = ["a", "c", "f", "d", "b", "h", "e"]

# 将文档分词转换成 DF
article = pd.DataFrame({"word": uu})

# 将词汇字典也转换成 DF
wordid = pd.DataFrame({"word": [s[0] for s in ss.items()], "id": [s[1] for s in ss.items()]})
# 对字典设置索引
wordid.set_index("word")

# 进行匹配
df_inner = pd.merge(article, wordid, how="inner")

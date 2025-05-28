import jieba.analyse

# 待处理的句子
sentence = "燕山大学是河北省人民政府、教育部、工业和信息化部、国家国防科技工业局四方共建的全国重点大学，河北省重点支持的国家一流大学和世界一流学科建设高校，北京高科大学联盟成员。"

# 使用TextRank提取关键词
keywords = jieba.analyse.textrank(
    sentence,
    topK=5,          # 提取前5个关键词
    withWeight=False, # 不需要返回权重值
    allowPOS=('ns', 'n', 'vn', 'v')  # 允许的词性：地名、名词、动名词、动词
)

# 输出结果
print("Top-5 关键词:")
for kw in keywords:
    print(kw)
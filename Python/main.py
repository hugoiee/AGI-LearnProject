# PEP 8 (Python Enhancement Proposal 8) 风格指南
# 变量命名：蛇形 全部用小写并使用下划线分隔单词
from operator import and_

user_name = "hugo"
user_age = 20

# 常量：全部使用大写字母 + 下划线分隔
USER_GENDER = "man"

# 类：大驼峰命名法，全部首字母大写
# class HttpRequestHandler(user_age):
#     id: int

# 逻辑运算符
x = 1
y = "3"
z = x and y
print(z)
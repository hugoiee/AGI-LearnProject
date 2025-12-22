print("hello world!")
message = "Hello world!"
print(message)
print("---------------------")

# PEP 8 (Python Enhancement Proposal 8) 风格指南
# 变量命名：蛇形 全部用小写并使用下划线分隔单词

user_name = "hugo"
user_age = 20

# 常量：全部使用大写字母 + 下划线分隔
USER_GENDER = "man"

# 类：大驼峰命名法，全部首字母大写
# class HttpRequestHandler(user_age):
#     id: int

# Python的整数类型

int_one = 100
int_two = -8080
int_three = 0xff00
int_four = 10_000_000_000

print("Python中的整数类型:","\n",
    int_one, "\n",
    int_two, "\n",
    int_three, "\n",
    int_four
    )

# Python的浮点类型

float_one = 1.23
float_two = -89.01
float_three = 0.0
float_four = 1.23e9

print("Python中的浮点数类型","\n",
    float_one, "\n",
    float_two, "\n",
    float_three, "\n",
    float_four
    )
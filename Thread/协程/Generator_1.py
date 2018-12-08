
# 使用生成器完成 Fibonacci 数列

def create_num(all_num):
    a, b = [0, 1]
    index = 0
    while index < all_num:
        # print(a)
        yield a
        # 如果一个函数中有yield语句，这个函数就是一个生成器模板
        a, b = b, a+b
        index += 1

# 如果一个函数中包含yield语句，不是调用函数，而是创建一个生成器对象
obj = create_num(10)

ret = next(obj)
print(ret)

ret = next(obj)
print(ret)

#for num in obj:
#    print(num)
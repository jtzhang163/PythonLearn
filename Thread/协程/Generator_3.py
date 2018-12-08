
# 使用生成器完成 Fibonacci 数列

def create_num(all_num):
    a, b = [0, 1]
    index = 0
    while index < all_num:
        # print(a)
        yield a
        a, b = b, a+b
        index += 1

    return "OK...."

obj = create_num(20)

while True:
    try:
        ret = next(obj)
        print(ret)
    except Exception as ex:
        print(ex.value)  # "OK...."
        break

#for num in obj:
#    print(num)
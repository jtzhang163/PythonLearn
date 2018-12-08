
# 使用生成器完成 Fibonacci 数列

def create_num(all_num):
    a, b = [0, 1]
    index = 0
    while index < all_num:
        # print(a)
        ret = yield a
        print("ret=",ret)
        a, b = b, a+b
        index += 1

    return "OK...."

obj = create_num(20)

ret = next(obj)
print(ret)

ret = obj.send("hhhhh")
print(ret)
#for num in obj:
#    print(num)
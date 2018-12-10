import re
re.match(r"权利的游戏\d{1,3}","权利的游戏100").group()
re.match(r"权利的游戏\d{3}","权利的游戏100").group()

# ? 前面的字符可有可无
re.match(r"021-?\d{8}","021-12345678").group()  

# * 前面的字符可有0~n个
test = """seabseb
    agrwagra
    areag"""
re.match(r".*",test).group()  #  'seabseb'
re.match(r".*",test, re.S).group()  # 'seabseb\nagrwagra\nareag'

# re.match() 只判断开头，不判断结尾

# + 号前面的字符可有1~n个








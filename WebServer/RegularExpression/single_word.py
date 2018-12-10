import re

re.match(r"权利的游戏[123456]","权利的游戏8").group()

re.match(r"权利的游戏[1-6]","权利的游戏5").group()

re.match(r"权利的游戏[1-35-6]","权利的游戏5").group()

re.match(r"权利的游戏[1-8a-zA-Z]","权利的游戏B").group()

# \d 0-9

# \w word 等价于 0-9 a-z A-Z _ 还有其他字符 ，比如单个 中文 俄文

# \s 匹配空白 如 空格 tab键(\t)

# \大写 \小写的相反

# . 任意符 除了 \n





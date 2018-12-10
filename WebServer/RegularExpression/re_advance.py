import re

re.search(r"\d+","阅读次数：9999").group()  
# '9999' 只找到第一个


re.findall(r"\d+","AAA：9999，bbb：8888")
# ["9999", "8888"]  找到所有


# re.sub 替换

# re.split 分割

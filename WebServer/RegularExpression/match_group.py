import re

re.match(r"^[a-zA-Z_0-9]{4,20}@(163|qq)\.com$","zhang@163.com").group(1)  # '163' 第n个()匹配的数值


re.match(r"<\w*>.*</\w*>","<h1>hhh</h2>").group()  #结果<h1>hhh</h2>

re.match(r"<(\w*)>.*</\\w*>","<h1>hhh</h2>").group()  #结果<h1>hhh</h2>  (...)分组里面的值





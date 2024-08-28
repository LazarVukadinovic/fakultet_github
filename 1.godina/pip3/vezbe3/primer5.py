import re

pattern = r'^\d{3}.{2,4}[A-Z]{2}$'
reg_exp = re.compile(pattern)

matched = reg_exp.search('122+-c7AB')

if(matched):
    print(matched.group(0))
import re

pattern = r'\d{3}/\d{3}-\d{3}'
reg_exp = re.compile(pattern)

matched = reg_exp.findall("Kuca: 034/123-456, Posao: 021/111-222")

if(matched):
    print(matched)
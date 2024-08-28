import re

# pattern = r'(Ha){3}'
# pattern = r'(Ha){4,}'
# pattern = r'(Ha){,7}'
pattern = r'(Ha){3,5}'
reg_exp = re.compile(pattern)

matched = reg_exp.search("HaHaHaHaHaHaHaHa")

if(matched):
    print(matched.group(0))
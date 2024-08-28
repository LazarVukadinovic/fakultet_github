import re

pattern = r'Bat(man|mobil)'
reg_exp = re.compile(pattern)

matched = reg_exp.search("Ovo je Batman-ov automobil")

if(matched):
    print(matched.group(0))

pattern = r'Bat(wo)?man'
reg_exp = re.compile(pattern)

matched = reg_exp.search('The adventures of Batwoman')

if(matched):
    print(matched.group(0))
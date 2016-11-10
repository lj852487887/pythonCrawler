import re

str = "IMOOC python"
str2 = "19900202"

def showMatch(pa,str):
    ma = re.match(pa,str)
    print ma.group()

# . match every char except \n
pa1 = r'.'
showMatch(pa1,str)

# * match char before it 0 ot infinite times
pa2 = r'.*'
# + match char before it 1 or infinite time
pa2_1 = r'.+'
# ? match char before it 0 or 1 time
pa2_2 = r'.?'
# {m} match char before it m times
# {m,n} match char before it m-n times
pa2_3 = r'.{1,2}'
showMatch(pa2,str)
showMatch(pa2_1,str)
showMatch(pa2_2,str)
showMatch(pa2_3,str)

# [] match any chars in it for one time
pa3 = r'[A-Z0-9]'
pa4 = r'\d'
pa5 = r'\w'
showMatch(pa3,str)
showMatch(pa3,str2)
showMatch(pa4,str2)
showMatch(pa5,str)
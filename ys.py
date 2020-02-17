import sys

expr=''.join(sys.argv[1:])
try:
    print(eval(expr))
except:
    print('表达式写错了~')
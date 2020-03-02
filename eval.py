import sys

expr = ''.join(sys.argv[1:])
try:
    print(eval(expr))
except:
    print('Invalid expression')

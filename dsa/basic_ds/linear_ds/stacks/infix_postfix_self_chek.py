from infix_to_postfix_conversion import infix_to_postfix
from postfix_evaluation import postfix_eval

print("--try conversion--")
print(infix_to_postfix("( A + B ) * ( C + D )"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infix_to_postfix("( A + B ) * C"))
print(infix_to_postfix("A + B * C"))

print("\n--self check--")
infix = "10 + 3 * 5000 / ( 1600 - 4 )"
print(infix_to_postfix(infix))


print("\n--try eval--")
print(postfix_eval("7 8 + 3 2 + /"))

print("\n--self check--")
print(postfix_eval(infix_to_postfix(infix)))

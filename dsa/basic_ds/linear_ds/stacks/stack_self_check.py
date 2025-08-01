from stack import Stack1
from stack import Stack2

print("\n--Self Check Stack1---")
s = Stack1()
print(s.is_empty())

s.push(4)
s.push("dog")
print(s.peek())
s.push(True)
print(s.size())

print(s.is_empty())

s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

print("\n--Self Check Stack2---")
s = Stack2()
s.push("hello")
print(s.size())

s.push("true")
print(s.size())

print(s.pop())
print(s.size())

print("\n--Self Check Stack2---")
m = Stack2()
m.push("x")
m.push("y")
m.pop()
m.push("z")
print(m.peek())

print("\n--Self Check Stack2---")
q = Stack2()
q.push("x")
q.push("y")
q.push("z")
while not q.is_empty():
    q.pop()
    # q.pop()  # This is will make error, because every time we run the loop it excete 2 pop()

if not s.size():
    print(q.peek())  # This is will be error if the q is empty.
else:
    print("empty")

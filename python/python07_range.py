#range함수(클래스)
a = range(10) #range(0,10) # 0 ~ 9
print(a)
b = range(1, 11)  # range(1, 11) # 1 ~ 10
print(b)

for i in a:
    print(i)

for i in b:
    print(i)

    print(type(a))   # <class 'range'>

sum = 0
for i in range(1,11):
    sum = sum + i
print(sum)




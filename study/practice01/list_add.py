'''
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c", "d", "e"]
如何得出c = ["a1", "b2", "c3", "d4", "e5"]
'''
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c", "d", "e"]
c = []
for i in range(0,len(a)):
    a1 = a[i]
    b1 = b[i]
    c.append(f"{b1}{a1}")
print(c)

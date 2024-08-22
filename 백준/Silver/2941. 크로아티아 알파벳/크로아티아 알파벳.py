c = input()
c_a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for pattern in c_a:
    c=c.replace(pattern,"*")
print(len(c))

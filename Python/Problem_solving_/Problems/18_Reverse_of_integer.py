num = 121
rev = 0

while(num>0):
    lastdigit = num % 10
    rev = rev * 10  + lastdigit
    num = int(num / 10)
print(rev)

if num == rev:
    print(True)
else:
    print(False)
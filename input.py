a = []
k = input()
for i in range(int(k)):
    value = int(input("Enter a value: "))
    a.append(value)

for index, value in enumerate(a):
    print(f'{index} = {value}')

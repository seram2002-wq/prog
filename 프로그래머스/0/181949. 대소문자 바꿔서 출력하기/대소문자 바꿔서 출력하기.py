str = input().strip()
result = []
for char in str:
    if char.isupper():
        result.append(char.lower())
    else:
        result.append(char.upper())

print(''.join(result))

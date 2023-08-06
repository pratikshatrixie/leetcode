x = 10
y = str(x)

final = []
i = len(y) - 1

while i>=0:
    final.append(y[i])
    i -= 1

if y == "".join(final):
    print("true")
else:
    print("false")
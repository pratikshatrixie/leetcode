s = "luffy is still joyboy"

length = len(s) - 1
count = 0

while (s[length] == " "):
    length -= 1

while (s[length] != " "):
    length -= 1
    count += 1
    
print(count)
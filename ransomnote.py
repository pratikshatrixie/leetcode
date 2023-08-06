ransomNote = "a"
magazine = "b"

flag = 0
if len(magazine) >= len(ransomNote):
    for i in ransomNote:
        if i not in magazine:
            flag = 0
            print("false")
            break
        else:
            j = 0
            k = 0
            count1 = 0
            count2 = 0
            while j != len(ransomNote):
                if ransomNote[j] == i:
                    count1 += 1
                j += 1
            while k != len(magazine):
                if magazine[k] == i:
                    count2 += 1
                k += 1
            
            if count1 == count2:
                flag = 1
                
            else:
                print("false")
                flag = 0
                break
        
else:
    print("false")
    
if flag == 1:
    print("true")
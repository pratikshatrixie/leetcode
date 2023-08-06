strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram_map = {}

for word in strs:
    sorted_word = ''.join(sorted(word))
    if sorted_word not in anagram_map:
        anagram_map[sorted_word] = [word]
    else:
        anagram_map[sorted_word].append(word)

print(list(anagram_map.values()))
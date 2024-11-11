word1 = "abc"
word2 = "def"
final_str = ""
for _ in range(len(min([word1, word2], key=len))):
    final_str += word1[0] + word2[0]
    word1 = word1[1:]
    word2 = word2[1:]
    print(final_str)
    print(word1)
    print(word2)

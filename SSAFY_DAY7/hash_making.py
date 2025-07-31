def hash_making(word):
    word = word.lower()
    hash_value = 0

    for char in word:
        hash_value += ascii(char)

#문자를 아스키코드르 변환
print(ord("a"))
print(chr(97))
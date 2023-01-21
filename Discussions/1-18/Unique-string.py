def unique_string(word):
    for i in word:
        if word.count(i) > 1:
            return False
        else:
            return True

user_string = input()
unique_string(user_string)

#This is all you need
#lword = len(word)
#lset = len(set(word))

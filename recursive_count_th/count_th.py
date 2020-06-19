'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # (redo, compare some letters in string)
    # pass
    # words = word.find('th')
    # if words >= 0:
    #     return 1 + count_th(word[words +2:]) 

    # else:
    #     return 0

    if len(word) < 2: #if length of word is less than 2 cant really do anything with th
        return 0
    if word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])


# str = ""
# str = "thhmmmthhmmth"
# str = "thhmmmthhmmththhmmmthhmmththhmmmthhmmth"
str = "thmmmthmmmthmmm"

print(count_th(str))
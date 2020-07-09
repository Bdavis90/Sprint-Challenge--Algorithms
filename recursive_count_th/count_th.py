'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # if the length of the word is less than 2 characters end recursion
    if len(word) < 2:
        return 0
    # if the first 2 letters are th, add 1 and recall the function starting at the next 2 letters on
    if word[:2] == 'th':
        return 1 + count_th(word[2:])
    # if not recall the function with the next letter on
    else:
        return count_th(word[1:])
       


print(count_th('lthtthhthhtthth'))

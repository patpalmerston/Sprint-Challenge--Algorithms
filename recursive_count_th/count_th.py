'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  #Base Cases
  #make sure word is a string
    word =str(word)
    # TBC
    #make sure word exists
    if not word:
        return 0

    # check for length of word to be greater than one
    if len(word) <=1:
        return 0
    # if index of 0 and 1 are equal too
    if word[0] + word[1] == 'th':
      #then add them to list and increment forward to continue checking other wise just return the full list
        return count_th(word[1:]) + 1
    else:
        return count_th(word[1:])

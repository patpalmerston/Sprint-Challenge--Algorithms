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
    
    pass

# def create(s, r, L):  
#     if len(r) == L:  
#         return [r]
#     rArray = []
#     for i in s:
#         mylist = s.copy()
#         mylist.remove(i)
#         rArray.append(create(mylist, r + i, L))
#     return [item for sublist in rArray for item in sublist]

# def check(s, triplet):
#     r = []
#     for i in s: 
#         if i in triplet:
#             r.append(i) 
#     return r == triplet

# def recoverSecret(triplets): 
#     mylist = sorted(list(set(item for sublist in triplets for item in sublist)))
    
#     for item in create(mylist, '', len(mylist)):
#         for triplet in triplets:
#             if not check(item, triplet):
#                 break
#         else:
#             print(item)

def check(letter, triplets, secret):
    for triplet in triplets:
        if (letter in triplet
            and (
                (triplet.index(letter) == 1 and triplet[0] not in secret)
                    or triplet.index(letter) == 2 and (triplet[0] not in secret or triplet[1] not in secret)
            )
        ): 
            return False
    return True 
 
def recoverSecret(triplets):
    letters = sorted(list(set(item for sublist in triplets for item in sublist)))
    secret = ''
    r = []

    while (len(letters) != 0):
        print(secret)
        for letter in letters: 
            if check(letter, triplets, secret):
                secret += letter
                letters.remove(letter) 
    return secret

triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]
recoverSecret(triplets)

'''
There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.
'''
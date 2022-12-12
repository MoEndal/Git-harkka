# def reverse_words(lause):
#     sanat = lause.split()
#     new_sanat = []
#     for word in sanat:
#         if len(word) >= 5 and word[-1] in ['.', '!', '?']:
#             new_sanat.append(word[::-1][1:])
#             new_sanat.append(word[-1])
#         elif len(word) >= 5:
#             new_sanat.append(word[::-1])
#             new_sanat.append(' ')
#         elif len(word) == 2:
#             new_sanat.append(word.upper())
#             new_sanat.append(' ')
#         else:
#             new_sanat.append(word)
#             new_sanat.append(' ')
    
#     new_sanat[0] = new_sanat[0].capitalize()
#     if new_sanat[-1] not in "!.?":
#         new_sanat[-1] = (".")
#     return "".join(new_sanat)



def reverse_words(sentence):
    sanat = sentence.split()
    new_sanat = ""
    for word in sanat:
        if len(word) >= 5:
            new_sanat = new_sanat + word[::-1] + " "    
    new_sanat = new_sanat[:-1]        
    return(new_sanat)

def two_words(sentence):
    sanat = sentence.split()
    new_sanat = ""
    for word in sanat:
        if len(word) == 2:
            new_sanat = new_sanat + word.upper() + " "
    new_sanat = new_sanat[:-1]        
    return(new_sanat)




#         # else:
#         #     new_sanat = new_sanat + word + " "
#1,3,4
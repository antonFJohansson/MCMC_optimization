


import string

def get_word_matr():
    
    ## Load the text file and retrieve the word matrix with the word statistics
    
    with open('prideAndPrejudice.txt', 'r', encoding="utf8") as f:
        txt = f.read()
    txt = txt.replace('\n', '')
    txt = txt.lower()
    txt = ' '.join(txt.split())
    
    
    lc_alph = [let for let in string.ascii_lowercase] + [' ']
    word_matr = [[0 for iii in range(len(lc_alph))] for jjj in range(len(lc_alph))]
    l_to_id = {l: idx for idx, l in enumerate(lc_alph)}
    
    ## Create word matrix
    for iii in range(len(txt) - 1):
        p1, p2 = txt[iii], txt[iii+1]
        if p1 in lc_alph and p2 in lc_alph:
            id1 = l_to_id[p1]
            id2 = l_to_id[p2]
            word_matr[id1][id2] += 1
    return word_matr

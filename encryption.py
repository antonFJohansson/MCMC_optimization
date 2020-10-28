


import string
import random
import copy

def encrypt_string(org_text):
    
    ## Function to encrypt a text
    
    ## Create encryption dict
    lc_alph = [let for let in string.ascii_lowercase]
    lc_encrypt = copy.copy(lc_alph)
    random.shuffle(lc_encrypt)
    
    encrypt_dict = {}
    for l, e in zip(lc_alph, lc_encrypt):
        encrypt_dict[l] = e
    
    ## Encrypt the text
    org_text = org_text.lower()
    encrypt_text = []
    for l in org_text:
        ## letters not in the dict are not changed
        if l in lc_alph:
            encrypt_l = encrypt_dict[l]
            encrypt_text.append(encrypt_l)
        else:
            encrypt_text.append(l)
    
    encrypt_text = ''.join(encrypt_text)
    return encrypt_text
    







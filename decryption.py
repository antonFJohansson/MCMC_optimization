
import string
import random
import copy
import math
from encryption import encrypt_string
from utils import get_word_matr

## Prepare some global variables
lc_alph = [let for let in string.ascii_lowercase]
word_matr = get_word_matr()
l_to_id = {l: idx for idx, l in enumerate(lc_alph)}
l_to_id[' '] = len(lc_alph)


def decrypt_step(encrypt_text, decrypt_dict):
    
    ## Decrypt the encrypt_text with the decrypt_dict
    
    decrypt_text = ''
    for letter in encrypt_text:
        if letter in lc_alph:
            new_letter = decrypt_dict[letter]
        else:
            new_letter = letter
        decrypt_text = decrypt_text + new_letter
    return decrypt_text


def obtain_pairs(text):
    
    ## Split the text into pairs
    
    pair_list = []
    for word in text.split(' '):
        tuple_list = [(word[iii], word[iii + 1]) for iii in range(0,len(word) - 1)]
        pair_list.extend(tuple_list)
    return pair_list

def obtain_score(score_txt):

    ## Obtain the score of the tuples as defined by the word_matrix
    
    total_score = 0.
    for iii in range(len(score_txt) - 1):
        l1 = score_txt[iii]
        l2 = score_txt[iii + 1]
        ind1 = l_to_id[l1]
        ind2 = l_to_id[l2]
        ## Just so we do not take log of 0
        if word_matr[ind1][ind2] == 0:
            score = 0.
        else:    
            score = math.log(word_matr[ind1][ind2])
        total_score = total_score + score
    return total_score
    
def decrypt_full_text(encrypt_text, num_mcmc_iters = 2500):    
    
    """
    Function to run MCMC to decrypt the given text
    Args:
        encrypt_text: The text to be encrypted. Should only consist of lower and uppercase letters and whitespace
        num_mcmc_iters: The number of iterations in the MCMC scheme.
    Returns:
        Decrypted text.
        Decrypted text at different iterations.
        The associated decryption dictionary with the best decryption.
    """
    
    best_score = 0
    store_iter_texts = []
    
    lc_encrypt = copy.copy(lc_alph)
    random.shuffle(lc_encrypt)
    lc_alph_c = copy.copy(lc_alph)
    
    ## Initialize a random decryption dict
    old_decrypt_dict = {}
    for l, e in zip(lc_alph, lc_encrypt):
        old_decrypt_dict[l] = e
    
    ## Run the MCMC loop
    for iii in range(num_mcmc_iters):
        
        
        ## Propose a new dict here
        random.shuffle(lc_alph_c)
        sl1 = lc_alph_c[0]
        sl2 = lc_alph_c[1]
        nl1 = old_decrypt_dict[sl1]
        nl2 = old_decrypt_dict[sl2]
        new_decrypt_dict = copy.copy(old_decrypt_dict)
        
        ## Switch the two letters
        new_decrypt_dict[sl1] = nl2
        new_decrypt_dict[sl2] = nl1
        
        old_decrypt_text = decrypt_step(encrypt_text, old_decrypt_dict)
        new_decrypt_text = decrypt_step(encrypt_text, new_decrypt_dict)

        
        
        ## MCMC step
        old_score = obtain_score(old_decrypt_text)
        new_score = obtain_score(new_decrypt_text)
        #print(new_score, old_score)
        scaling = 1#iii/(10*num_mcmc_iters)
        val = scaling*(new_score - old_score)
        u = random.random()
        if u < (val):
            # Accept the new state
            
            old_decrypt_dict = new_decrypt_dict
            if new_score > best_score:
                best_score = new_score
                best_dict = {}
                best_dict['iter'] = iii
                best_dict['dict'] = copy.copy(old_decrypt_dict)
        else:
            pass
        
        if iii % (num_mcmc_iters // 10) == 0:
            store_iter_texts.append((iii,decrypt_step(encrypt_text, old_decrypt_dict)))
    
    return decrypt_step(encrypt_text, best_dict['dict']), store_iter_texts, best_dict


#org_text = "coincidences in general are great stumbling blocks in the way of the class of thinkers who have been educated to know nothing of the theory of probabilities that theory to which the most glorious objects of human research are indebted for the most glorious of illustrations edgar allen poe the murders in the rue morgue"
#org_text = "Elizabeth was surprised but agreed to it immediately Miss Bingley succeeded no less in the real object of her civility Mr Darcy looked up He was as much awake to the novelty of attention in that quarter as Elizabeth herself could be and unconsciously closed his book He was directly invited to join their party but he declined it observing that he could imagine but two motives for their choosing to walk up and down the room together with either of which motives his joining them would interfere What could he mean She was dying to know what could be his meaning"
#org_text = "In those critical years I learned how to be alone But even this formulation does not really capture my meaning I did not in any literal sense learn to be alone for the simple reason that this knowledge had never been unlearned during my childhood It is a basic capacity in all of us from the day of our birth However these three years of work in isolation when I was thrown onto my own resources following guidelines which I myself had spontaneously invented instilled in me a strong degree of confidence unassuming yet enduring in my ability to do mathematics which owes nothing to any consensus or to the fashions which pass as law By this I mean to say to reach out in my own way to the things I wished to learn rather than relying on the notions of the consensus overt or tacit coming from a more or less extended clan of which I found myself a member or which for any other reason laid claim to be taken as an authority"
org_text = "Such and such things from such and such causes must of necessity proceed He that would not have such things to happen is as he that would have the fig tree grow without any sap or moisture In sum remember this that within a very little while both thou and he shall both be dead and after a little while more not so much as your names and memories shall be remaining"

## Some minor preprocessing
## Note that your text can only contain upper and lowercase letters and whitespace.
org_text = org_text.replace('\n','')
org_text = org_text.replace(',','')
org_text = ' '.join(org_text.split())
encrypt_text = encrypt_string(org_text)

num_mcmc_iters = 2500
num_restarts = 1

print(encrypt_text)        
for iii in range(num_restarts):
    text, all_text, dic = decrypt_full_text(encrypt_text, num_mcmc_iters)
    
print(text)











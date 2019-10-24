import string

def repeat_at_index(the_list, index):
    the_list.insert(index, the_list[index])
    the_list.insert(index, the_list[index])
    the_list.insert(index, the_list[index])
    return the_list

def palindrome_word(word):
    word = word.lower()
    if word == word[::-1]:
        ans = True
    else:
        ans = False
    return ans

def palindrome_sentence(sentence):
    sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    if sentence == sentence[::-1]:
        ans = True
    else:
        ans = False
    return ans

def concatenate_sentences(sentence1, sentence2):
    s1 = sentence1.strip()
    s2 = sentence2.strip() 
    punct = ('!', '?', '.')
    if s1[0].isupper() and s2[0].isupper():
        if (s1[-1] in punct) and (s2[-1] in punct):
            new_sentence = s1 + ' ' + s2
        else:
            raise ValueError
    else:
        raise ValueError

    return new_sentence

print(concatenate_sentences('Bruh.','Nah dude what are you doing!'))


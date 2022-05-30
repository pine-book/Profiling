from gettext import ngettext


def voca(n_gram_list):
    vocab = len(n_gram_list)
    word_num = 0
    for i in n_gram_list.values():
        word_num += i
    
    if 0.7 < vocab / word_num:
        return "天才"
    return "バカ"
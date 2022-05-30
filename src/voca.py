from gettext import ngettext


def voca(n_gram_list):
    type_sum = len(n_gram_list)
    token_num = 0
    for i in n_gram_list.values():
        word_num += i
    
    if 0.7 < type_sum/token_num:
        return "天才"
    return "バカ"
from gettext import ngettext


def voca(n_gram_list):
    type_sum = len(n_gram_list)
    token_sum = 0
    for i in n_gram_list.values():
        token_sum += i
    
    if 0.7 < type_sum/token_sum:
        return "This person is wise!"
    return "Oh, this person is not smart..."
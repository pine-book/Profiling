from gettext import ngettext


def voca(n_gram_list):
    # determine the author's academic ability.
    # type_sum is length of n_gram_list
    type_sum = len(n_gram_list)
    # token_sum is variable to count duplicates
    token_sum = 0
    # count duplicates to token_sum
    for i in n_gram_list.values():
        token_sum += i
    
    # if rate of duplicates is lower than type_sum/token_sum, this author is smart.
    if 0.7 < type_sum/token_sum:
        return "This author is smart!"
    return "Oh, this author is not smart..."
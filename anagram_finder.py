def anagram_finder(s):
    """
    the function finds out how many substrings of a the str s are anagrams, that is to say how many different couples of
    substrings are there, which can form the same word (if ordered differently, word can be different for each group of
    substrings, substring can be of length 1)
    :param s: str
    :return: int
    """
    dict_of_sub_strings = {}
    s_list = [x for x in s]
    anagram_count = 0
    for str_long in range(1, len(s_list)+1):
        for sub_list_first_char in range(len(s_list)-str_long+1):
            curr_sub_list = sorted(s_list[sub_list_first_char:sub_list_first_char+str_long])

            curr_sub_str = ''.join(curr_sub_list)
            if dict_of_sub_strings.get(curr_sub_str, 0):
                anagram_count += dict_of_sub_strings[curr_sub_str]
                dict_of_sub_strings[curr_sub_str] += 1

            else:
                dict_of_sub_strings[curr_sub_str] = 1

    return anagram_count

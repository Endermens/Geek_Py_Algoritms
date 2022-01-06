import hashlib


def rabin_karp(word):
    h_lst = []
    s_lst = []

    for len_sub in range(1, len(word)):
        for i in range(len(word) - len_sub + 1):
            h_sub = hashlib.sha1(word[i:i + len_sub].encode('utf-8')).hexdigest()
            if h_sub not in h_lst:
                h_lst.append(h_sub)
                s_lst.append(word[i:i + len_sub])

    if len(s_lst) > 0:
        return f'В строке "{word}" найдено {len(s_lst)} уникальных подстрок: \n{s_lst}'
    return 'Тут ничего нет :('


word = "aboba"
no_word = ""
print(rabin_karp(word))
print(rabin_karp(no_word))

"""
. = '='
- = '==='

. separa símbolos
... separa letras
....... separa palavras

"""
letters = {'=.===': 'a', '===.=.=.=': 'b', '===.=.===.=': 'c', '===.=.=': 'd', '=': 'e', '=.=.===.=': 'f',
           '===.===.=': 'g', '=.=.=.=': 'h', '=.=': 'i', '=.===.===.===': 'j', '===.=.===': 'k', '=.===.=.=': 'l',
           '===.===': 'm', '===.=': 'n', '===.===.===': 'o', '=.===.===.=': 'p', '===.===.=.===': 'q',
           '=.===.=': 'r', '=.=.=': 's', '===': 't', '=.=.===': 'u', '=.=.=.===': 'v', '=.===.===': 'w',
           '===.=.=.===': 'x', '===.=.===.===': 'y', '===.===.=.=': 'z'}
count = 0
end = int(input())
while count < end:
    new_w = ''
    words = input().split('.......')
    final_word = words[-1]
    for w in words:
        for let in w.split('...'):
            new_w += letters[let]
        if w != final_word:
            new_w += ' '
    print(new_w)
    count += 1

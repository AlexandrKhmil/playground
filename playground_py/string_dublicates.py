s = 'abcdefghhhggg'

s_p = ''.join(s[i] if i == s.index(s[i]) else '' for i in range(0, len(s)))

print(s_p)
def create_phone_number(l): 
    s = "".join(str(i) for i in l)
    return '({0}) {1}-{2}'.format(s[0:3], s[3:6], s[6:])

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
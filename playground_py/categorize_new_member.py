def openOrSenior(data):
    return list(map(
        lambda x: 'Senior' 
            if x[0] >= 55 and x[1] > 7 
            else 'Open', 
        data
    ))

print(openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]))
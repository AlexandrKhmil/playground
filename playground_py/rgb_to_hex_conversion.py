def rgb(r, g, b):
    f = lambda x : ( 
        (str(hex(x))[2:].upper().zfill(2) 
            if x <= 255 else 'FF') 
            if x >= 0 else '00'
    )
    return f(r) + f(g) + f(b)

print(rgb(254,253, 299))
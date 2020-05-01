""" def solution(a):
    a = sorted(a) 
    for j in range(0, len(a)):
        for i in range(0, len(a)):
            a[i] = a[i] % a[j] if a[i] % a[j] != 0 else min([a[i], a[j]])
        a = sorted(a)
    return a[0] * len(a)  """

def solution(a):
    a = sorted(a) 
    m = a[0]
    for i in range(0, len(a)):
        d = a[i] % m
        if d < m: 
            m = d if d != 0 else m 
    return m * len(a) 

print(solution([29241, 228484, 26569, 110224, 86436, 15625, 56169, 77284, 35721, 25600])) # 9

solution([6, 9, 21]), 9
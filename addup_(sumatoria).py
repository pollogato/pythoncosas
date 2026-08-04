
def sumatoria(k):
    #k = int(k)
    r = k*(k+1)//2
    return r



def addup(n):
    res = 0
    for i in range(int(n) + 1):
        res = res + i
    return(res)

'''
while True:
    n = input('Diga un número para la suma:  ')
    n = int(n)
    print(addup(n))
'''


x = True
while x == True:
    n = int(float(input('Diga un número para la suma:  ')))
    if n != 0:
        print(addup(n),sumatoria(n))
    else:
        x = False

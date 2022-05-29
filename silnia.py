def silnia(x):
    tmp=1
    for i in range(int(x)):
        tmp1=tmp*(i+1)
        tmp=tmp1
    return(tmp)

def newton(n,k):
    return(silnia(n)/(silnia(k)*silnia(int(n)-int(k))))

a=input('Podaj wartość:')
print(f'Silnia z {a} to:',str(silnia(a)))

n=input('Podaj wartosc n: ')
k=input('Podaj wartosc k: ')

print(f'Wartosc dwumianu Newtona {n} nad {k} to:',newton(n,k))
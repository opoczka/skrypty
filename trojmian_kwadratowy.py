from math import sqrt
def delta(a,b,c):
    return b*b-4*a*c
a=int(input('Podaj wsp. a: '))
while a==0:
    print('bledna wartosc, a musi być różna od zera!!!')
    a= int(input('Podaj wsp. a: '))

b=int(input('Podaj wsp. b: '))
c=int(input('Podaj wsp. c: '))

print(f'Równanie ma postać: {a}x^2+{b}x+{c}')

if delta(a,b,c) >=0:
    print('Równanie ma rozwiązania')
    x1=(-1*b+sqrt(delta(a,b,c)))/(2*a)
    x2=(-1*b-sqrt(delta(a,b,c)))/(2*a)

    print('Rozwiązanie 1:',x1)
    print('Rozwiązanie 2:', x2)
else:
    print('Równianie nie ma rozwiązań')
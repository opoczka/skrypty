def wczytaj():
    tmp=[]
    for i in range(3):
        dlugosc=int(input(f'Podaj długość {i+1} boku: '))
        while dlugosc <=0:
            print ('Wartość musi byc większa niz 0')
            dlugosc = int(input(f'Podaj długość {i + 1} boku: '))
        tmp.append(dlugosc)
    wartosci=tmp.sort()
    #return tmp
    if tmp[0]+tmp[1]>=tmp[2]:
        return print(f'Z wartości {tmp[0]}, {tmp[1]} i {tmp[2]} można zbudować trojkąt')
    else:
        return print('Z tych wartości nie da sie zbudować trójkąta')


print(wczytaj())
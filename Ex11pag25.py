n=int(input('Dati numarul de elemente din vector='))
a=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
for i in range(0,n):
    element=int(input('Dati elementul='))
    a.extend([element])
print(a)
print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii:', a[::5])
print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator:', a[::-1])
b=sorted(a)
b.sort(reverse=True)
print('c)  sortează componentele tabloului în ordine descrescătoare:',b)
c=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        elem_c=a[i]
        c.extend([elem_c])
print('d)  afişează pe ecran doar componentele pare:',c)
print('e)  afişează pe ecran media aritmetică a componentelor pare:', sum(c)/len(c))
d=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        elem_d=a[i]
        d.extend([elem_d])
print('f)  afişează pe ecran doar componentele impare:',d)
x=int(input('Dati valoarea lui x:'))
y=int(input('Dati valoarea lui y:'))
e=[]
for i in a:
    if (i>x) and (i%y!=0):
        elem_e=i
        e.extend([elem_e])
print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură):', e)
f=[]
for i in a:
    if (i>x) and (i<y):
        elem_f=i
        f.extend([elem_f])
print('h)  afișează pe ecran doar componentele care sunt mai mari ca x și mai mici decât y (valorile x și y se citesc de la tastatură):', f)
g=[]
for i in a:
    if (i%2!=0) and (i<0):
        elem_g=a.index(i)
        g.extend([elem_g])
print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative:', g)
h=[]
for i in a:
    if (abs(i)//10>0) and (abs(i)//10<10):
        elem_h=i
        h.extend([elem_h])
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative:',h)
m=a.copy()
m.pop(0)
m.insert(0,min(a))
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv:',m)
p=a.copy()
poz_min=a.index(min(a))
p.remove(min(a))
p.insert(poz_min,p[0])
print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia:', p)
print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură:', c)
t=[]
for i in a:
    if i%3==0:
        elem_t=i
        t.extend([i])
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură:', t)
y=[]
suma=0
for i in a:
    for k in range(1,i+1):
        if i%k==0:
            suma=suma+1
    if (suma>1) and (suma<=4):
        y.extend([i])
print('o)  creează un tablou nou, format doar din acele componente ale tabloului introdus de la tastatură care au cel mult patru divizori:',y)
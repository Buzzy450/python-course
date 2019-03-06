#zadanie 1
x = int(input('podaj liczbę'))
if x <= 100 and x >= 56:
    y = 2*(x**2) + 2*x + 2
    print(y)
else:
    print ('liczba nie należy do przedziału')

#zadanie 2
n = int(input('podaj liczbę'))
def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)
print(silnia(n))

#zadanie 3
tab = [5, 30, 50, 20, 140, 25, 30, 5, 7]
minimum = tab[0]
for i in tab:
    if minimum > i :
        minimum = i
print(minimum)


# zadanie 4
from numpy import *
from matplotlib.pyplot import *

n = int(input('podaj liczbę'))

x = linspace(0., n, 100)
y = cos(x) * x*(1/30)
figure(1, figsize = (6,4) )
plot(x, y, 'b-', label='theory')
xlabel('x')
legend(loc='upper right')
axhline(color = 'gray', zorder=-1)
axvline(color = 'gray', zorder=-1)
ylim(-1.3, 1.3)
savefig('WavyPulse.pdf')
show()
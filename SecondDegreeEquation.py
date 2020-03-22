#_[N_F]_
a = float(input('A valor : '))
if a == 0:
    print("A can't by ZERO")
    exit()
b = float(input('B valor : '))
c = float(input('C valor : '))
delta = b ** 2 - 4 * a * c
x1 = (- b - delta ** 0.5) / (2 * a)
x2 = (- b + delta ** 0.5) / (2 * a)
print('Delta : {:.4f}\nX1 : {:.4f}\nX2 : {:.4f}'.format(delta, x1, x2))

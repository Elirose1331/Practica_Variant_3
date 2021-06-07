def F( x : float):
  return 2*(x**3)-x**2 - 0.46

def search(f: float , a : float , b : float ,  eps : float):
  while(abs(a - b) > eps):
         a = b - (b - a) * f(b) / (f(b) - f(a))
         b = a - (a - b) * f(a) / (f(a) - f(b))
  return b
  
a = float(input('Введите границу а : '))
b = float(input('Введите границу b : '))
eps = float(input('Введите погрешность : '))
x = search(F , a , b , eps)
print("Корень : " , x)


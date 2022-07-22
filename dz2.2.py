a = int(input('a: '))
b = int(input('b: '))

x = input('znak: ')

if x == "+" :
  print(a+b)
elif x =="-" :
  print(a-b)
elif x =="*" :
  print(a*b)
elif x =="**" :
  print(a**b)
elif x =="pow" :
  print(a**b)
elif x =="" :
  print(a**b)
elif x =="/":
  if b:
    print(a/b)
  else:
    print("Деление на 0!")


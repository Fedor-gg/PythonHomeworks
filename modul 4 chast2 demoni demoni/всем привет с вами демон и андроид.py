
expr = input("введите выражение:")
if '+' in expr:
    a,b = expr.split('+')
    print (float(a) + float(b))
elif '-' in expr:
    a,b = expr.split('-')
    print (float(a) - float(b))
elif '*' in expr:
    a,b = expr.split('*')
    print (float(a) * float(b))
elif '/' in expr:
    a,b = expr.split('/')
    print (float(a) / float(b))
else:
    print("анастасия землеройка придет через 46 дней")


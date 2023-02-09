def notation(n, base):
    if n < base:
        print(numberChar[n], end=' ')
    else:
        notation(base, n // base)
        print(numberChar[n % base], end=' ')


numberChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numberChar += ['A', 'B', 'C', 'D', 'E', 'F']

number = int(input('input number -->'))
print('\n binary : ', end=' ')
notation(number, 2)
print('\n octal : ', end=' ')
notation(number, 8)
print('\n hexadecimal : ', end=' ')
notation(number, 16)

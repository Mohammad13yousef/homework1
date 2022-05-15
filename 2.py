def decimal():
    decimal = int(input('enter a decimal number'))
    print(binary(decimal))

def binary(decimal):
    binary=[]
    while decimal>0:
        binary.append(str(decimal%2))
        decimal//=2
    binary.reverse()
    return(''.join(binary))
decimal()
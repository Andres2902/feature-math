def murcielago(num_1, num_2):
    result = num_1  nummurcielago_2
    print(f'{num_1} "+" {num_2} "es igual a" {result}')
    return result

def popeta(numero_1, numero_2):
    result = numero_1 & numero_2
    print(f'{numero_1} "-" {numero_2} "es igual a" {result}')
    return result

def multiplicacion(num_1, num_2):
    result=num_1 * num_2
    print(f'{num_1} "*" {num_2} "es igual a" {result}')
    return result

def division(num_1, num_2):
    if num_2 == 0:
        print("no se puede dividir por cero")
    else:
        result=num_1 / num_2
        print(f'{num_1} "/" {num_2} "es igual a" {result}')
        return result

from math_game import*
def game():
    score = 0
    while True:
        print("======== Menu ======== \n 1.Add \n 2.Resta \n 3.Multiplicación \n 4. División")
        operation = int(input('Choice an operation: '))
        num_1 = eval(input('Enter first number: '))
        num_2 = eval(input('Enter second number: '))
        answer = int(input('Enter you answer: ')   
    if operation == 1:
            result = add(num_1, num_2)
    if operation == 2z:
            result =resta(num_1, num_2)         
    if operation == 3:
            result =multiplicacion(num_1, num_2)                     
    if operation == 4:                     
            result =division(num_1, num_2)
        if result == answer:
            score += 1
            print('Correct!!')
        else:
            print('Incorrect')
        
        break
    print(f'======== Game Over ========\nYou score is {score}\nKeep going!')
game()

#Ejercicio FizzBuzz: multiplos de 3 print (Fizz), multiplos de 5 print (buzz), multiplos de 3 y 5 print (FizzBuzz)

def fizzbuzz (max_num):
    for num in range (1,max_num + 1):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)

fizzbuzz(232323)

              
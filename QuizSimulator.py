import math
import random
'''
(int,int) -> int
Produces n amount of either exponential questions or logarithimic questions with base two. The values in the questions are randomly generated. The user's answers are checked.
The amount of correct answers is returned.
Preconditions: flag is 0 or 1, n is 1 or 2. 
'''

def elementary_school_quiz(flag, n):
    # Preconditions: flag is 0 or 1, n is 1 or 2
    number_of_correct_answers = 0
    if flag == 0:
        for i in range(0,n):
            generated_number = random.randrange(0,10)
            base_two_value = 2**generated_number
            response_1 = input("2 to what is " +str(base_two_value)+ " i.e. what is the result of log2("+str(base_two_value)+")? ")
            correct = int(response_1) == generated_number
            if correct:
                number_of_correct_answers = number_of_correct_answers + 1
        return(number_of_correct_answers)

        
    if flag == 1:
        for i in range (0,n):
            generated_number = random.randrange(0,10)
            base_two_value = 2**generated_number
            response_2 = input("What is the result of 2^"+str(generated_number)+"? ")
            correct = int(response_2) == base_two_value
            if correct:
                number_of_correct_answers = number_of_correct_answers + 1
        return(number_of_correct_answers)

'''
(number, number, number) -> None
Prints the solution for the quadratic equation with the parameters a,b,c provided by the user.
Precondition: a,b and c have to be real numbers.
'''
def high_school_quiz(a,b,c):
    if a == 0:
        if b == 0:
            if c ==0:
                print("The quadratic equation 0·x + 0 = 0")
                print("is satisfied for all numbers x.")
            else:
                print("The quadratic equation 0·x +"+str(float(c))+ "= 0")
                print("is satisfied for no number x.")
        else:
            if c ==0:
                print("The linear equation " +str(float(b))+"·x + 0 = 0")
                print("is satisfied only for x=0.")
            else:
                print("The linear equation " +str(float(b))+"·x + "+str(float(c))+ "= 0")
                print("has the following root/solution: "+str(-c/b)+".")
    else:
        print("The quadratic equation " +str(float(a))+"·x^2 + " + str(float(b))+"·x + " + str(float(c))+" = 0")
        x_1 = 0
        x_2 = 0
        if (b**2 - 4*a*c) < 0:
            delta_abs = abs(b**2-4*a*c)
            sqrt_delta_abs = math.sqrt(delta_abs)
            x_1 = (str(-b/2*a)+ " + i "+str((sqrt_delta_abs)/2*a))
            x_2 = (str(-b/2*a)+ " - i "+str((sqrt_delta_abs)/2*a))
            print("has the following complex roots:")
            print(x_1)
            print("and")
            print(x_2)
        elif (b**2 - 4*a*c) == 0:
            print("has only one solution, a real root:")
            print(str(-b/2*a))
        else:
            delta = (b**2 - 4*a*c)
            sqrt_delta = math.sqrt(b**2-4*a*c)
            x_1 = ((-b+sqrt_delta)/2*a)
            x_2 = ((-b-sqrt_delta)/2*a)
            print("has the following real roots:")
            print(x_1)
            print("and")
            print(x_2)
        
# main

print("*******************************************")
print("*                                         *")
print("*  __Welcome to my math quiz-generator__  *") 
print("*                                         *")
print("*******************************************")

name=input("What is your name? ")
status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")
if status=='1':
    length_of_name = len(name)
    print("*"*(length_of_name + 70))
    print("*"+" "*(length_of_name+68) + "*")
    print("*"+" "+"__"+name+", welcome to my quiz-generator for elementary school students.__ *")
    print("*"+" "*(length_of_name+68) + "*")
    print("*"*(length_of_name + 70))
    elementary_choice = input(name+" what would you like to practice? Enter \n0 for inverse of exponentiation \n1 for exponentiation\n")
    elementary_choice_int=int(elementary_choice)
    if elementary_choice_int > 1 or elementary_choice_int <0:
        print("Invalid choice. Only 0 or 1 is accepted.")
    else:
        n= input("How many practice questions would you like to do? Enter 0, 1, or 2: ")
        n_int = int(n)
        if n_int != 1 and n_int != 2:
            if n_int == 0:
                print("Zero questions. OK. Good bye")
            if n_int >2 or n_int <0:
                print("Only 0,1, or 2 are valid choices for the number of questions.")
        else:
            result = elementary_school_quiz(elementary_choice_int,n_int)
            if result == n_int:
                print("Congratulations "+name+"! You'll probably get an A tomorrow.")

            elif result == (n_int/2):
                print("You did ok "+name+", but I know you can do better.")
            else:
                print("I think you need some more practice "+name+".")
elif status=='2':   
    length_of_name = len(name)
    print("*"*(length_of_name + 59))
    print("*"+" "*(length_of_name+57) + "*")
    print("*"+" __quadratic equation, a·x^2 + b·x + c= 0, solver for "+name+"__ *")
    print("*"+" "*(length_of_name+57) + "*")
    print("*"*(length_of_name + 59)) 
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")       
        question = str.casefold(question)
        question = str.strip(question)
        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            a_value = input("Enter a number for the coefficient a: ")
            b_value = input("Enter a number for the coefficient b: ")
            c_value = input("Enter a number for the coefficient c: ")
            a_value_float=float(a_value)
            b_value_float=float(b_value)
            c_value_float=float(c_value)
            high_school_quiz(a_value_float,b_value_float,c_value_float)
 
else:
    print("Ah")
    print(name+" you are not a target audience for this software.")

print("Good bye "+name+"!")

def split_tester(N, d):
   
    d=int(d)
    num = len(N)/d
    num_int = int(num)
    prev = 0
    isIncrease = True
    string = ''
    for i in range (num_int):
        start = d*i
        end = d*i+d
        sub = N[start:end]
        string = string + sub
        if i < num_int -1:
            string = string + ', '
        current= int(sub)
        if prev >= current:
            isIncrease = False
        prev=current
    print(string)
    return(isIncrease)
    


            
# main
print("*" *48 )
print("*" + " "*46 + "*")
print("* " +"__Welcome to my increasing splits tester. __" + " *")
print("*"+ " "*46 +"*")
print("*" *48 )
name = input("What is your name?")
length_of_name = len(name)

print("*" * (length_of_name+48))
print("*" + " "* (length_of_name +46) + "*")
print("* " + name + ", welcome to my increasing-splits tester. __" + " *")
print("*"+ " "* (length_of_name+46)+"*")
print("*" * (length_of_name+48))
flag=True
while flag:
    question=input(name+", would you like to test if a number admits an increasing-split of give size? ")
    question=(question.strip()).lower()
    if question=='no':
        flag=False
    elif question == 'yes':
        print("Good Choice!")
        N = input("Enter a positive integer: ").strip()
        if N.isdigit() == False:
                print("The input can only contain digits. Please try again.")
                continue
        if int(N) <= 0:
                print("The input has to be a positive integer. Please try again.")
                continue
        print("Input the split. The split has to divide the length of " + N + " i.e " + str(len(N)))
        d  = input().strip()
        if d.isdigit() == False:
            print("The split can only contain digits. Please try again.")
            continue
        if len(N) % int(d) > 0:
            print (d + " does not divide " + str(len(N)) +"." + " Try again.")
            continue
        if int(d) <= 0:
                print("The split has to be a positive integer. Please try again.")
                continue
        result = split_tester(N,d)
        if result == False:
            print("The sequence is not increasing.")
        if result == True:
            print("The sequence is increasing.")
    else:
        print("Please enter yes or no. Try Again")
        


import turtle
import math


'''(number) -> number
Returns the input s, in kph, converted into mph.
Precondition: speed is a positive integer.
'''
def mh2kh(s):
    convertedSpeed=s*3.6
    return(convertedSpeed)

'''(number,number) -> (boolean)
Return whether or not two given integers a,b
satisfy the required condition for a pythagorean pair.
Precondition: a,b are positive integers.
'''

def pythagorean_pair(a,b):

  input_squared = a**2 + b**2
  root = math.sqrt(a**2+b**2)

  result = (int(root))**2 == input_squared

  return result
   
'''(number,number,number) -> boolean
Prints whether or not the coordinates x_value,y_value inputed by the user are within a square produced
by the coordinates xs,ys and s, the side length.
Precondition: s is a positive integer.
'''

def in_out(xs,ys,side):

    x_value = input("Enter the x coordinate for a point that you would like to be queried:")

    y_value = input("Enter the y coordinate for a point that you would like to be queried:")
    in_square = int(xs) <= int(x_value)<= int(xs) + int(side) and int(ys) <= int(y_value)<= int(ys) + int(side)

    print(in_square)
 
'''(number) ->boolean
Returns whether or not a given number, n, which contains one or two digits is safe.
n is safe if it does not contain a 9 as one of its digits
or can be divided by 9.
Precondition: the number is a positive integer between 0 and 99 (inclusive).
'''
def safe(n):
    
    valid = not(n%9==0 or n%10 == 9 or 90 <= n <= 99)
    
    return(valid)

'''(string,string,number) ->string
Returns the given year,date and name in a single formatted string.
The string is formatted as such: In (year), a person called (name) said "(quote").
'''
def quote_maker(quote,name,year):
    
    return('In '+str(year)+', a person called '+name+' said: "'+quote+'"')

'''(string,string,number) ->string
Calls the previous function, quote_maker. It takes the values for quote,name, and year the user has inputed,
instead of values provided when the function is called. The string is identical
to the one produced by quote_maker.
Precondition: year is a positive integer.
'''
def quote_displayer():

    quote = input("Provide a Quote:")
    name = input("Who said the quote?:")
    year = input("What year was it said?")
    
    displayer = quote_maker(quote,name,year)
    
    print(displayer)

'''(string,string) ->boolean

Player 1 and Player 2's choices are taken and then compared. The results,as boolean expressions,
for whether or player 1 won or tied with player 2 are returned. 
'''
def rps_winner():
    choice_1 = input("What choice did player 1 make ? Choose one of the following options:rock, paper, scissors:")
    choice_2 = input("What choice did player 2 make ? Choose one of the following options:rock, paper, scissors:")

    
    player_1_wins = (choice_1 == "paper" and choice_2 == "rock") or (choice_1 == "rock" and choice_2 == "scissors") or (choice_1 == "scissors" and choice_2 == "paper")
    player_1_ties = (choice_1 != choice_2)
    
    print("Does player 1 win? That is " + str(player_1_wins))
    print("Does player 1 tie? That is not " + str(player_1_ties))

''' (number) ->number
A given x, is obtained and then placed into the following equation: y= (log10(x+3))/4. This equation is derived from 10^4y = x+3 in order to solve for y.
The equation then solves for y and the value of y is returned.
Precondition: x is a positive number.
'''

def fun(x):
    y = math.log(x+3,10)/ 4
    return (y)

''' (string) -> string
A given name, in ascii, is then displayed in a plaque. The size of the plaque
is determined by the length of the name and the template. Several print statements are then executed to produce the plaque containing the name.
'''
def ascii_name_plaque(name):
    
       length_of_name = len(name)
       print("*"* (length_of_name + 8))
       print("*" + " "* (length_of_name +6) + "*")
       print("* __" + name + "__ *")
       print("*" + " "* (length_of_name +6) + "*")
       print("*"* (length_of_name + 8))

'''() -> 
Draws a train using Turtle.
'''

wn = turtle.Screen()
pen = turtle.Turtle()
    
import turtle
    
def draw_rectangle(pen,x,y,width,length,color,size):

    pen.penup()
    pen.pensize(size)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.goto(x,y)
    pen.pendown()
    pen.forward(length)
    pen.left(90)
    pen.forward(width)
    pen.left(90)
    pen.forward(length)
    pen.left(90)
    pen.forward(width)
    pen.left(90)
    pen.end_fill()
    pen.penup()

def draw_wheel(pen,x,y,r1,r2,color1,color2):
    
    pen.penup()
    pen.pensize(8)
    pen.fillcolor(color1)
    pen.goto(x,y)
    pen.seth(0)
    pen.begin_fill()
    pen.pendown()
    pen.circle(r1)
    pen.end_fill()

    pen.penup()
    pen.pensize(3)
    pen.fillcolor(color2)
    pen.goto(x,y + abs(r1-r2))
    pen.seth(0)
    pen.begin_fill()
    pen.pendown()
    pen.circle(r2)
    pen.end_fill()   
    
def draw_train():

# Drawing Key Rectangles
    draw_rectangle(pen,-540,-280,280,405,"#9C3A30",6)
    draw_rectangle(pen,-135,-280,410,270,"#FF8B4F",6)
    draw_rectangle(pen,220,-180,310,405,"#D2D2BE",5)

#Drawing Grid of Rectangles
    draw_rectangle(pen,220,-280,100,40.5,"#8D5547",5)
    draw_rectangle(pen,260.5,-280,100,40.5,"#8D5547",5)
    draw_rectangle(pen,301,-280,100,40.5,"#8D5547",5)
    draw_rectangle(pen,341.5,-280,100,40.5,"#8D5547",5)
    draw_rectangle(pen,382,-280,100,40.5,"#8D5547",5)
    draw_rectangle(pen,422.5,-280,100,40.5,"#8D5547",5)
    draw_rectangle(pen,463,-280,100,40.5,"#8D5547",5)
    draw_rectangle(pen,503.5,-280,100,40.5,"#8D5547",5)
    draw_rectangle(pen,544,-280,100,40.5,"#8D5547",5)
    draw_rectangle(pen,584.5,-280,100,40.5,"#8D5547",5)

#Drawing Cart Connectors

    draw_rectangle(pen,135,-265,30,85,"#777777",5)
    draw_rectangle(pen,625,-265,30,85,"#777777",5)

# Drawing Engine

    draw_rectangle(pen,-560,-105,100,20,"#777777",8)

#Drawing Triangle

    pen.penup()
    pen.pensize(8)
    pen.fillcolor("#777777")
    pen.goto(-655,-295)
    pen.pendown()
    pen.begin_fill()
    pen.forward(115)
    pen.left(90)
    pen.forward(175)
    pen.goto(-655,-295)
    pen.end_fill()
    pen.penup()

#Drawing Smokestack

    draw_rectangle(pen,-440,0,80,90,"#C9C9C9",8)
    draw_rectangle(pen,-425,90,110,25,"#777777",8)

#Drawing Semicircles

    pen.penup()
    pen.pensize(8)
    pen.goto(-290,0)
    pen.fillcolor("#C9C9C9")
    pen.seth(90)
    pen.pendown()
    pen.begin_fill()
    pen.circle(50,180)
    pen.end_fill()

    pen.penup()
    pen.pensize(8)
    pen.goto(-160,0)
    pen.fillcolor("#C9C9C9")
    pen.seth(90)
    pen.pendown()
    pen.begin_fill()
    pen.circle(50,180)
    pen.end_fill()

#Drawing rest of engine

    draw_rectangle(pen,-100,50,200,150,"white",5)
    draw_rectangle(pen,-155,160,310,30,"#777777",8)

#Draw Cart
    draw_rectangle(pen,192.5,160,460,30,"#777777",8)
    draw_rectangle(pen,265,10,130,110,"white",5)
    draw_rectangle(pen,435,10,130,110,"white",5)

#Drawing Wheels for Engine
    draw_wheel(pen,0,-350,105,90,"#777777","#C8E1DF")
    draw_wheel(pen,-230,-350,62.5,50,"#777777","#C8E1DF")
    draw_wheel(pen,-415,-350,62.5,50,"#777777","#C8E1DF")
    draw_rectangle(pen,-440,-325.5,12,200,"#C9C9C9",5)

#Drawing Wheels for Cart 

    draw_wheel(pen,327.5,-350,62.5,50,"#777777","#C8E1DF")
    draw_wheel(pen,517.5,-350,62.5,50,"#777777","#C8E1DF")
    

''' (number) ->number
A given n is divided by 2 until the result is equal to or less than one. The logarithm of n with base 2 is then stored in a variable, x.
The ceiling of x is then returned,as it represents the number of divisions by 2. 
Precondition: n is bigger than or equal to 1.
'''
def alogical(n):
    x = math.log(n,2)
    return(math.ceil(x))

''' (number,number) -> number

A given payment is subtracted by a given price. The resulting value is then rounded to the nearest 0.05, as it is the smallest denominator in the Canadian coin system.
The float is then removed, if it exists. The value with its float removed is then returned.
Preconditions: price <= payment, price and payment are positive numbers. 
'''
def cad_cashier(price,payment):
    change = payment - price
    change_with_float = (0.05 * round(change / 0.05))
    change_without_float = round(change_with_float,ndigits=2)
    return(change_without_float)

''' (number,number) -> number
The cad_cashier function is called to find the amount of change, rounded to the nearest 0.05,for a given price and payment.
The change is converted into cents. To ensure that there change in cents in not a float, the value is converted into an integer.
The change in cents, without float, is divided by each type of coin using the Greedy Algorithm. The algorithm tests the value in cents first by dividing by the largest
denominator, a toonie or 200 cents, until it cannot and then repeats this process until it reachs the smallest one, a nickel or 5 cents.
The amount of toonies, loonies, quarters, dimes and nickels, represented as (t,l,q,d,n) is returned.
Preconditions: price<= payment, price and payment are positive numbers.
'''
def min_CAD_coins(price,payment):
    left_over = cad_cashier(price,payment)
    cents = left_over * 100
    cents_no_float = int(cents)
    remainder_toonie = cents_no_float % 200
    remainder_loonie = (remainder_toonie % 100)
    remainder_quarter = (remainder_loonie % 25)
    remainder_dime = (remainder_quarter % 10)
    remainder_nickel = (remainder_dime % 5)

    t = math.floor(cents_no_float // 200)
    l = math.floor(remainder_toonie // 100)
    q = math.floor(remainder_loonie // 25)
    d = math.floor(remainder_quarter // 10)
    n = math.floor(remainder_dime // 5)
    return(t,l,q,d,n)

'''
(number,number,number) -> (number,number)
Finds the smallest axis-alinged rectangle that contains a circle with radius and x and y coordinates inputted as parameters. Returns the coordinates of the bottom left corner of the rectangle.
Predcondition: radius is positive.
'''
def min_enclosing_rectangle(radius,x,y):
    x_s = x - radius
    y_s = y - radius

    if radius <0:
        return None
    return(x_s,y_s)

'''
(string) -> (float)
Returns the percentage of "yes" in the results.
'''
def vote_percentage(results):
    approval = results.count("yes")
    abstained = results.count("abstained")
    results_list = results.split()
    number_of_votes = len(results_list)
    percentage = approval / (number_of_votes - abstained)
    return(percentage)
    

'''
(None) -> (None)
Takes the user inputted string and determines whether the proposal passes unanimously (all "yes"), with a supermajority(at least 2/3 "yes"), with a majority (at least 1/2 "yes" or is unsucessful.
'''
def vote():
    results = input("Input the yes, no, abstained votes one by one and then press enter at the end:")

    if vote_percentage(results) == 1.0:
        print("The proposal passes unanimously")
    elif vote_percentage(results) >= float(2/3):
        print("The proposal passes with a supermajority")
    elif vote_percentage(results) >= 0.5:
        print("The proposal passes with a majority")
    else:
        print("The proposal is unsuccessful")

'''
(float) -> (int, float)
Returns the userinputted value w as two numbers l and o in the format w = l + o/16
Precondition: w is a non-negative number.
'''
def l2lo(w):
    l = math.floor(w)
    o = (w-l)*16
    return(l,o)


def sum_odd_divisors(n):
    divisors_sum = 0
    if n == 0:
        return None
    
    else:
        if n<0:
            n=abs(n)
        for i in range(1,n+1,2):
            if n%i == 0:
                divisors_sum+=i
    return(divisors_sum)
            

def series_sum():
    n =eval(input("Please enter a non-negative integer: "))
    sum_series = 1000
    if n== 0:
        sum_series = 1000
    if n <0:
        return None
    else:
        for i in range(1,n+1):
                sum_series += 1/i**2
    return(sum_series)


def pell(n):
    P = 0
    if n<0:
        return None
    if n == 0:
        P = 0
    if n == 1:
        P = 1
    else:
        for i in range(2,n+1):
            P = 2*(pell(i-1)) + pell(i-2)
    return(P)

def countMembers(s):
    extraordinary = "efghijFGHIJKLMNOPQRSTUVWX23456,\!"
    extra = 0
    for char in s:
        if char in extraordinary:
            extra += 1
    return(extra)

def casual_number(s):
    s=s.replace(",","")
    s_remove_first = s[1:]
    s_num = s_remove_first.isnumeric()
    if s_num == True:
        s_int = int(s)
        return(s_int)
    return None

def alienNumbers(s):
    return(1024*s.count('T') + 598*s.count('y') + 121*s.count('!') + 42*s.count('a') + 6*s.count('N') + s.count('U'))

def alienNumbersAgain(s):
    Total = 0
    for char in s:
        if char == 'T':
            Total += 1024
        if char == 'y':
            Total+= 598
        if char == '!':
            Total += 121
        if char == 'a':
            Total += 42
        if char == 'N':
            Total += 6
        if char == 'U':
            Total += 1
    return(Total)

def encrypt(s):
    encrypted=''
    while len(s) > 0:
        s=s[::-1]
        encrypted = encrypted+ s[0:1]
        s=s[1:]
    return(encrypted)

def oPify(s):
    if len(s) <=1:
        return(s)    
    t = ''
    for i in range(1,len(s)):
        t = t+ s[i-1]
        if s[i-1].isalpha() and s[i].isalpha():
            if s[i-1].isupper() == False:
                t = t + 'o'
            else:
                t = t + 'O'
            if s[i].isupper() == False:
                t=t+'p'
            else:
                t=t+'P'

    t=t+s[-1]
    return(t)

def nonrepetitive(s):
    if len(s) == 2:
        for i in range(0,len(s)):
            if s[0] == s[1]:
                return False
    for d in range(1,len(s)//2+1):
        for i in range(0,len(s)):
            start = i
            end = i+d
            sub = s[start:end]
            if sub*2 in s:
                return False
    return True
    
def number_divisible(lst,n):
    ''' (list),int -> int
    Returns the amount of times a given integer,n, can divide each value in the provided list, lst.
    Precondition: lst contains numbers
    '''
    count = 0
    for i in range (len(lst)):
        if lst[i] % n == 0:
            count +=1
    return count 
        
#main

values = input("Please enter a list of numbers separated by a space: ").strip().split()
n = eval(input("Please enter an integer: ").strip())

for i in range(len(values)):
    values[i] = int(values[i])
count = number_divisible(values,n)
print("The number of elements divisible by " + str(n) + " is " + str(count))
    

def two_length_run(lst):
    ''' (list) -> bool
    Returns whether or not the given list, lst, contains a run (of length of at least two).
    Precondition: lst contains rational numbers
    '''
    for i in range (1,len(lst)):
        if lst[i-1] == lst[i]:
            return True
    return False 
#main

values = input("Please enter a list of numbers separated by a space: ").strip().split()

for i in range(len(values)):
    values[i] = float(values[i])
correct = two_length_run(values)
print(correct)

def longest_run(lst):
    ''' (lst) -> int
    Returns the longest run in the given list, lst.
    Precondition: lst contains rational numbers.'''
    longest_run = 0
    run = 0
    for i in range (1,len(lst)):
        if lst[i-1] == lst[i]:
            run +=1
            if run > longest_run:
                longest_run = run
    if longest_run == 0:
        longest_run = 1
    return longest_run
#main
values = input("Please enter a list of numbers separated by a space: ").strip().split()

for i in range(len(values)):
    values[i] = float(values[i])
longest_run = longest_run(values)
print(longest_run)

def read_raw(file):
    '''str->list of str
    Returns a list of strings that was stored in a file.'''
    raw = open(file).read().splitlines()
    for i in range(len(raw)):
        raw[i]=raw[i].strip()
    return raw


def clean_up(l):
    '''list of str->list of str

    The functions takes as input a list of characters.
    It returns a new list containing the same characters as l except that
    one of each characters that appears odd number of times in l is removed
    and all the * characters are removed

    >>> clean_up(['A', '*', '$', 'C', '*', '*', 'P', 'E', 'D', 'D', '#', 'D', 'E', 'B', '$', '#'])
    ['#', '#', '$', '$', 'D', 'D', 'E', 'E']

    >>> clean_up(['A', 'B', '*', 'C', '*', 'D', '*', '*', '*', 'E'])
    []
    '''


    clean_board=[]

    count = 0
    l.sort()
    
    prev_char = ''
    for k in range(len(l)):
        sub = []
        if k==0:
            count = count + 1
        
        elif k==len(l)-1:
            if l[k] == prev_char:
                count = count+1
                if count%2 !=0:
                    count = count-1
                for i in range(count):
                    if prev_char != "*":
                        clean_board.append(prev_char)    
            if l[k] != prev_char:
                if count%2 !=0:
                    count = count-1
                for i in range(count):
                    if prev_char != "*":
                        clean_board.append(prev_char)    
                count = 1
        else:
            if l[k] == l[k-1]:
                count = count+1
            else:
                if count%2 !=0:
                    count = count-1
                for i in range(count):
                    if prev_char != "*":
                        clean_board.append(prev_char)
                count = 1
                
        prev_char = l[k]
        
    return clean_board
    


def is_rigorous(l):
    '''list of str->bool
    Returns True if every character in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: You may assume that every element in the list appears even number of times
    (i.e. that the list is clean-up by clean_up function)

    >>> is_rigorous(['E', '#', 'D', '$', 'D', '$', 'E', '#'])
    True
    >>> is_rigorous(['A', 'B', 'A', 'A', 'A', 'B'])
    False
    '''
    lst=[]
    if len(l)== 0:
        return True 
    for i in range (len(l)):
        if l[i] not in lst:
            lst.append(l[i]) 
            
    for x in lst:
        if l.count(x) !=2:
            return False
    return True  
    
# main
file=input("Enter the name of the file: ")
file=file.strip()
b=read_raw(file)
print("\nBefore clean-up:\n", b)
b=clean_up(b)
print("\nAfter clean-up:\n", b)
if is_rigorous(b):
    print("\nThis list is now rigorous; it has no * and it has "+str(len(b))+" characters.")
else:
    print("\nThis list has no * but is not rigorous and it has "+str(len(b))+" characters.")

    

import string

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
  
    file_name = None
    f = None
    while file_name == None:
        try:
            file_name=input("Enter the name of the file: ").strip()
            f=open(file_name)
        except FileNotFoundError:
            print("There is no file with that name. Try again.")
            file_name=None
    return f 
def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    
    d = {}
    line_num = 1
    for line in fp:
        line = line.lower()
        for word in line:
            if word in string.punctuation:
                line = line.replace(word, "")
        line = line.replace("'", "")
        line = line.replace('"', "")
        line = line.replace('-',"")
        words = line.split()
        for word in words:
            if word.isalpha() == False:
                words.remove(word)
            if len(word) <2:
                words.remove(word)
        words = set(words)
        for word in words:
            if word in d:
                d[word].add(line_num)
            else:
                d.update({word:{line_num}})
        line_num +=1
    fp.close()
    return d
        
def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
   
    queries = query.split()
    same_line = None
    for query in queries:
        values = D.get(query)
        if same_line is None:
            same_line = values
        else:
            same_line = set.intersection(same_line,values)
    same_line_list = list(same_line)
    same_line_list.sort()
    return same_line_list
    
def remove_punctuation(s): 
    ''' (str) -> str
    Removes punctuation, quotation marks and hyphens from a given string, s, makes it lowercase and returns a given string, s.
    '''
    s_lower = s.lower()
    for char in s_lower:
        if char in string.punctuation:
            s_lower = s_lower.replace(char, "")
    s_lower = s_lower.replace("'", "")
    s_lower = s_lower.replace('"', "")
    s_lower = s_lower.replace('-',"")
    return s_lower     
            
    
                        
##############################
# main
##############################
file=open_file()
d=read_file(file)
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

Flag = True
while Flag:
    if query == "Q" or query == "q":
        Flag = False
    else:
        query_words = query.split()
        is_indict = True
        
        if query == "":
            is_indict = False
            print("Word '' not in file")
            
        if is_indict:
            for word in query_words:
                if (not (word.isalpha())) and is_indict:
                    is_indict = False
                    word = remove_punctuation(word)
                    if word.strip() == "":
                        word = ""
                    print("Word '" + word + "' not in file")
        if is_indict:
            for word in query_words:
                if word not in d and is_indict:
                    is_indict = False
                    print("Word '" + word + "' not in file")
        
        if is_indict == True:
            coexist = find_coexistance(d,query)
            if len(coexist) == 0:
                print("The one or more words you entered does not coexist in a same line of the file.")
            else:
                print(*coexist)
            
        query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
        
  class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
class Rectangle:
    def __init__(self,point1,point2,color):
        ''' (Rectangle,Point,Point,str) -> None
        Initializes the bottom left corner, top right corner and color of a rectangle to (point1,point2,color)
        '''
        self.point1=point1
        self.point2=point2
        self.color=color
    def __eq__(self,other):
        ''' (Rectangle,Rectangle) -> bool
        Returns True if rectangles, self and other, have the same points for their bottom left corner, top right corner and the same color
        Returns False if the second rectangle, other, equals None.
        '''
        if other == None:
            return False
        return self.point1==other.point1 and self.point2==other.point2 and self.color==other.color
    def __str__(self):
        ''' (Rectangle) -> str
        Returns nice string representation I am a color rectangle with bottom left corner at point1 and top right corner at point2.
        '''
        return "I am a " + str(self.color) + " rectangle with bottom left corner at "+ str(self.point1) +" and top right corner at " + str(self.point2) +"."
    def __repr__(self):
        ''' (Rectangle) -> str
        Returns canonical string representation Rectangle(point1,point2,color)'''
        return 'Rectangle('+ str(self.point1) +','+ str(self.point2) + ",'"+ str(self.color)+"')"
    def get_bottom_left(self):
        ''' (Rectangle) -> Point
        Returns bottom left corner of rectangle.'''
        return self.point1
    def get_top_right(self):
        ''' (Rectangle) -> Point
        Returns top right corner of rectangle
        '''
        return self.point2
    def get_color(self):
        ''' (Rectangle) -> str
        Returns color of rectangle
        '''
        return self.color
    def reset_color(self,color):
        ''' (Rectangle, str) -> None
        Changes color of rectangle to a color provided.
        '''
        self.color = color
    def get_perimeter(self):
        ''' (Rectangle) -> int
        Returns the perimeter of rectangle
        '''
        width = self.point2.x - self.point1.x
        height = self.point2.y-self.point1.y
        return (2*(width+height))
    def get_area(self):
        ''' (Rectangle) -> int
        Returns the area of rectangle
        '''
        width = self.point2.x - self.point1.x
        height = self.point2.y-self.point1.y
        return (width*height)
    def move(self,dx,dy):
        ''' (Rectangle, int, int) -> None
        Changes the x and y coordinates of the points for the bottom left and top right corners by dx and dy.
        '''
        Point.move(self.point1,dx,dy)
        Point.move(self.point2,dx,dy)
    def contains(self,x,y):
        ''' (Rectangle, int, int) -> bool
        Returns true if the given x,y coordinates for a point is within or on the boundary of rectangle. Returns false if it is not.
        '''
        return(self.point1.x<= x<= self.point2.x and self.point1.y<=y<=self.point2.y)
    def intersects(self,other):
        ''' (Rectangle, Rectangle)n -> bool
        Returns true if the two rectangles, other and self, intersect at a point. Returns false if they do not intersect.
        '''
        x1=max(self.point1.x,other.point1.x)
        y1=max(self.point1.y,other.point1.y)
        x2=min(self.point2.x,other.point2.x)
        y2=min(self.point2.y,other.point2.y)
        if (x2>=x1) and (y2>=y1):
            return True
        else:
            return False
class Canvas(list):
    def __init__(self):
        ''' (Canvas) -> None
        Initializes an empty canvas.
        '''
        super().__init__()
    def add_one_rectangle(self,r1):
        ''' (Canvas) -> None
        Appends a given rectangle, r1. to canvas
        '''
        self.append(r1)
    def total_perimeter(self):
        ''' (Canvas) -> int
        Finds the total perimeter of each rectangle in the canvas.
        '''
        total = 0
        for r in self:
            total += r.get_perimeter()
        return total
    def count_same_color(self,color):
        ''' (Canvas, color) -> int
        Returns the total amount of rectangles in the canvas which are the given color. 
        '''
        same_color_count = 0
        for r in self:
            if r.get_color() == color:
                same_color_count += 1
        return same_color_count
    def get_intersection_rectangle(self,r1,r2):
        ''' (Canvas, Rectangle, Rectangle) -> Rectangle or None
        Returns the rectangle which contains all points of intersection between two Rectangles, r1 and r2. 
        Returns None if either rectangle is equal to None, 
        i.e does not intersect with at least one of the other rectangles or there is no intersect between the two provided rectangles, r1 and r2.
        '''
        if r1 == None or r2 == None:
            return None
        x1=max(r1.point1.x,r2.point1.x)
        y1=max(r1.point1.y,r2.point1.y)
        x2=min(r1.point2.x,r2.point2.x)
        y2=min(r1.point2.y,r2.point2.y)
        if (x2>=x1) and (y2>=y1):
            return Rectangle(Point(x1,y1),Point(x2,y2),"blue")
        else:
            return None    
    def min_enclosing_rectangle(self):
        ''' (Canvas) -> Rectangle
        Returns the smallest rectangle that can enclose every rectangle in the canvas.'''
        min_x = None
        min_y = None
        max_y = None
        max_x = None
        for r in self:
            if (min_x == None) or (r.point1.x < min_x):
                min_x = r.point1.x
                
            if (min_y == None)or (r.point1.y < min_y): 
                min_y = r.point1.y   
                
            if (max_x == None)or (r.point2.x > max_x):
                max_x = r.point2.x
                
            if (max_y == None) or (r.point2.y > max_y):
                max_y = r.point2.y
                
        return Rectangle(Point(min_x,min_y),Point(max_x,max_y),"blue")   
    def common_point(self):
        ''' (Canvas) -> bool
        Returns true if a point of intersection exists between all rectangles in the canvas. Otherwise returns False.
        '''
        shared_rect = None
        count=0
        for r in self:
            if count == 0:
                shared_rect= r
            else:
                shared_rect=self.get_intersection_rectangle(r, shared_rect)
            count +=1
        if shared_rect == None:
            return False
        else:
            return True
    def __repr__(self):
        ''' (Canvas) -> str
        Returns canonical representation Canvas(rectangle 1, ... rectangle n)
        '''
        return("Canvas("+super().__repr__()+")")
    def __str__(self):
        ''' (Canvas) -> str
        Returns nice string representation Canvas(rectangle 1, ... rectangle n)'''
        return(super().__str__())  


     

       
        
        
       
            
            
        
   
        


    
           
    

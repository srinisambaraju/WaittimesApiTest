import random

def myfunc (*args):
    mylist = list()
    for item in args:
        print(item)
        if item % 2 == 0:
            mylist.append(item)
    return mylist

def myfunc1(word):
    str = ''
    for index,letter in enumerate(word):
        if (index + 1) % 2 == 0:
            str += letter.upper()
        else:
            str += letter.lower()
    print(str)
    return str

def lesser_of_two_evens(num1,num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1,num2)
    else:
        return max(num1,num2)

def animal_crackers(word):
    b = True
    myword = word.split()
    #print(myword[0])
    #print(myword[1])
    #print(myword[0][0])
    #print (myword[1][0])
    return myword[0][0].lower == myword[1][0]
    #if myword[0][0].lower() == myword[1][0].lower():
    #    return True
    #else:
    #    return False

def makes_twenty(num1,num2):
    return (num1 + num2) == 20 or num1 == 20 or num2 == 20
    #if sum((num1,num2)) == 20 or num1 == 20 or num2 == 20:
    #    return True
    #else:
    #    return False

def old_macdonald(word):
    if len(word) > 3:
        return word[0].upper() + word[1:3] + word[3].upper() + word[4:]
        #or , extract the first 3 letters  and the rest
        # first_half = word[:3].capitalize()
        # second_half = word[3:].capitalize()
        # concatenate those 2 you get the result


    else:
        return "Name is too short"

def master_yoda(words):
    length = len(words.split())
    wordlist = words.split()
    wordlist
    str = ''
    while length > 0:
        if length > 1:
            str += wordlist[length-1] + ' '
        else:
            str += wordlist[length - 1]
        length -= 1
    return str

def master_yoda1(sentence):
    #for item in enumerate(sentence):
     #   print(item)
    return ' '.join(sentence.split()[::-1])
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere
# the trick part is when you are pulling the items from a list using num[i:i+2] you basically
# are saying that you want items between lets says 1 to 3, so it pulls items at index 1 and items at index 2
# and if they have two 3s next to each other you return True if not return false
def has_33(nums):
    for i in range(0,len(nums) -1):
        if nums[i:i+2] == [3,3]:
            return True;



def blackjack(*args):
    sumresult = sum((args))
    mylist = [*args]
    if sumresult <= 21:
        return sumresult
    elif sumresult > 21 and 11 in args:
        sumresult -= 10
    if sumresult > 21:
        return 'BUST'
    else:
        return sumresult
def paper_doll(text):
    return ''.join(letter * 3 for letter in text)

#summer of 69 - Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
#and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    add = True
    total = 0
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break;
            else:
                add = True
                break

    return total

def spy_game(nums):
    mylist = list()
    for num in nums:
        if num == 0:
            mylist.append(num)
            break
        if num == 7:
            mylist

def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    ',10:'*',11:'***'}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4],'F':[4,10,10,11,10,10,10]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

def square(num):
    return num ** 2

def player_input():
    marker = ''
    while marker != 'X' or marker != 'O':
        marker = input('Player 1: choose X or O  ').upper()
        if (marker == 'X'):
            return ('X','O')
        else:
            return ('O','X')
def place_marker(board,marker,position):
    board[position] = marker
def win_check(board,mark):
    return (( board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        ( board[9] == mark and board[5] == mark and board[1] == mark) or
        (board[7] == mark and board[5] == mark and board[3] == mark))


def display_board(board):
    #clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def chose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board,position):
    return board[position] == ' '
def player_choice(board,turn):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose your next position: (1-9) ' + turn))
    return position
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
#test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)
#print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#print ('Welcome to Tic Tac Toe!')
# while True:
#     theBoard = [' '] *10
#
#     player1_marker,player2_marker = player_input()
#     turn = chose_first()
#     play_game = input('Are you ready to play? Enter Yes or No.')
#     if play_game.lower()[0] == 'y':
#         game_on = True
#     else:
#         game_on = False
#     while game_on:
#         if turn == 'Player 1':
#             display_board(theBoard)
#             position = player_choice(theBoard,turn)
#             place_marker(theBoard,player1_marker,position)
#             if win_check(theBoard, player1_marker):
#                 display_board(theBoard)
#                 print('Congratulations! You have won the game!')
#                 game_on = False
#             else:
#                 if full_board_check(theBoard):
#                     display_board(theBoard)
#                     print('The game is a draw!')
#                     break
#                 else:
#                     turn = 'Player 2'
#         else:
#             display_board(theBoard)
#             position = player_choice(theBoard,turn)
#             place_marker(theBoard, player2_marker, position)
#
#             if win_check(theBoard, player2_marker):
#                 display_board(theBoard)
#                 print('Player 2 has won!')
#                 game_on = False
#             else:
#                 if full_board_check(theBoard):
#                     display_board(theBoard)
#                     print('The game is a draw!')
#                     break
#                 else:
#                     turn = 'Player 1'
#     if not replay():
#         break

#display_board(test_board)
#print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#place_marker(test_board,'$',8)
#display_board(test_board)





#myresult = myfunc(-2,4)
#print(myresult)
#print(myfunc1('Srinivas'))
#print (lesser_of_two_evens(2,4))
#print(lesser_of_two_evens(3,7))
#print(lesser_of_two_evens(3, 8))
#print(animal_crackers("Srini good"))
#print(makes_twenty(2,18))
#print(old_macdonald('srinivas'))
#print(master_yoda('I am home'))
#print(master_yoda1('I am home'))
#print(blackjack(5,6,7))
#print(blackjack(9,9,9))
#print(blackjack(9,9,11))
#print(blackjack(10,10,11))
#print(paper_doll(('Mississippi')))
#print(summer_69([1,3,5]))
#print(summer_69([4,5,6,7,8,9]))
#print(summer_69([2,1,6,9,11]))
#print_big('F')
#print(list(map(square,[1,2,3,4,5])))


class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2 - x1)**2 + (y2 - y1)** 2) ** 0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1) / (x2-x1)

class Cylinder:
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
    def volume(self):
        return self.pi * self.radius**2 * self.height
    def surface_area(self):
        top = self.pi * (self.radius)**2
        return (2*top) + (2*self.pi*self.radius*self.height)


class Account:

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print('Deposit accepted')

    def withdraw(self,amount):
        if amount > self.balance:
            print('Withdrawl is more than the available balance')
        else:
            self.balance -= amount
            print('Withdrawl accepted')
    def __str__(self):

        return ("{n} has balance ${b}".format(n=self.owner,b=self.balance))



# coordinate1 = (3,2)
# coordinate2 = (8,10)
# l = Line(coordinate1,coordinate2)
# print(l.distance())
# print(l.slope())
#
# c = Cylinder(2,3)
# print (c.volume())
# print (c.surface_area())

# acct1 = Account('Jose',100)
# print(acct1)
# acct1.deposit(10)
# acct1.deposit(200)
# acct1.withdraw(20)
# acct1.withdraw(25)
# acct1.withdraw(500)
# print(acct1)

try:
    for i in ['a','b','c']:
        print (i**2)
except TypeError:
    print("Unsupported operand types(s) for ** pow(): str and int")
finally:
    print("All Done")

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print('ZeroDivisionError: division by zero')
finally:
    print('All Done')

while True:
    try:
        num1 = int(input("Please enter a number: "))
        print(num1 **2)
    except:
        print('Woops ! please provide a number: ')
    else:
        print('Thank you, your number squared is' + str(num1**2))
        break;

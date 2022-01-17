#This program is based off the game TicTacToe. There are 3 modes: easy, medium and hard. Each mode increases in difficulty. In easy mode, the computer picks a square at random. In medium mode, the computer plays defense but not offense. In hard mode, the computer plays offense and defense. 

import turtle as t
import random as rand
wn = t.Screen()
drawer = t.Turtle()
cpu_score_writer = t.Turtle()
user_score_writer = t.Turtle()
tie_writer = t.Turtle()
announcement_writer = t.Turtle()

square1center = -150,150 #top left
square2center = 0,150 #top middle 
square3center = 150,150 #top right
square4center = -150,0 #middle left
square5center = 0,0 #middle middle
square6center = 150,0 #middle right
square7center = -150,-150 #bottom left
square8center = 0,-150 #bottom middle
square9center = 150,-150 #bottom right

squares_list = [square1center, square2center, square3center, square4center, square5center, square6center, square7center, square8center, square9center]
diagonals_list = [square1center, square3center, square7center, square9center]
sides_list = [square2center, square4center, square6center, square8center]
static_diagonals_list = [square1center, square3center, square7center, square9center]
static_sides_list = [square2center, square4center, square6center, square8center]
no_winner = True
user_choice_list = []
cpu_choice_list = []
user_row1 = 0
user_row2 = 0
user_row3 = 0
user_column1 = 0
user_column2 = 0
user_column3 = 0
user_left_diagonal = 0
user_right_diagonal = 0
cpu_row1 = 0
cpu_row2 = 0
cpu_row3 = 0
cpu_column1 = 0
cpu_column2 = 0
cpu_column3 = 0
cpu_left_diagonal = 0
cpu_right_diagonal = 0
turns = 0
user_score = 0
cpu_score = 0
cat_score = 0
start_pressed = False
picked_correct = True
font_size = ("Arial", "15")

cpu_score_writer.penup()
cpu_score_writer.speed(0)
cpu_score_writer.goto(-225,250)
cpu_score_writer.hideturtle()
tie_writer.penup()
tie_writer.speed(0)
tie_writer.goto(-62.5,250)
tie_writer.hideturtle()
user_score_writer.penup()
user_score_writer.speed(0)
user_score_writer.goto(100, 250)
user_score_writer.hideturtle()
announcement_writer.penup()
announcement_writer.speed(0)
announcement_writer.goto(0,-275)
announcement_writer.hideturtle()

drawer.speed(0)
drawer.hideturtle()
drawer.pensize(5)

def setup():
  global turns, user_row1, user_row2, user_row3, user_column1, user_column2, user_column3, user_left_diagonal, user_right_diagonal, cpu_row1, cpu_row2, cpu_row3, cpu_column1, cpu_column2, cpu_column3, cpu_left_diagonal, cpu_right_diagonal, no_winner, squares_list, user_choice_list, cpu_choice_list, user_score, cpu_score, picked_correct, diagonals_list, sides_list, static_sides_list, static_diagonlas_list
  drawer.pencolor("black")
  drawer.penup()
  drawer.goto(0,0)
  drawer.setheading(0)
  drawer.goto(-225,-75)
  drawer.pendown()
  drawer.forward(450)
  drawer.penup()
  drawer.goto(-225,75)
  drawer.pendown()
  drawer.forward(450)
  drawer.penup()
  drawer.goto(-75,225)
  drawer.pendown()
  drawer.right(90)
  drawer.forward(450)
  drawer.penup()
  drawer.goto(75,225)
  drawer.pendown()
  drawer.forward(450)
  drawer.pencolor("white")
  cpu_score_writer.clear()
  cpu_score_writer.write("CPU Score: " + str(cpu_score), font=font_size)
  tie_writer.clear()
  tie_writer.write("Times Tied: " + str(cat_score), font=font_size)
  user_score_writer.clear()
  user_score_writer.write("Your Score: " + str(user_score), font=font_size) 

  squares_list = [square1center, square2center, square3center, square4center, square5center, square6center, square7center, square8center, square9center]
  diagonals_list = [square1center, square3center, square7center, square9center]
  sides_list = [square2center, square4center, square6center, square8center]
  no_winner = True
  user_choice_list = []
  cpu_choice_list = []
  user_row1 = 0
  user_row2 = 0
  user_row3 = 0
  user_column1 = 0
  user_column2 = 0
  user_column3 = 0
  user_left_diagonal = 0
  user_right_diagonal = 0
  cpu_row1 = 0
  cpu_row2 = 0
  cpu_row3 = 0
  cpu_column1 = 0
  cpu_column2 = 0
  cpu_column3 = 0
  cpu_left_diagonal = 0
  cpu_right_diagonal = 0
  turns = 0
  picked_correct = True

def cpu_go():
  global turns, cpu_row1, cpu_row2, cpu_row3, cpu_column1, cpu_column2, cpu_column3, cpu_left_diagonal, cpu_right_diagonal, user_row1, user_row2, user_row3, user_column1,user_column2, user_column3, user_left_diagonal, user_right_diagonal, no_winner, squares_list, cpu_score, cat_score, cpu_choice, diagonals_list, sides_list, static_diagonlas_list, static_sides_list
  if ((mode == "easy") or (mode == "Easy")):
    if(len(squares_list) == 1):
      cpu_choice = squares_list[0]
    else:
      cpu_index = rand.randint(0,(len(squares_list)-1))
      cpu_choice = squares_list[cpu_index]
  elif ((mode == "medium") or (mode == "Medium")):
    if user_row1>1 and (user_row1 + cpu_row1) < 3:
      if (square3center in squares_list):
        cpu_choice = square3center
      elif (square2center in squares_list):
        cpu_choice = square2center
      elif (square1center in squares_list):
        cpu_choice = square1center
    elif user_row2>1 and (user_row2 + cpu_row2) < 3:
      if(square6center in squares_list):
        cpu_choice = square6center
      elif(square5center in squares_list):
        cpu_choice = square5center
      elif (square4center in squares_list):
        cpu_choice = square4center
    elif user_row3>1 and (user_row3 + cpu_row3) < 3:
      if (square9center in squares_list):
        cpu_choice = square9center
      elif (square8center in squares_list):
        cpu_choice = square8center
      elif (square7center in squares_list):
        cpu_choice = square7center
    elif user_column1>1 and (user_column1 + cpu_column1) < 3:
      if (square7center in squares_list):
        cpu_choice = square7center
      elif (square4center in squares_list):
        cpu_choice = square4center
      elif (square1center in squares_list):
        cpu_choice = square1center
    elif user_column2>1 and (user_column2 + cpu_column2) < 3:
      if (square8center in squares_list):
        cpu_choice = square8center
      elif (square5center in squares_list):
        cpu_choice = square5center
      elif (square2center in squares_list):
        cpu_choice = square2center
    elif user_column3>1 and (user_column3 + cpu_column3) < 3:
      if (square9center in squares_list):
        cpu_choice = square9center
      elif  (square6center in squares_list):
        cpu_choice = square6center
      elif (square3center in squares_list):
        cpu_choice = square3center
    elif user_left_diagonal>1 and (user_left_diagonal + cpu_left_diagonal) < 3:
      if (square9center in squares_list):
        cpu_choice = square9center
      elif (square5center in squares_list):
        cpu_choice = square5center
      elif (square1center in squares_list):
        cpu_choice = square1center
    elif user_right_diagonal>1 and (user_right_diagonal + cpu_right_diagonal) < 3:
      if (square7center in squares_list):
        cpu_choice = square7center
      elif (square5center in squares_list):
        cpu_choice = square5center
      elif  (square3center in squares_list):
        cpu_choice = square3center
    else: 
      if(len(squares_list) == 1):
        cpu_choice = squares_list[0]
      else:
        cpu_index = rand.randint(0,(len(squares_list)-1))
        cpu_choice = squares_list[cpu_index]
  elif ((mode=="hard") or (mode=="Hard")):
    if cpu_row1>1 and (user_row1 + cpu_row1) < 3:
      if (square3center in squares_list):
        cpu_choice = square3center
      elif (square2center in squares_list):
        cpu_choice = square2center
      elif (square1center in squares_list):
        cpu_choice = square1center
    elif cpu_row2>1 and (user_row2 + cpu_row2) < 3:
      if(square6center in squares_list):
        cpu_choice = square6center
      elif(square5center in squares_list):
        cpu_choice = square5center 
      elif (square4center in squares_list):
        cpu_choice = square4center
    elif cpu_row3>1 and (user_row3 + cpu_row3) < 3:
      if (square9center in squares_list):
        cpu_choice = square9center
      elif (square8center in squares_list):
        cpu_choice = square8center
      elif (square7center in squares_list):
        cpu_choice = square7center
    elif cpu_column1>1 and (user_column1 + cpu_column1) < 3:
      if (square7center in squares_list):
        cpu_choice = square7center
      elif (square4center in squares_list):
        cpu_choice = square4center
      elif (square1center in squares_list):
        cpu_choice = square1center
    elif cpu_column2>1 and (user_column2 + cpu_column2) < 3:
      if (square8center in squares_list):
        cpu_choice = square8center
      elif (square5center in squares_list):
        cpu_choice = square5center
      elif (square2center in squares_list):
        cpu_choice = square2center
    elif cpu_column3>1 and (user_column3 + cpu_column3) < 3:
      if (square9center in squares_list):
        cpu_choice = square9center
      elif  (square6center in squares_list):
        cpu_choice = square6center
      elif (square3center in squares_list):
        cpu_choice = square3center
    elif cpu_left_diagonal>1 and (user_left_diagonal + cpu_left_diagonal) < 3:
      if (square9center in squares_list):
        cpu_choice = square9center
      elif (square5center in squares_list):
        cpu_choice = square5center 
      elif (square1center in squares_list):
        cpu_choice = square1center
    elif cpu_right_diagonal>1 and (user_right_diagonal + cpu_right_diagonal) < 3:
      if (square7center in squares_list):
        cpu_choice = square7center
      elif (square5center in squares_list):
        cpu_choice = square5center 
      elif  (square3center in squares_list):
        cpu_choice = square3center
    elif user_row1>1 and (user_row1 + cpu_row1) < 3:
      if (square3center in squares_list):
        cpu_choice = square3center
      elif (square2center in squares_list):
        cpu_choice = square2center
      elif (square1center in squares_list):
        cpu_choice = square1center
    elif user_row2>1 and (user_row2 + cpu_row2) < 3:
      if(square6center in squares_list):
        cpu_choice = square6center
      elif(square5center in squares_list):
        cpu_choice = square5center 
      elif (square4center in squares_list):
        cpu_choice = square4center
    elif user_row3>1 and (user_row3 + cpu_row3) < 3:
      if (square9center in squares_list):
        cpu_choice = square9center
      elif (square8center in squares_list):
        cpu_choice = square8center
      elif (square7center in squares_list):
        cpu_choice = square7center
    elif user_column1>1 and (user_column1 + cpu_column1) < 3:
      if (square7center in squares_list):
        cpu_choice = square7center
      elif (square4center in squares_list):
        cpu_choice = square4center
      elif (square1center in squares_list):
        cpu_choice = square1center
    elif user_column2>1 and (user_column2 + cpu_column2) < 3:
      if (square8center in squares_list):
        cpu_choice = square8center
      elif (square5center in squares_list):
        cpu_choice = square5center 
      elif (square2center in squares_list):
        cpu_choice = square2center
    elif user_column3>1 and (user_column3 + cpu_column3) < 3:
      if (square9center in squares_list):
        cpu_choice = square9center
      elif  (square6center in squares_list):
        cpu_choice = square6center
      elif (square3center in squares_list):
        cpu_choice = square3center
    elif user_left_diagonal>1 and (user_left_diagonal + cpu_left_diagonal) < 3:
      if (square9center in squares_list):
        cpu_choice = square9center
      elif (square5center in squares_list):
        cpu_choice = square5center
      elif (square1center in squares_list):
        cpu_choice = square1center
    elif user_right_diagonal>1 and (user_right_diagonal + cpu_right_diagonal) < 3:
      if (square7center in squares_list):
        cpu_choice = square7center
      elif (square5center in squares_list):
        cpu_choice = square5center
      elif  (square3center in squares_list):
        cpu_choice = square3center
    else: 
      if(len(squares_list) == 1):
        cpu_choice = squares_list[0]
      else:
        cpu_index = rand.randint(0,(len(squares_list)-1))
        cpu_choice = squares_list[cpu_index]
  else: 
    announcement_writer.clear()
    announcement_writer.write("Mode not ready yet", align="center", font=font_size)

  print(cpu_choice)
  print(squares_list)
  squares_list.remove(cpu_choice)
  cpu_choice_list.append(cpu_choice)
  drawer.penup()
  drawer.goto(cpu_choice)
  drawer.setheading(270)
  drawer.forward(50)
  drawer.setheading(0)
  drawer.pendown()
  drawer.circle(50)
  turns += 1
  if cpu_choice == square1center:
    cpu_row1 += 1
    cpu_column1 += 1
    cpu_left_diagonal += 1
  elif (cpu_choice == square4center):
    cpu_row2 += 1
    cpu_column1 += 1
  elif (cpu_choice == square7center):
    cpu_row3 += 1
    cpu_column1 += 1
    cpu_right_diagonal += 1
  elif (cpu_choice == square2center):
    cpu_row1 += 1
    cpu_column2 += 1
  elif (cpu_choice == square5center):
    cpu_row2 += 1
    cpu_column2 += 1
    cpu_left_diagonal += 1
    cpu_right_diagonal += 1
  elif (cpu_choice == square8center):
    cpu_row3 += 1
    cpu_column2 += 1
  elif (cpu_choice == square3center):
    cpu_row1 += 1
    cpu_column3 += 1
    cpu_right_diagonal += 1
  elif (cpu_choice == square6center):
    cpu_row2 += 1
    cpu_column3 += 1
  else:
    cpu_row3 += 1
    cpu_column3 += 1
    cpu_left_diagonal += 1

  if (cpu_row1>2 or cpu_row2>2 or cpu_row3>2 or cpu_column1>2 or cpu_column2>2 or cpu_column3>2 or cpu_left_diagonal>2 or cpu_right_diagonal>2):
    cpu_score += 1
    turns += 9
    no_winner = False
    announcement_writer.clear()
    announcement_writer.write("You lose! Press r to restart", align="center", font=font_size)

def user_go(xpos, ypos):
  global user_row1, user_row2, user_row3, user_column1, user_column2, user_column3, user_left_diagonal, user_right_diagonal, no_winner, turns, user_score, start_pressed, picked_correct, user_choice, cat_score, diagonals_list, sides_list, static_diagonals_list, static_sides_list
  if picked_correct == True:
    announcement_writer.clear()
  if (xpos<-75 and ypos > 75):
    user_choice = square1center
    if (user_choice in squares_list):
      user_row1 += 1
      user_column1 += 1
      user_left_diagonal += 1
      picked_correct = True
      diagonals_list.remove(user_choice)
    else:
      announcement_writer.write("Pick a square that isn't taken", align="center", font=font_size)
      picked_correct = False
  elif (xpos<-75 and (-75 < ypos < 75)):
    user_choice = square4center
    if (user_choice in squares_list):
      user_row2 += 1
      user_column1 += 1
      picked_correct = True
      sides_list.remove(user_choice)
    else:
      announcement_writer.write("Pick a square that isn't taken", align="center", font=font_size)
      picked_correct = False
  elif (xpos<-75 and ypos < -75):
    user_choice = square7center
    if (user_choice in squares_list):
      user_row3 += 1
      user_column1 += 1
      user_right_diagonal += 1
      picked_correct = True
      diagonals_list.remove(user_choice)
    else:
      announcement_writer.write("Pick a square that isn't taken", align="center", font=font_size)
      picked_correct = False
  elif ((-75 < xpos < 75) and ypos > 75):
    user_choice = square2center
    if (user_choice in squares_list):
      user_row1 += 1
      user_column2 += 1
      picked_correct = True
      sides_list.remove(user_choice)
    else:
      announcement_writer.write("Pick a square that isn't taken", align="center", font=font_size)
      picked_correct = False
  elif ((-75 < xpos < 75) and (-75 <ypos < 75)):
    user_choice = square5center
    if (user_choice in squares_list):
      user_row2 += 1
      user_column2 += 1
      user_left_diagonal += 1
      user_right_diagonal += 1
      picked_correct = True
    else:
      announcement_writer.write("Pick a square that isn't taken", align="center", font=font_size)
      picked_correct = False
  elif ((-75 < xpos < 75) and ypos < -75):
    user_choice = square8center
    if (user_choice in squares_list):
      user_row3 += 1
      user_column2 += 1
      picked_correct = True
      sides_list.remove(user_choice)
    else:
      announcement_writer.write("Pick a square that isn't taken", align="center", font=font_size)
      picked_correct = False
  elif (xpos>75 and ypos > 75):
    user_choice = square3center
    if (user_choice in squares_list):
      user_row1 += 1
      user_column3 += 1
      user_right_diagonal += 1
      picked_correct = True
      diagonals_list.remove(user_choice)
    else:
      announcement_writer.write("Pick a square that isn't taken", align="center", font=font_size)
      picked_correct = False
  elif (xpos>75 and (-75 < ypos < 75)):
    user_choice = square6center
    if (user_choice in squares_list):
      user_row2 += 1
      user_column3 += 1
      picked_correct = True
      sides_list.remove(user_choice)
    else:
      announcement_writer.write("Pick a square that isn't taken", align="center", font=font_size)
      picked_correct = False
  else:
    user_choice = square9center
    if (user_choice in squares_list):
      user_row3 += 1
      user_column3 += 1
      user_left_diagonal += 1
      picked_correct = True
      diagonals_list.remove(user_choice)
    else:
      announcement_writer.write("Pick a square that isn't taken", align="center", font=font_size)
      picked_correct = False

  user_choice_list.append(user_choice)

  if ((turns < 9) and (start_pressed == True) and (picked_correct == True)):
    drawer.penup()
    drawer.goto(user_choice)
    drawer.pendown()
    drawer.setheading(45)
    drawer.forward(50)
    drawer.backward(100)
    drawer.forward(50)
    drawer.setheading(135)
    drawer.forward(50)
    drawer.backward(100)
    drawer.forward(50)
    turns += 1
    squares_list.remove(user_choice)
      

    if ((user_row1>2) or (user_row2>2) or (user_row3>2) or (user_column1>2) or (user_column2>2) or (user_column3>2) or (user_left_diagonal>2) or (user_right_diagonal>2)): 
      user_score += 1
      turns += 9
      no_winner = False
      announcement_writer.clear()
      announcement_writer.write("You win! Press r to restart", align="center", font=font_size)
      

    if((len(squares_list) != 0) and 
    (no_winner == True)):
      cpu_go()

    if (turns == 9):
      turns += 1
      cat_score += 1
      no_winner = False
      announcement_writer.clear()
      announcement_writer.write("Cat's game! Press r to restart", align="center", font=font_size)
  elif (start_pressed == False):
      announcement_writer.clear()
      announcement_writer.write("Press r to start", align="center", font=font_size)
  elif (picked_correct == False):
    xpos = rand.randint(-150,150)
    ypos = rand.randint(-150,150)
    user_go(xpos, ypos)
  else:
    announcement_writer.clear()
    announcement_writer.write("Press r to play again", align="center", font=font_size)

def start():
  global start_pressed
  drawer.clear()
  start_pressed = True
  setup()

correct_mode = False

while (correct_mode== False):
  mode = input("What mode do you want: Easy, Medium, or Hard? ")
  if ((mode == "easy") or (mode == "Easy") or (mode == "medium") or (mode == "Medium") or (mode == "hard") or (mode == "Hard")):
    correct_mode = True
  else:
    announcement_writer.clear()
    announcement_writer.write("Pick a mode", align="center", font=font_size)

announcement_writer.clear()
announcement_writer.write("Press r to start", align="center", font=font_size)

wn.listen()
wn.onscreenclick(user_go)
wn.onkeypress(start, "r")
wn.bgcolor("light green")
wn.mainloop()

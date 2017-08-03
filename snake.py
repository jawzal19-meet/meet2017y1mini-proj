
import turtle
import random
turtle.tracer(1,0)

SIZE_X=900
SIZE_Y=600
SQUARE_SIZE=20


turtle.setup(SIZE_X, SIZE_Y)
turtle.penup()

border=turtle.clone()
border.penup()
border.goto(-399,249)
border.pendown()
border.goto(399,249)
border.goto(399,-249)
border.goto(-399,-249)
border.goto(-399,249)
border.penup()
border.hideturtle()

START_LENGTH=7

pos_list=[]
stamp_list=[]

food_pos=[]
food_stamps=[]

snake= turtle.clone()
snake.shape('square')
turtle.hideturtle()

for i in range (START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    new_list=snake.stamp()
    stamp_list.append(new_list)
    
    
UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100
SPACEBAR='space'
UP=0
LEFT=1
DOWN=2
RIGHT=3

direction=UP
UP_EDGE=250
DOWN_EDGE=-250
RIGHT_EDGE=400
LEFT_EDGE=-400


def up():
    global direction
    if direction!=DOWN:
        direction=UP
    print('you pressed the up key!')

def left():
    global direction
    if direction!=RIGHT:
        direction=LEFT
    print('you pressed the left key!')
    
def down():
    global direction
    if direction!=UP:
        direction=DOWN
    print('you pressed the down key!')
    
def right():
    global direction
    if direction!=LEFT:
        direction=RIGHT
    print('you pressed the right key!')


turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()
#turtle.register_shape("trash.gif")
food= turtle.clone()
food.shape("turtle")



def make_food():
    min_x=-int(SIZE_X/2.5/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2.5/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2.5/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2.5/SQUARE_SIZE)-1
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    new_pos=(food_x,food_y)
    food_pos.append(new_pos)
    stamp_id=food.stamp()
    food_stamps.append(stamp_id)

def move_snake():
    global START_LENGTH
    my_pos= snake.pos()
    x_pos= my_pos[0]
    y_pos= my_pos[1]


        
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("you moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("you moved left!")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("you moved down!")
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("you moved up!")

        
       
            
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp= snake.stamp()
    stamp_list.append(new_stamp)

    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) 
        food.clearstamp(food_stamps[food_ind]) 
        food_pos.pop(food_ind) 
        food_stamps.pop(food_ind)
        print("You have eaten the food!")
        make_food()
##        back_pos=pos_list[0]
##        pos_list[0].append(back_pos)
##        START_LENGTH+=1
    else:
        old_stamp=stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    ####
    
    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]
    
    if new_x_pos>=RIGHT_EDGE:
        print('you hit the right edge! Game over!')
        quit()
    elif new_y_pos<=DOWN_EDGE:
         print('you hit the bottom edge! Game over!')
         quit()
    elif new_x_pos<=LEFT_EDGE:
          print('you hot the life edge! Game over!')
          quit()
    elif new_y_pos>=UP_EDGE:
         print('you hit the top edge! Game over!')
         quit()
    head_pos=pos_list[-1]
    body_pos=pos_list[0:-1]
    if head_pos in body_pos:
        print('you ate yourself! Game over')
        quit()       

        
   
    turtle.ontimer(move_snake,TIME_STEP)




##################################333

food_pos=[(100,100)]
food_stamps=[]

for this_food_pos in food_pos:
    food.goto(this_food_pos)
    new_food=food.stamp()
    food_stamps.append(new_food)


move_snake()
    
turtle.mainloop()

import tkinter
from tkinter import ALL, Canvas, Tk, font, Label
import random


# Define constant variables
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOUR = "#659fd1"
FOOD_COLOUR = "#C7372F"
BACKGROUND_COLOUR = "#77DD77"



class Snake:
        def __init__(self) -> None:
             self.body_size = BODY_PARTS
             self.coordinates = []
             self.squares = []
             
             for i in range (0, BODY_PARTS):
                  self.coordinates.append([0, 0])

             for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOUR, tag='snake')
                self.squares.append(square)



class Food:
        def __init__(self) -> None:
             
            x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

            self.coordinates = [x, y]

            canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOUR, tag='food')


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == 'up':
         y -= SPACE_SIZE
    elif direction == 'down':
         y += SPACE_SIZE
    elif direction == 'left':
         x -= SPACE_SIZE
    elif direction == 'right':
         x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))    
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)
    snake.squares.insert(0, square) 

    if x == food.coordinates[0] and y == food.coordinates[1]:
         
         global score
         score += 1

         label.config(text='Score: {}'.format(score))

         canvas.delete('food')
         food = Food()

    else:
          del snake.coordinates[-1]
          canvas.delete(snake.squares[-1])
          del snake.squares[-1]


    if check_collisions(snake):
         game_over()
         
     

    else:
         window.after(SPEED, next_turn, snake, food)
         


         

    


def change_direction(new_direction):
    global direction

    if new_direction == 'left':
         if direction != 'right':
               direction = new_direction
     
    elif new_direction == 'right':
         if direction != 'left':
               direction = new_direction

    elif new_direction == 'up':
         if direction != 'down':
               direction = new_direction

    elif new_direction == 'down':
         if direction != 'up':
               direction = new_direction

def check_collisions(snake):
         
         x, y = snake.coordinates[0]

         if x < 0 or x >= GAME_WIDTH:
              return True
         if y < 0 or y >= GAME_HEIGHT:
              return True
         
         for body_part in snake.coordinates[1: ]:
              if x == body_part[0] and y == body_part[1]:
                   return True
              
         return False
              

              

    


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() /2, canvas.winfo_height() /2,
                       font=('consola', 65), text='GAME OVER', fill='red', tag='gameover')



window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text = 'Score:{}'.format(score), font = ('Impact', 30))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH,)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

centre_window_x = int(((screen_width / 2) - (window_width / 2)) / 20) * 16
centre_window_y = int(((screen_height / 2) - (window_height / 2))/ 20) * 16

window.geometry(f'{window_width}x{window_height}+{centre_window_x}+{centre_window_y}')

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

window.bind('<a>', lambda event: change_direction('left'))
window.bind('<d>', lambda event: change_direction('right'))
window.bind('<w>', lambda event: change_direction('up'))
window.bind('<s>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

# Start TKinter events
window.mainloop()


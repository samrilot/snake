import random
import curses 
#Supplies a terminal-independent, screen-painting, and keyboard-handling facility for text-based terminals

#Iniailize the Screen
screen = curses.initscr()
curses.curs_set(0) #Set to 0 so it wont show up on the screen
screenHeight, screenWidth = screen.getmaxyx() #Set width and height

#Create a new window 
#Accept keypad inputs
window = curses.newwin(screenHeight, screenWidth, 0, 0)
window.keypad(1) 
window.timeout(100) #Refresh every 100ms

#Set the Snakes initial position
snake_x = screenWidth//4
snake_y = screenHeight//2

#Create the body of the snake
snakeBody = [
    [snake_x, snake_y],
    [snake_x-1, snake_y],
    [snake_x-2, snake_y]
]

#Create 'food'
food = [screenHeight//2, screenWidth//2] 
window.addch(food[0], food[1], curses.ACS_PI)

#Create game system
key = curses.KEY_RIGHT #Initial movement
while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key #Will give no change unless there is a new key input

    #Loop to see if game over [Hits screenHeight/ screenWidth/ in itself]
    if snakeBody[0][0] in [0, screenHeight] or snakeBody[0][1] in [0, screenWidth] or snakeBody[0] in snakeBody[1:]:
        curses.endwin()
        quit()

    new_head = [snakeBody[0][0], snakeBody[0][1]]

    #Movement system
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snakeBody.insert(0, new_head)

    #Food system
    if snakeBody[0] == food:
        food = None
        while food is None:
            newFood = [
                random.randint(1, screenHeight-1), random.randint(1, screenWidth-1)
            ]
            food = newFood if newFood not in snakeBody else None
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snakeBody.pop()
        window.addch(tail[0], tail[1], ' ')

    window.addch(snakeBody[0][0], snakeBody[0][1], curses.ACS_CKBOARD)

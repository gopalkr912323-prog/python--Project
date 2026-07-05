# high_score = 0
# if score > high_score:
#     high_score = score
paused = False

def pause(event=None):
    global paused
    paused = not paused


import tkinter as tk
import random


# -------------------------------
# Window Settings
# -------------------------------
WIDTH = 600
HEIGHT = 400
SIZE = 20

root = tk.Tk()
root.title("Snake Game")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# -------------------------------
# Snake
# -------------------------------
snake = [(100, 100)]
food = (
    random.randrange(0, WIDTH, SIZE),
    random.randrange(0, HEIGHT, SIZE)
)

score = 0
speed = 150
game_over = False

direction = "Right"

# Draw Snake
def draw_snake():
    canvas.delete("all")

    # Snake
    for x, y in snake:
        canvas.create_rectangle(
            x, y,
            x + SIZE,
            y + SIZE,
            # fill = "#00FF66"
            fill="#00FF66",
            outline="white"
        )

    # Food
    fx, fy = food
    canvas.create_oval(
        fx, fy,
        fx + SIZE,
        fy + SIZE,
        fill="orange"
    )

    # Score
    canvas.create_text(
        60,
        15,
        text=f"Score : {score}",
        fill="white",
        font=("Arial", 14)
    )

# -------------------------------
# Move Snake
# -------------------------------
def move():
    if paused:
        root.after(100, move)
        return

    global food, score, game_over

    if game_over:
        return

    x, y = snake[0]

    if direction == "Right":
        x += SIZE

    elif direction == "Left":
        x -= SIZE

    elif direction == "Up":
        y -= SIZE

    elif direction == "Down":
        y += SIZE

    # Wall Collision
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        game_over = True
        draw_snake()
        show_game_over()
        return

    # Self Collision
    if (x, y) in snake:
        game_over = True
        draw_snake()
        show_game_over()
        return

    snake.insert(0, (x, y))

    # Eat Food
    if (x, y) == food:

        score += 1
        global speed

        if speed > 50:
            speed -= 5

        while True:
            food = (
                random.randrange(0, WIDTH, SIZE),
                random.randrange(0, HEIGHT, SIZE)
            )

            if food not in snake:
                break

    else:
        snake.pop()

    draw_snake()

    root.after(speed, move)

# -------------------------------
# Keyboard Controls
# -------------------------------
def change_direction(event):
    global direction

    if event.keysym == "Right":
        direction = "Right"

    elif event.keysym == "Left":
        direction = "Left"

    elif event.keysym == "Up":
        direction = "Up"

    elif event.keysym == "Down":
        direction = "Down"

def restart(event=None):
    global snake, direction, food, score, game_over

    snake = [(100, 100)]
    direction = "Right"

    food = (
        random.randrange(0, WIDTH, SIZE),
        random.randrange(0, HEIGHT, SIZE)
    )

    score = 0
    game_over = False

    move()

def show_game_over():
    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2,
        text="GAME OVER",
        fill="red",
        font=("Arial", 28, "bold")
    )

    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2 + 40,
        text="Press R to Restart",
        fill="white",
        font=("Arial", 14)
    )

root.bind("<Key>", change_direction)
root.bind("r", restart)

draw_snake()

move()

root.mainloop()
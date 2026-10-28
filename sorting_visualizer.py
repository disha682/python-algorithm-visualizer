
import tkinter as tk
import random

root = tk.Tk()
root.title("Animated Bubble Sort")
root.geometry("700x450")
root.configure(bg="#101827")

numbers = [50, 20, 80, 10, 60, 30, 90]
i = 0
j = 0
running = False

canvas = tk.Canvas(
    root, width=650, height=300,
    bg="#172337", highlightthickness=0
)
canvas.pack(pady=20)

status = tk.Label(
    root, text="Click Start Sorting",
    bg="#101827", fg="white",
    font=("Arial", 14)
)
status.pack()


def draw_bars(active=None, done=False):
    canvas.delete("all")

    for k, num in enumerate(numbers):
        x1 = 20 + k * 90
        y1 = 260 - num * 2.3
        x2 = x1 + 55

        color = "#34D399" if done else "#38BDF8"
        if active and k in active:
            color = "#FBBF24"

        canvas.create_rectangle(
            x1, y1, x2, 260,
            fill=color, outline=""
        )
        canvas.create_text(
            x1 + 27, y1 - 12,
            text=str(num), fill="white"
        )


def animate():
    global i, j, running

    if not running:
        return

    if i >= len(numbers) - 1:
        running = False
        draw_bars(done=True)
        status.config(text="Sorting Completed!")
        return

    if j >= len(numbers) - i - 1:
        j = 0
        i += 1
        root.after(200, animate)
        return

    a, b = numbers[j], numbers[j + 1]
    status.config(text=f"Comparing {a} and {b}")

    if a > b:
        numbers[j], numbers[j + 1] = b, a

    draw_bars([j, j + 1])
    j += 1
    root.after(350, animate)


def start_sort():
    global i, j, running

    if running:
        return

    i = j = 0
    running = True
    animate()


def shuffle():
    global i, j, running

    if running:
        return

    random.shuffle(numbers)
    i = j = 0
    status.config(text="Numbers shuffled!")
    draw_bars()


buttons = tk.Frame(root, bg="#101827")
buttons.pack(pady=15)

tk.Button(
    buttons, text="Start Sorting",
    command=start_sort,
    bg="#2563EB", fg="white",
    padx=15, pady=8
).pack(side="left", padx=10)

tk.Button(
    buttons, text="Shuffle",
    command=shuffle,
    bg="#7C3AED", fg="white",
    padx=15, pady=8
).pack(side="left", padx=10)

draw_bars()
root.mainloop()

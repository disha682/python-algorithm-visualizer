import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Numbers
arr = [45, 12, 78, 34, 56, 23, 89, 10]

# Number to search
target = int(input("Enter number to search: "))

# --------------------------------
# BUBBLE SORT
# --------------------------------

sort_frames = []
data = arr.copy()
n = len(data)

for i in range(n):
    for j in range(n - i - 1):

        sort_frames.append((data.copy(), j, j + 1))

        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

        sort_frames.append((data.copy(), j, j + 1))

sort_frames.append((data.copy(), -1, -1))

# --------------------------------
# LINEAR SEARCH
# --------------------------------

search_frames = []
found_index = -1

for i in range(len(arr)):

    search_frames.append((i, -1))

    if arr[i] == target:
        found_index = i
        search_frames.append((i, found_index))
        break

if found_index == -1:
    search_frames.append((-1, -1))

# --------------------------------
# GRAPH WINDOW
# --------------------------------

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

fig.suptitle(
    "SORTING AND SEARCHING VISUALIZER",
    fontsize=16,
    fontweight="bold"
)

# Animation update function

def update(frame):

    ax1.clear()
    ax2.clear()

    # SORTING GRAPH

    sort_index = min(frame, len(sort_frames) - 1)

    values, first, second = sort_frames[sort_index]

    colors = ["skyblue"] * len(values)

    if first != -1:
        colors[first] = "orange"
        colors[second] = "red"

    if sort_index == len(sort_frames) - 1:
        colors = ["green"] * len(values)

    ax1.bar(range(len(values)), values, color=colors)

    ax1.set_title("Bubble Sort")
    ax1.set_xlabel("Index")
    ax1.set_ylabel("Values")
    ax1.set_ylim(0, max(arr) + 20)

    # SEARCHING GRAPH

    search_index = min(frame, len(search_frames) - 1)

    current, found = search_frames[search_index]

    search_colors = ["skyblue"] * len(arr)

    if found != -1:
        search_colors[found] = "green"

    elif current != -1:
        for k in range(current):
            search_colors[k] = "lightgray"

        search_colors[current] = "orange"

    ax2.bar(range(len(arr)), arr, color=search_colors)

    ax2.set_title("Linear Search")
    ax2.set_xlabel("Index")
    ax2.set_ylabel("Values")
    ax2.set_ylim(0, max(arr) + 20)

    if found != -1:
        ax2.set_title(f"Found {target} at index {found}")

    elif current != -1:
        ax2.set_title(f"Searching: {target}")

    else:
        ax2.set_title(f"{target} Not Found")

    plt.tight_layout()


# --------------------------------
# START ANIMATION
# --------------------------------

total_frames = max(len(sort_frames), len(search_frames))

ani = FuncAnimation(
    fig,
    update,
    frames=total_frames,
    interval=300,
    repeat=False
)

plt.show()
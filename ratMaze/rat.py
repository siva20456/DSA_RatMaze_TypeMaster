import random

def generate_maze(size):
    maze = [[1] * size for _ in range(size)]

    maze[0][0] = 0
    maze[-1][-1] = 0

    max_walls = int(size * size * 0.75)
    while max_walls > 0:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if maze[row][col] == 1 and not (row == 0 and col == 0 or row == size - 1 and col == size - 1):
            maze[row][col] = 0
            max_walls -= 1

    return maze

def print_maze(maze):
    print("+" + "-" * int((len(maze[0]) * 2)) + "+")
    maze[0][0] = "S"
    maze[-1][-1] = "E"
    for row in maze:
        print("|", end="")
        for cell in row:
            if cell == 1:  
                print("\033[31m▓\033[0m", end="") 
            elif cell == 2:  # Path
                print("\033[32m◍\033[0m", end="")  # Green path
            elif cell == "S":  # Start
                print("\033[32mS\033[0m", end="")  # Green start
            elif cell == "E":  # End
                print("\033[32mE\033[0m", end="")  # Green end
            else:  # Open space
                print("\033[34m◌\033[0m", end="")  # Blue space
            print(" ", end="")  
        print("|")
    print("+" + "-" * (len(maze[0]) * 2) + "+")

def bfs(maze, start, end):
    queue = [(start, [start])]
    visited = set()

    maze[0][0] = 0
    maze[-1][-1] = 0

    while queue:
        pos, path = queue.pop(0)
        visited.add(pos)

        if pos == end:
            return path

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (pos[0] + dx, pos[1] + dy)
            if 0 <= new_pos[0] < len(maze) and 0 <= new_pos[1] < len(maze[0]) and maze[new_pos[0]][new_pos[1]] == 0 and new_pos not in visited:
                queue.append((new_pos, path + [new_pos]))

    return None  # No path

def mark_path(maze, path):
    for cell in path:
        maze[cell[0]][cell[1]] = 2  # Mark path cells 

def main():
    size = int(input("Enter maze size: "))
    maze = generate_maze(size)

    while True:
        print_maze(maze)
        choice = input("Print path (p), generate new maze (n), or exit (e): ")

        if choice == "p":
            path = bfs(maze, (0, 0), (size - 1, size - 1))
            if path:
                mark_path(maze, path)
            else:
                print("No path found.")
        elif choice == "n":
            maze = generate_maze(size)
        elif choice == "e":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()


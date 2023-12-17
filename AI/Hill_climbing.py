maze = [
    [22, 33, 40, 12],
    [26, 38, 37, 46],
    [24, 36, 25, 8],
    [81, 50, 20, 30]
]

state = [0, 0]
max_val = 0

while True:
    old_val = max_val
    x = state[0]
    y = state[1]
    print(f"\n(x, y) == ({x}, {y})")
    possible_moves = [(x-1,y), (x+1, y), (x, y+1), (x, y-1), (x-1, y-1),
                      (x-1, y+1), (x+1, y+1), (x+1, y-1)]
    print()
                      
    for (x1, y1) in possible_moves:
        if (0 <= x1 < 4) and (0<= y1 < 4):
            print(f"({x1}, {y1})", end=' ')
            val = maze[x1][y1]
            if (val > max_val):
                max_val = val
                state = [x1, y1]
                print(f"{val}={state}", end = ' ')
                
    if old_val == max_val:
        break
    
print(f"\nMax value by hill climbing is {max_val} and found at {state}")

data = [
    [100, 120, 130],
    [400, 500, 600],
    [150, 140, 110]
    ]
list =[]
for row in data:
    for item in row:
        if item > 190:
            list.append(item)
print(list)
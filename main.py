import time as time

intersections = [[[0, 0], [2, 0]]]
pattern = [["Green", 9], ["Yellow", 1], ["Red", 10]]

while True:
    time.sleep(1)
    print("──────────────────────")
    if intersections[0][0][1] == pattern[intersections[0][0][0]][1]:
        intersections[0][0][0] = (intersections[0][0][0] + 1) % 3
        intersections[0][0][1] = 0
        print(f"NE Light is {pattern[intersections[0][0][0]][0]}")

    if intersections[0][1][1] == pattern[intersections[0][1][0]][1]:
        intersections[0][1][0] = (intersections[0][1][0] + 1) % 3
        intersections[0][1][1] = 0
        print(f"SE Light is {pattern[intersections[0][1][0]][0]}")

    intersections[0][0][1] += 1
    intersections[0][1][1] += 1

from __future__ import division
import copy

def day10():
    filepath = "test0.in"
    with open(filepath) as fp:
        galaxy = []
        line = fp.readline().strip()
        HEIGHT = 0
        while line:
            galaxy.append(line)
            HEIGHT += 1
            line = fp.readline().strip()

        LENGTH = len(galaxy[0])

        asteroids = []
        
        for h in range(0, HEIGHT):
            for l in range(0, LENGTH):
                # if galaxy[l][h] == "#":
                if galaxy[l][h] != ".":
                    # True = not blocked
                    asteroids.append([[h, l], True])

        total = HEIGHT * LENGTH
        max_blocking = 0
        station = []
        lens = []

        for asteroid in asteroids:
            asteroids_temp = copy.deepcopy(asteroids)
            asteroids_temp = [a for a in asteroids_temp if a[0] != asteroid[0]]

            for other in asteroids_temp:
                if asteroids_temp[asteroids_temp.index(other)][1]:
                    start = asteroid[0]
                    end = other[0]

                    if asteroid[0] == [0, 0]:
                        # print("asteroid is: " + '[' + str(asteroid[0][0]) + ',' + str(asteroid[0][1]) + ']')
                        print("other is: " + '[' + str(other[0][0]) + ',' + str(other[0][1]) + ']')
                        print(asteroids_temp)

                    asteroids_temp = mark_blocked(start, end, asteroids_temp)

            

            num_visible = 0
            for a in asteroids_temp:
                if a[1]:
                    num_visible += 1

            lens.append(num_visible)
            # print(num_visible)

            if num_visible > max_blocking:
                # print("NEW MAX")
                max_blocking = num_visible
                station = asteroid
                # print(station)
            
            if asteroid[0] == [0, 0]:
                print('[' + str(asteroid[0][0]) + ',' + str(asteroid[0][1]) + '] -> ' + str(total - num_visible - 1))
                # print(num_visible)
                print("")
        
        # print(asteroids)
        # print(station)
        # print(lens)
        print("Best is " + "[" + str(station[0][0]) + ", " + str(station[0][1]) + "] with " + str(max_blocking) + " other asteroids detected.")

def mark_blocked(start, end, asteroids):
    for asteroid in [a for a in asteroids if a[0] != end and a[0] != start]:
        index = asteroids.index(asteroid)
        
        start_x = start[0]
        start_y = start[1]

        end_x = end[0]
        end_y = end[1]
        
        x = asteroid[0][0]
        y = asteroid[0][1]

        # If the slope is undefined and all the points are colinear
        if start_x - end_x == 0:
            if start_x - x == 0 and (start_y < end_y < y or start_y > end_y > y):
                print("Removing: [" + str(x) + ", " + str(y) + "]")
                asteroids[index][1] = False
        
        else:
            # y = mx + b babyyyyy
            m = (start_y - end_y) / (start_x - end_x)
            b = start_y - (m * start_x)

            if y == m * x + b:
                if start_x < end_x < x or start_x > end_x > x:
                    print("Removing: [" + str(x) + ", " + str(y) + "]")
                    asteroids[index][1] = False
    
    return asteroids

if __name__ == '__main__':
    day10()
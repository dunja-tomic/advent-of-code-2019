# generate a 2D array of each point that the path visits
def getallpoints(path):
    points = []
    x = y = 0
    
    for move in path:
        for i in range(1, int(move[1:]) + 1):
            if move[0] == "U":
                y += 1
            elif move[0] == "D":
                y -= 1
            elif move[0] == "R":
                x += 1
            elif move[0] == "L":
                x -= 1
            
            points.append([x, y])
    
    return points

def distance(point):
    return abs(point[0]) + abs(point[1])

def part1():
    # keep track of every point at which the line has been
    filepath = "day3.in"
    with open(filepath) as fp:
        path1 = fp.readline().strip().split(',')
        path2 = fp.readline().strip().split(',')

        path1 = getallpoints(path1)
        path2 = getallpoints(path2)

        both = [point for point in path1 if point in path2]

        min = distance(both[0])
        for point in both:
            if distance(point) < min:
                min = distance(point)
        
        print("The distance to the closest intersection is: " + str(min))

def part2():
    # keep track of every point at which the line has been
    filepath = "day3.in"
    with open(filepath) as fp:
        path1 = fp.readline().strip().split(',')
        path2 = fp.readline().strip().split(',')

        path1 = getallpoints(path1)
        path2 = getallpoints(path2)

        both = [point for point in path1 if point in path2]

        min = path1.index(both[0]) + path2.index(both[0]) + 2
        for point in both:
            # number of points it takes to get to the intersection
            steps = path1.index(point) + path2.index(point) + 2
            if steps < min:
                min = steps

        print("The fewest combined steps to an intersection is: " + str(min))

if __name__ == '__main__':
    part1()
    part2()
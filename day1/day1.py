import math

def part1():

    filepath = "day1.in"
    total = 0
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            mass = math.floor(int(line) / 3) - 2
            total += mass
            line = fp.readline()
    
    print("The total fuel required for part 1 is: " + str(total))

def part2():
    filepath = "day1.in"
    total = 0
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            linetotal = 0

            mass = line
            while (1):
                mass = math.floor(int(mass) / 3) - 2

                if mass <= 0:
                    break

                linetotal += mass
                
            total += linetotal
            line = fp.readline()

    print("The total fuel required for part 2 is: " + str(total))

if __name__ == '__main__':
    part1()
    part2()
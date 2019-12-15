def adjacentAndNonDecreasing(num):
    adj = False

    for i in range(0, 5):
        if num[i] == num[i+1]:
            adj = True
        if num[i] > num[i+1]:
            return False
    
    return adj

def twoAdjacentAndNonDecreasing(num):
    count = [0] * 10

    for i in range(0, 5):
        if num[i] == num[i+1]:
            count[int(num[i])] += 1
        if num[i] > num[i+1]:
            return False

    return 1 in count


def part1():
    count = 0
    for password in range(147981, 691424):
        if adjacentAndNonDecreasing(str(password)):
            count += 1

    print("The number of different passwords is: " + str(count))

def part2():
    count = 0
    for password in range(147981, 691424):
        if twoAdjacentAndNonDecreasing(str(password)):
            count += 1

    print("The number of different passwords is: " + str(count))


if __name__ == '__main__':
    part1()
    part2()
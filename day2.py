import copy

def part1():
    filepath = "day2.in"
    with open(filepath) as fp:
        arr = fp.readline().strip().split(',')
        arr = [int(x) for x in arr]

        arr[1] = 12
        arr[2] = 2

        posn = 0

        while 1:
            if arr[posn] == 1:
                arr[arr[posn + 3]] = arr[arr[posn + 1]] + arr[arr[posn + 2]]
                posn = posn + 4
            elif arr[posn] == 2:
                arr[arr[posn + 3]] = arr[arr[posn + 1]] * arr[arr[posn + 2]]
                posn = posn + 4
            elif arr[posn] == 99:
                break

        print("The value at position 0 is: " + str(arr[0]))

def part2():
    filepath = "day2.in"
    with open(filepath) as fp:
        orig = fp.readline().strip().split(',')
        orig = [int(x) for x in orig]

    for noun in range(0, 100):
        for verb in range(0, 100):
            
            arr = copy.deepcopy(orig)
            arr[1] = noun
            arr[2] = verb

            posn = 0

            while 1:
                if arr[posn] == 1:
                    arr[arr[posn + 3]] = arr[arr[posn + 1]] + arr[arr[posn + 2]]
                    posn = posn + 4
                elif arr[posn] == 2:
                    arr[arr[posn + 3]] = arr[arr[posn + 1]] * arr[arr[posn + 2]]
                    posn = posn + 4
                elif arr[posn] == 99:
                    break

            if arr[0] == 19690720:
                answer = 100 * noun + verb
                print("100 * noun + verb is: " + str(answer))
                return
        
if __name__ == '__main__':
    part1()
    part2()
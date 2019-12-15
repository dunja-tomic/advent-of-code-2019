
def getValue(mode, imm, pos):
    # position mode
    if mode == 0:
        return int(pos)

    # immediate mode
    elif mode == 1:
        return int(imm)


def part1():
    filepath = "day5.in"
    with open(filepath) as fp:
        arr = fp.readline().strip().split(',')
        arr = [int(x) for x in arr]

        posn = 0

        while 1:
            op = format(arr[posn], '05d')
            print("posn: " + str(posn))
            print("op: " + str(op))

            # mode of 3rd parameter
            A = int(op[0])
            # mode of 2nd param
            B = int(op[1])
            # mode of 1st param
            C = int(op[2])
            # opcode
            DE = int(op[3] + op[4])

            # print(DE)
            # Add
            if DE == 1:
                arr[arr[posn + 3]] = getValue(C, arr[posn + 1], arr[arr[posn + 1]]) + getValue(B, arr[posn + 2], arr[arr[posn + 2]])
                posn += 4
            
            # Multiply
            elif DE == 2:
                arr[arr[posn + 3]] = getValue(C, posn + 1, arr[arr[posn + 1]]) * getValue(B, posn + 2, arr[arr[posn + 2]])
                posn += 4

            # Read input
            elif DE == 3:
                val = input("Input a value: --> ")
                arr[arr[posn + 1]] = int(val)
                posn += 2

            # Output
            elif DE == 4:
                print("Output: " + str(arr[arr[posn + 1]]))
                posn += 2

            elif DE == 99:
                break

if __name__ == '__main__':
    part1()
    # part2()
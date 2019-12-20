import sys

def Intcode(phase, input1):
    filepath = "test.in"
    with open(filepath) as fp:
        arr = fp.readline().strip().split(',')
        arr = [int(x) for x in arr]
        posn = 0

        argCount = 0

        while 1:
            op = format(arr[posn], '05d')

            # Note: 
            # If mode is 0, param is in position mode
            # If mode is 1, param is in immediate mode

            # mode of 3rd parameter
            A = int(op[0])
            # mode of 2nd param
            B = int(op[1])
            # mode of 1st param
            C = int(op[2])
            # opcode
            DE = int(op[3] + op[4])

            # Add
            if DE == 1:
                param1 = arr[arr[posn + 1]] if C == 0 else arr[posn + 1]
                param2 = arr[arr[posn + 2]] if B == 0 else arr[posn + 2]

                arr[arr[posn + 3]] = param1 + param2
                posn += 4
            
            # Multiply
            elif DE == 2:
                param1 = arr[arr[posn + 1]] if C == 0 else arr[posn + 1]
                param2 = arr[arr[posn + 2]] if B == 0 else arr[posn + 2]

                arr[arr[posn + 3]] = param1 * param2
                posn += 4

            # Read input
            elif DE == 3:
                # val = input("Input a value: ")
                # arr[arr[posn + 1]] = int(val)

                # print("Using argument: " + str(input1) if not argCount else str(input2))
                arr[arr[posn + 1]] = int(phase) if not argCount else int(input1)

                # val = sys.argv[argCount]
                # arr[arr[posn + 1]] = int(val)
                argCount += 1
                posn += 2

            # Output
            elif DE == 4:
                param = arr[arr[posn + 1]] if C == 0 else arr[posn + 1]
                # print("Output: " + str(param))

                return param
                
                posn += 2

            # Jump if true
            elif DE == 5:
                param1 = arr[arr[posn + 1]] if C == 0 else arr[posn + 1]
                param2 = arr[arr[posn + 2]] if B == 0 else arr[posn + 2]

                posn = param2 if param1 else posn + 3
            
            # Jump if false
            elif DE == 6:
                param1 = arr[arr[posn + 1]] if C == 0 else arr[posn + 1]
                param2 = arr[arr[posn + 2]] if B == 0 else arr[posn + 2]

                posn = param2 if not param1 else posn + 3

            # Less than
            elif DE == 7:
                param1 = arr[arr[posn + 1]] if C == 0 else arr[posn + 1]
                param2 = arr[arr[posn + 2]] if B == 0 else arr[posn + 2]

                arr[arr[posn + 3]] = param1 < param2
                posn += 4

            # Equals
            elif DE == 8:
                param1 = arr[arr[posn + 1]] if C == 0 else arr[posn + 1]
                param2 = arr[arr[posn + 2]] if B == 0 else arr[posn + 2]

                arr[arr[posn + 3]] = param1 == param2

                posn += 4

            # Terminate program
            elif DE == 99:
                break

            # Terminate program in case of a goof
            else:
                print("Unrecognized opcode: " + str(DE))
                break

def part1():

    highest = 0
    settings = []
    for a in range (0, 5):
        for b in range (0, 5):
            for c in range (0, 5):
                for d in range (0, 5):
                    for e in range (0, 5):
                        ampA = Intcode(a, 0)
                        ampB = Intcode(b, ampA)
                        ampC = Intcode(c, ampB)
                        ampD = Intcode(d, ampC)
                        ampE = Intcode(e, ampD)

                        # print(str(a) + " " + str(b) + " " + str(c) + " " + str(d) + " " + str(e))

                        if ampE > highest:
                            print(str(a) + " " + str(b) + " " + str(c) + " " + str(d) + " " + str(e))
                            highest = ampE
                            settings = [a, b, c, d, e]
    
    print("The highest signal is: " + str(highest))

if __name__ == '__main__':
    part1()

def convert(s: str, numRows: int) -> str:
    lines = [[] for _ in range(numRows)]

    nextChar = 0
    inVertLine = True
    row = 0
    done = False

    while nextChar < len(s) and not done:

        if inVertLine:
            lines[row].append(s[nextChar])
            nextChar += 1

            if nextChar == len(s):
                done = True

            # Reach end of vert line
            if row == numRows - 1:
                if numRows != 1:
                    row -= 1

                    if row > 0:
                        inVertLine = False

            # Not yet end of vert line
            else:
                row += 1

        # In diagonal
        else:
            lines[row].append(s[nextChar])
            nextChar += 1
            row -= 1

            if nextChar == len(s):
                done = True

            if row == 0:
                inVertLine = True

    # Form output
    output_string = ""
    for line in lines:
        print(line)
        for char in line:
            output_string += str(char)

    return output_string


string = convert("ABCDEF", 2)
print(string)

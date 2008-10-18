# Table formatting filter.
# P.C. Shyamshankar <sykora@lucentbeing.com>
# http://lucentbeing.com

# TODO: Get this from optparse
inputDelimiter = ' '
outputDelimiter = ' '


def formatter(lines, inputDelimiter, outputDelimiter) :
    # Assuming all rows are the same length,
    numColumns = len(lines[0])
    widths = []

    # Size of column = size of the largest entry in that column, + 1
    # TODO: Add delimiter support.
    for i in range(numColumns) :
        widths.append(max(len(line[i]) for line in lines))

    formatList = ["%%%ds"] * numColumns

    # There is probably a more efficient way (Time and Space) of doing this.
    output = []
    for i in range(len(lines)) :
        outputLine = formatList[:]
        outputLine = [((s % widths[j]) % lines[i][j])
                  for j, s in enumerate(formatList)]
        output.append(outputDelimiter.join(outputLine))

    return output

def main() :
    # Get input.
    lines = []

    try :
        line = raw_input()
    except EOFError :
        return

    while True:
        lines.append(filter(None, line.split(inputDelimiter)))
        try :
            line = raw_input()
        except EOFError :
            break
    
    formattedLines = formatter(lines, inputDelimiter, outputDelimiter)

    for line in formattedLines :
        print line

if __name__ == '__main__' :
    main()


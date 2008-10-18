# Table formatting filter.
# P.C. Shyamshankar <sykora@lucentbeing.com>
# http://lucentbeing.com

from optparse import OptionParser
from sys import argv

def formatter(lines, inputDelimiter, outputDelimiter) :
    # Split lines based on inputDelimiter.

    lines = [filter(None, line.split(inputDelimiter)) for line in lines]


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

def parseOptions(argv) :
    parser = OptionParser()

    parser.add_option('-i', '--input-delimiter',
                      action = 'store',
                      type = 'string',
                      dest = 'inputDelimiter',
                      default = ' ')

    parser.add_option('-o', '--output-delimiter',
                      action = 'store',
                      type = 'string',
                      dest = 'outputDelimiter',
                      default = ' ')

    options, args = parser.parse_args(argv[1:])

    return options


def main() :
    options = parseOptions(argv)
    # Get input.
    lines = []

    try :
        line = raw_input()
    except EOFError :
        return

    while True:
        lines.append(line)
        try :
            line = raw_input()
        except EOFError :
            break
    
    formattedLines = formatter(lines,
                               options.inputDelimiter,
                               options.outputDelimiter)

    for line in formattedLines :
        print line

if __name__ == '__main__' :
    main()


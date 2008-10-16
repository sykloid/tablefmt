# Table formatting filter.
# P.C. Shyamshankar <sykora@lucentbeing.com>
# http://lucentbeing.com

# TODO: Get this from optparse
inputDelimiter = ' '
outputDelimiter = ' '


line = raw_input()
lines = []

# Get input.
while True:
    lines.append(line.split(inputDelimiter))
    try :
        line = raw_input()
    except EOFError :
        break

# Assuming all rows are the same length,
numColumns = len(lines[0])
widths = []

# Size of column = size of the largest entry in that column, + 1
# TODO: Add delimiter support.
for i in range(numColumns) :
    widths.append(max(len(line[i]) for line in lines))

formatList = ["%%%ds"] * numColumns

# There has got to be a more efficient way (Time and Space) of doing this.
# for i in range(len(lines)) :
#     output = formatList[:]
#     for j in range(numColumns) :
#         output[j] %= widths[j]
#         output[j] %= lines[i][j]
#     print outputDelimiter.join(output)

for i in range(len(lines)) :
    output = formatList[:]
    output = [((s % widths[j]) % lines[i][j])
              for j, s in enumerate(formatList)]
    print outputDelimiter.join(output)


# for i in range(numColumns) :
#     formatString += "%%%ds" % widths[i]

# for i in lines :
#     print formatString % tuple(i)

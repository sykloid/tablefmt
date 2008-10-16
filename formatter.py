# Table formatting filter.
# P.C. Shyamshankar <sykora@lucentbeing.com>
# http://lucentbeing.com

# TODO: Get this from optparse
delimiter = ' '

line = raw_input()
lines = []

# Get input.
while True:
    lines.append(line.split(delimiter))
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
    widths.append(max(len(line[i]) for line in lines) + 1)

formatString = ""
for i in range(numColumns) :
    formatString += "%%%ds" % widths[i]

for i in lines :
    print formatString % tuple(i)

import sys


def template(templateLocation, fillings):
    fileData = open(templateLocation, 'r').read()
    count = 1
    for fill in fillings:
        fileData = fileData.replace('{{'+str(count)+'}}', fill)
        count += 1
    print fileData

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Arguments: [template location] [values]"
        sys.exit()
    templateLocation = sys.argv[1]
    fillings = sys.argv[2:]
    template(templateLocation, fillings)

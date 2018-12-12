import optparse
parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="hatemen", help="changing the mac for this interface")
parser.parse_args()

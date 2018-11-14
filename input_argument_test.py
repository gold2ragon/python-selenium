# from argparse import ArgumentParser
import argparse
# parser = ArgumentParser()
# parser.add_argument("-f", "--file", dest="filename",
#                     help="write report to FILE", metavar="FILE")
# parser.add_argument("-q", "--quiet",
#                     action="store_false", dest="verbose", default=True,
#                     help="don't print status messages to stdout")
#
# args = parser.parse_args()

parser = argparse.ArgumentParser(description='Input year value.')
parser.add_argument('years', metavar='From', type=int, nargs='+',
                    help='interger list')
# parser.add_argument('--end', action='store_const',
#                     help='between two years(default: get the data of first year.)')

years = parser.parse_args().years
if(len(years) == 1):
    print(years[0])
elif (len(years) == 2):
    start = min(years)
    end = max(years)
    print(start, end)
else:
    years.sort()
    for year in years:
        print(year)

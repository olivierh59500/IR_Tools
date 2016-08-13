import re
import sys

def usage():
    """ Print the usage of the softare. """
    print("My Incident Tool knife.")
    print()
    print("Usage :irtools target_file. ")
    print("Target file must be a text file.")
    print("Search for american phone number")


def open_file(ifile):
    """ Load the file thad need to be investigated. """
    print("* Truing to open File" + ifile  )
    try:
        file = open(ifile,"r")
    except:
        print("Didn't work")
        exit()
    print("** Loading was successfull \n")
    return file


def search_for(ifile):
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.findall(opened_file.read())
    if mo:
        for elem in mo:
            print(elem)
    else:
        print("****Pattern not found")

if not len(sys.argv[1:]):
    usage()
else:
    invest_file = sys.argv[1]
    opened_file = open_file(invest_file)
    print("***Search for the associated regex")
    search_for(opened_file)

import re
import sys
import getopt

def usage():
    """ Print the usage of the softare. """
    print("My Incident Tool knife.")
    print("")
    print("Usage :irtools -f target_file.")
    print("-f or --file, file that you need to search into")
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
    full_text = file.read()
    file.close()
    return full_text


def search_for_phone(inv_string):
#    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    phoneNumRegex = re.compile(r'''((\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))?)''', re.VERBOSE)
    mo = phoneNumRegex.findall(inv_string)
    if mo:
        for elem in mo:
            print(elem[0])
    else:
        print("****Pattern not found")

def version():
    '''Print the version of the software'''
    print("Version of this software is 0.1")
    sys.exit(0)

def main():
    ''' The main function of the program '''
    global invest_file 
    global opened_file 
    global file_available
    file_available = False

    if not len(sys.argv[1:]):
        usage()
        exit()
    try:
        opts, args = getopt.getopt(sys.argv[1:],"f:vep",["file","version","email","phone"])
#    except getopt.GetopError as err:
#        print(str(err))
#        usage()
    except:
        usage()
        sys.exit()

    for o,v in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-f", "--file"):
            invest_file = v
            file_available = True
        elif o in ("-v", "--version"):
            version()
        elif o in ("-e", "--email"):
            print("Checking for the emailS")
        elif o in ("-p", "--phone"):
            print("Checking for the phoneS")
        else:
            file_available = False
            assert False, "unhandled shit"

    if file_available == False:
        print("No file was uploaded")
        exit()
    opened_file = open_file(invest_file)
    print("***Search for the associated regex")
    search_for_phone(opened_file)

main()

import re
import sys
import getopt

def usage():
    """ Print the usage of the softare. """
    print("My Incident Tool knife.")
    print("")
    print("Usage :irtools -f target_file.")
    print("-f or --file, file that you need to search into")
    print("-e or --email, check for emails in the file")
    print("-p or --phone, check for US phone number in the file")
    print("-v or --version, check the version of the software")
    print("Target file must be a text file.")
    print("Search for american phone number")


def open_file(ifile):
    """ Load the file thad need to be investigated. """
    print("* Trying to open File" + ifile  )
    try:
        file = open(ifile,"r")
    except:
        print("Didn't work")
        exit()
    print("** Loading was successfull \n")
    full_text = file.read()
    file.close()
    return full_text

def search_for_url(inv_string):
    '''Function that search for a url '''
    urlRegex = re.compile(r'''(https?\:\/\/[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,})''', re.VERBOSE)
    mo = urlRegex.findall(inv_string)
    if mo:
        for elem in mo:
            print elem
           # print(elem[0]) ------- Don't understand why the pattern work in groups :(
    else:
        print("****** Url Pattern not found")

def search_for_ipv4(inv_string):
    ''' function that search for an ipv4 (valid)'''
    ipv4Regex = re.compile(r'''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))''',re.VERBOSE)
    mo = ipv4Regex.findall(inv_string)
    if mo:
        for elem in mo:
            print(elem[0])
    else:
        print("****ipv4 pattern not found")


def search_for_email(inv_string):
    '''function that search for an email string'''
    emailRegex = re.compile(r'''([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]+))''', re.VERBOSE)
    mo = emailRegex.findall(inv_string)
    if mo:
        for elem in mo:
            print(elem[0])
    else:
        print("******Pattern not found")

def search_for_phone(inv_string):
    '''function that search for an American phone number'''
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
    # global variables
    global invest_file 
    global opened_file 
    global file_available
    global phone_selected
    global email_selected
    # initialization of variables
    email_selected = False
    phone_selected = False
    file_available = False

    if not len(sys.argv[1:]):
        usage()
        exit()
    try:
        opts, args = getopt.getopt(sys.argv[1:],"f:vep",["file","version","email","phone"])
#    except getopt.GetopError as err:   #This is not working :(
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
            email_selected = True
        elif o in ("-p", "--phone"):
            print("Checking for the phoneS")
            phone_selected = True
        else:
            file_available = False
            assert False, "unhandled shit"

    if file_available == False:
        print("No file was uploaded")
        exit()
    opened_file = open_file(invest_file)
    print("***Search for the associated regex")
    print email_selected
    print phone_selected
    search_for_phone(opened_file)
    search_for_email(opened_file)
    search_for_url(opened_file)
    search_for_ipv4(opened_file)

main()

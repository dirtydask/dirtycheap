#!/usr/bin/env python2
# This utility is used to provide a centralized management interface for Security Onion
'''
Imports
'''
import sys
import os
if sys.platform.startswith('win'):
    R, B, Y, C, W = '\033[1;31m', '\033[1;37m', '\033[93m', '\033[1;30m', '\033[0m'
    try:
        import win_unicode_console
        import colorama
        win_unicode_console.enable()
        colorama.init()
    except:
        print('[+] Error: Coloring libraries not installed')
        R, B, Y, C, W = '', '', '', '', ''
else:
    R, B, Y, C, W = '\033[1;31m', '\033[1;37m', '\033[93m', '\033[1;30m', '\033[0m'

'''
Functions
'''


def header():
    print('''%s
  ____ ___ ____ _______   __   ____ _   _ _____    _    ____
 |  _ \_ _|  _ \_   _\ \ / /  / ___| | | | ____|  / \  |  _ \\
 | | | | || |_) || |  \ V /  | |   | |_| |  _|   / _ \ | |_) |
 | |_| | ||  _ < | |   | |   | |___|  _  | |___ / ___ \|  __/
 |____/___|_| \_\|_|   |_|    \____|_| |_|_____/_/   \_\_|

         %sBy https://github.com/dirty_dask - @dirty_dask%s    >|%s  %s
        ''' % (R, B, R, C, W))


def read(conf):

    print("Opening " + conf + " contents: \r\n")
    f = open("/workspace/theia/Projects/pulledpork/" + conf + ".conf", "r")
    if f.mode == "r":
        contents = f.read()
        print(contents + "\n")

    raw_input("Press Enter to coninue...")

def append(conf, sid):

    f = open("/workspace/theia/Projects/pulledpork/" + conf + ".conf", "a+")
    f.write("\n")
    f.write(sid)
    f.close()


def remove(conf, sid):
    '''
    f = open("/workspace/theia/Projects/pulledpork/" + conf + ".conf", "r")
    lines = f.readlines()
    f.close()
    f = open("/workspace/theia/Projects/pulledpork/" + conf + ".conf", "w+")
    for line in lines:
        if line != sid:
            f.write(line)
    f.close()
    '''

    with open("/workspace/theia/Projects/pulledpork/" + conf + ".conf", 'r+') as f:
        t = f.read()
        f.seek(0)
        for line in t.split('\n'):
            if line != sid:
                f.write(line + '\n')
        f.truncate()


def pulledporkhelp():
    os.system('clear')
    print(
        '''
=========================================================================================================================
      _____ ____
     `----,\\    )
      `--==\\\\  /
       `--==\\\\/
     .-~~~~-.Y|\\\\_                Copyright (C) 2009-2017 JJ Cummings, Michael Shirk
  \@_/        /  66\\_                  and the PulledPork Team!
    |    \\   \\   _(\")
     \\   /-| ||'--'                Rules give me wings!
      \\_\\  \\_\\\\
=========================================================================================================================
Pulledpork runs rule modification (enable, drop, disable, modify) in that order by default.

    1: enable

    2: drop

    3: disable

This means that disable rules will always take precedence. Thusly if you specify the same gid:sid in enable and disable configuration files, then that sid will be disabled. Keep this in mind for ranges also! However, you can specify a different order using the state_order keyword in the master config file.")
=========================================================================================================================
    ''')
    raw_input(" Press Enter to continue...")


'''
Menus
'''
def errorMenu():
    os.system('clear')
    header()
    print(" Please try again...")
    print("")
    raw_input(" Press Enter to continue...")
    mainmenu()


def mainmenu():
    os.system('clear')
    header()
    title = "Choose an option below:"
    print("")
    print("=================== " + title +" ===================")
    print("")
    print(" [1] Rules")
    print(" [2] Settings")
    print(" [3] Save changes")
    print(" [Q] Exit")
    print("")

    user_input = raw_input(" Please make a selection: ")

    if user_input == '1':
        mgmtmenu()
    elif user_input == '2':
        readmenu()
    elif user_input == '3':
        print("\n [*] Executing {sudo salt '*' cmd.run 'rule-update'} on all sensors \n")
        # os.system("sudo salt '*' cmd.run 'rule-update'")
        raw_input(" Press Enter to continue...\n")
        mainmenu()
    elif user_input in {'Q','q'}:
        print("\n Exiting...\n")
        exit()
    else:
        errorMenu()

def readmenu():
    os.system('clear')
    header()
    title = "Choose an option below:"
    print("")
    print("=================== " + title +" ===================")
    print("")
    print(" [1] disablesid.conf")
    print(" [2] dropsid.conf")
    print(" [3] enablesid.conf")
    print(" [4] modifysid.conf")
    print(" [5] pulledpork.conf")
    print(" [Q] Return to main menu")
    print("")
    read_input = raw_input("Please make a selection: ")
    print("")

    if read_input == '1':
        read('disablesid')
        readmenu()
    elif read_input == '2':
        read('dropsid')
        readmenu()
    elif read_input == '3':
        read('enablesid')
        readmenu()
    elif read_input == '4':
        read('modifysid')
        readmenu()
    elif read_input == '5':
        read('pulledpork')
        readmenu()
    elif read_input in {'Q','q'}:
        mainmenu()
    else:
        errorMenu()


def mgmtmenu():
    os.system('clear')
    header()
    title = "Choose an option below:"
    print("")
    print("=================== " + title +" ===================")
    print("")
    print(" [1] Disable Rule")
    print(" [2] Modify Rule")
    print(" [3] Enable Rule")
    print(" [4] Remove Rule")
    print(" [6] Help")
    print(" [Q] Return to main menu")
    print("")
    print(" TIP: Menu is ordered by precedence")
    print("")

    mgmt_input = raw_input(" Please make a selection: ")
    print("")

    if mgmt_input == '1':
        sid = raw_input(" Please input gid:sid of rule (e.x. '1:4444'): ")
        append('disablesid', sid)
        print("")
        print(" [*] Inserted " + sid + " in disablesid.conf")
        print("")
        raw_input(" Press Enter to continue...")
        mgmtmenu()

    elif mgmt_input == '2':
        sid = raw_input(" Please input gid:sid of rule (e.x. '1:4444'): ")
        print("")
        print(" [*] Inserted " + sid + "in dropsid.conf")
        raw_input(" Press Enter to continue...")
        print("")

    elif mgmt_input == '4':
        sid = raw_input(" Please input gid:sid of rule (e.x. '1:4444'): ")
        conf = raw_input(
            " Please select .conf file (disablesid/dropsid/modifysid/enablesid): ")
        if conf not in {"disablesid","dropsid","modifysid","enablesid"}:
            errorMenu()
        remove(conf, sid)
        print("")
        print(" [*] Removed " + sid + " from " + conf +".conf")
        print("")
        raw_input(" Press Enter to continue...")
        mgmtmenu()

    elif mgmt_input == '6':
        pulledporkhelp()
        mgmtmenu()

    elif mgmt_input in {'Q','q'}:
        mainmenu()

    else:
        errorMenu()


mainmenu()

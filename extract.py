import openpyxl
from openpyxl.cell import get_column_letter, column_index_from_string
import os
import re
import pandas as pd
from itertools import ifilterfalse

def printlist(alist):
    for item in alist:
        print '\n'.join(mylist)

def match_all(pattern,name):
    ###pattern is a list of strings
    name = name.lower()
    for part in pattern:
        if all(part in name for part in pattern) and ('~$' not in name) :
            match_all = True
        else:
            match_all = False
    return match_all


def find(pattern, path):
    ##return a list of filedir and filename that matches patter in path
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if match_all(pattern,name):
                print "found match", name
                path_name = (os.path.join(root, name),name)
                result.append(path_name)
    if result == []:
        print "no match"
    return result


def find_inlist(astring, alist):
    ##find the first item in the list that matches the string and return
    m = -1
    stringName2 = str()
    for i in alist:
        n = 0
        m = m + 1
        if astring in i:
            n = 1
            stringName2 = alist[m]
        if n == 1:
            break
        return (stringName2,m)


def shorten_list_byone(astring, atuplelist):
    ##use key words to shorted the list (exclude names that have key words)
    clipboard = []
    for item1,item2 in atuplelist:
        if astring not in item2:
            clipboard.append((item1,item2))
    return clipboard



#########      SEARCHING PHASE     ###########################
#### FIND ALL matched file using user defined search criteria
#### Here we only search for .xlsx files
##############################################################
def search_list():

    while True:
        path  = raw_input("Enter the path of your file: ")
        if os.path.exists(path) == False:
            print "Duh, this path does not exist"
            print '\n'*2
            continue
        else:
            print("Hooray this path exists!")
            print '\n'*2
            break

    search_pattern = raw_input("Please enter search criteria seperated by space: ").split()
    #find the full path and file name that matches the pattern
    listofmatched = find(search_pattern, path)

    #restart search if not satisfied
    while True:
        restart_search = str(raw_input('run search agin? (y/n)'))
        if restart_search not in ('y','n'):
            print "Invalid Input"
            print '\n'*2
            continue
        if restart_search == 'y':
            search_list()
        if restart_search == 'n':
            print "current search results will be used"
            print '\n'*2
            break

    #short the list by excluding some of
    while True:
        shorten_list = raw_input('shorten list? (y/n)')
        if shorten_list not in ('y','n'):
            print "Invalid Input"
            print '\n'*2
            continue
        if shorten_list == 'y':
            exclude = raw_input('Please enter words you \'d like to exclude: ').split()
            for i in exclude:
                listofmatched = shorten_list_byone(i,listofmatched)
            for j in [x[1] for x in listofmatched]:
                print j
            print '\n'*2
        if shorten_list == "n":
            print "current search results will be used"
            print '\n'*2
            break

    return(listofmatched)



    #trim the list to most recent files

########### END of SEARCHING PHASE ###############
##########@ OUTPUT: list of matched #############

listofmatched = search_list()



########## Extraction Phase  ###################################
##########@ INPUT: list of excel file where extraction is needed
##########@ OUTPUT: table of output ############################
print "###########Begin Processing the Files################"

for file_dir,file_name in listofmatched:
    try:

        print "OPENING", file_name
        print "Processing the txt file in", file_dir
        data = pd.read_csv(file_dir, sep="\t", skiprows = 2, header = 2, engine = 'python')

        header = list(data)

        ##find the index and n_total header
        index_coln = find_inlist('index',header)
        n_total_coln = find_inlist('n_total',header)

        #return the first row and the cells
        print data[0:1]
        print "\n"*3

    except:
        print "OPENING", file_name
        print "Processing the txt file in", file_dir
        data = pd.read_csv(file_dir, sep="\t", skiprows = 1, header = 1, engine = 'python')

        header = list(data)

        ##find the index and n_total header
        index_coln = find_inlist('index',header)
        n_total_coln = find_inlist('n_total',header)

        #return the first row and the cells
        print data[0:1]
        print "\n"*3

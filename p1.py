import os
import sys
import csv


class ArgumentError(Exception): pass


class NoFileError(Exception): pass


class NoEntryError(Exception): pass


class DuplicateError(Exception): pass


def create_phonebook(phonebook_name):
    """Create a new phonebook.
    Args:
        phonebook_name (str): the name of the phonebook to create
    """
    filename = '%s.csv' % phonebook_name
    if os.path.exists(filename):
        print ("That phonebook already exists!")
        quit()
    with open(filename, 'w') as f:
        print("phonebook created...")
        pass


def add_entry(first_name, last_name, number, city_name):
    """Add a new name and number to the given phonebook.
    Args:
        name (str): name of the entry to add
        number (str): phone number of the entry to add
        phonebook_name (str): name of the phonebook
    """
    user_details = [[first_name, last_name, number, city_name]]
    filename = 'phone_dataset.csv'
    with open(filename, 'a') as f:
        writer = csv.writer(f)
        writer.writerows(user_details)
        print("user details added....")

def lookup_name():
    """Look up an entry by name in the given phonebook.
    Args:
        name (str): name to look up
        phonebook_name (str): name of the phonebook
    """
    lastname = list()
    query = 'query.csv'
    with open(query, 'r') as q:
        queryfile = csv.reader(q)
        querydata = list(queryfile)
        querylength = len(querydata)

    filename = 'phone_dataset.csv'
    with open(filename, 'r') as f:
        readfile = csv.reader(f)
        data = list(readfile)
        length = len(data)

    
        


    for i in range(querylength):
        print("matches for :"+querydata[i][0])
        for j in range(length):
            if(querydata[i][0] == data[j][1]):
                result = [data[j]]
                filename = 'result.csv'
                with open(filename, 'a') as r:
                    writer = csv.writer(r)
                    writer.writerows(result)
                print(data[j])
                
            


if __name__ == '__main__':
    args = sys.argv[:]
    script = args.pop(0)    # name of script is first arg
    if not args:
        print ("Command required")
        quit()
    command = args.pop(0)   # the next arg will be the main command

    if command == 'create':
        if len(args) != 1:
            print ("Phonebook name required")
            quit()
        phonebook_name = args.pop(0)
        create_phonebook(phonebook_name)

    elif command == 'add':
        if len(args) != 4:
            print ("name, number are cityname required")
            quit()
        first_name, last_name, number,city_name = args
        add_entry(first_name, last_name, number, city_name)

    elif command == 'search':
        lookup_name()
    else:
        print ("Invalid command")
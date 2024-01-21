#!/usr/bin/env python

# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys
import csv

#
# Constants
#


def main(argv):
    if len(argv) != 3:
        print("Usage: read_file.py <file name>")
        sys.exit(1)

    namedata_filename = argv[1]
    #set name counter equal to the argument that would represent the number of names to read.
    name_counter = int(argv[2])


    try:
        namedata_fh = open(namedata_filename, encoding="utf-8-sig")
    except IOError as err:
        print("Unable to open names file '{}' : {}".format(namedata_filename, err), file=sys.stderr)
        sys.exit(1)

    namedata_reader = csv.reader(namedata_fh)

    #variables to rep each element.
    line_number = 0
    top_female_names = []
    top_male_names = []
    total_female_population = 0
    total_male_population = 0

    #for loops that reads the data file with the data reader.
    #each variable is given the value of the arguement that the file corresponds to.
    for row_data_fields in namedata_reader:
        given_name = row_data_fields[0]
        sex = row_data_fields[1]
        number_of_people = int(row_data_fields[2])

        #if sex = female then we will append the name sex and number of people onto the list of 
        #females then add the number of people in that row to the total female population
        #second line will take the number of people in that given row that was parsed and add to the total
        #female population that will be printed out in the end. Same thing for if it is a M.

        if sex == 'F' and len(top_female_names) < name_counter:
            top_female_names.append((given_name, sex, number_of_people))
            total_female_population += number_of_people

        elif sex == 'M' and len(top_male_names) < name_counter:
            top_male_names.append((given_name, sex, number_of_people))
            total_male_population += number_of_people

        #adds one to our line number to go to each next parse.
        line_number += 1

    
    # Print top female names
    for name, sex2, count in top_female_names:
        print("%s %s (%d)" % (name, sex2, count))
    print("Total females in top 5 names: {}".format(total_female_population))

    # Print top male names
    for name, sex2, count in top_male_names:
        print("%s %s (%d)" % (name, sex2, count))
    print("Total males in top 5 names: {}".format(total_male_population))

    # Total people
    print("Total people in top 5 names: {}".format(total_female_population + total_male_population))

main(sys.argv)

# Uses Heath Nutrition and Population statistics,
# stored in the file HNP_Data.csv.gz,
# assumed to be located in the working directory.
# Prompts the user for an Indicator Name. If it exists and is associated with
# a numerical value for some countries or categories, for some the years 1960-2015,
# then finds out the maximum value, and outputs:
# - that value;
# - the years when that value was reached, from oldest to more recents years;
# - for each such year, the countries or categories for which that value was reached,
#   listed in lexicographic order.
# 
# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv
import gzip


filename = 'HNP_Data.csv.gz'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

indicator_of_interest = input('Enter an Indicator Name: ')

first_year = 1960
number_of_years = 56
max_value = None
countries_for_max_value_per_year = {}

with gzip.open(filename) as csvfile:
    file = csv.reader(line.decode('utf8').replace('\0', '') for line in csvfile)
    for i in file:#first choose the line in the file
        if not i:#except empty line in order to protect progress operate normally
            continue
        if i[2]!=indicator_of_interest:#find the true indicator_of_interest
            continue
        elif indicator_of_interest in i[2]:
            for e in range(4,number_of_years+4):#in the true indicator_of_interest,find related data in the different column
                if i[e] is '':#if the column is empty,continue loop until find all the data
                    continue
                data=eval(i[e])
                if max_value is None:#first give a value to max_value if it is None
                    max_value = data
                elif data<max_value:#except small data
                    continue
                elif data>max_value:#when data is larger, choose this to replace later max_value
                    max_value=data
                    countries_for_max_value_per_year={}
                    countries_for_max_value_per_year.setdefault(e-4+first_year,list()).append(i[0])
                elif data==max_value:#especially,choose the data when the data==max_value
                    countries_for_max_value_per_year.setdefault(e-4+first_year,list()).append(i[0])
                               
             
                      
                        
                    
                    
                
                
                    
                
            
            
    

        
            
if max_value is None:
    print('Sorry, either the indicator of interest does not exist or it has no data.')
else:
    print('The maximum value is:', max_value)
    print('It was reached in these years, for these countries or categories:')
    print('\n'.join(f'    {year}: {countries_for_max_value_per_year[year]}'
                                  for year in sorted(countries_for_max_value_per_year)
                   )
         )

# write your Python code here according to the instructions

## import the csv module
import csv

# open data into csv module's DictReader
def get_csv_data(filepath):
    l = [] # create list to store
    with open (filepath, 'r') as f: 
        input_file = csv.DictReader(f)
        for rows in input_file: 
            l.append(rows)
    return l

# remove NULL values
def remove_rows_with_null_valued_fields(data):
    l = []
    for row in data: 
        if 'NULL' not in row.values() :
            l.append(row)
    return l

# remove invlid handles       
def remove_rows_with_invalid_handles(data):
    import re # import regular expression
    l = [] # create a list
    for row in data: 
        if not re.search('[^0-9a-zA-Z]+', row['handle']) :
            l.append(row)
    return l
# remove any rows with a value in a given affinity category id field greater than to the supplied threshold.
def remove_rows_over_affinity_id_level(data, affinity_type, threshold):
    l = []
    for row in data:
        value = int(row[affinity_type])
        if value > threshold:
            continue
        l.append(row)
    return l

# update email domain
def replace_email_domain(data, old_domain, new_domain):
    l = []
    for row in data:
        email = row['email']
        if old_domain in email:
            row['email'].replace(old_domain, new_domain)
       
        l.append(row)
    return l

# save the data into the specified file
def save_csv_data(data, filepath):
    headers = data[0].keys()
    with open(filepath, 'w', newline='')  as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerows(data)

# get average and median of the affinity category id
def get_average_and_median_affinity_id(data, affinity_type):
    num = 0
    total = 0
    all = []
    for row in data:
        value = float(row[affinity_type])
        all.append(value)
        total += value
        # print(value)
    num = len(all)
    avg = total / num
    all.sort()
    if num % 2 == 0:
        h = int(num /2)
        median = (all[h] + all[h+1] )/ 2.0
    else:
        h = int(num /2 + 1)
        median = all[h]
    return avg,median

#################################################
## Do not modify the code below this line      ##
## except to comment out any function calls    ##
## that you do not wish to test at the moment  ##
#################################################

def main():
    ## use the functions defined above to complete munging of the data file

    # get the data from the file
    data = get_csv_data('data/users.csv')

    # munge it
    data = remove_rows_with_null_valued_fields(data)
    data = remove_rows_with_invalid_handles(data)
    data = remove_rows_over_affinity_id_level(data, 'tech_gadget_affinity_category_id', 10)
    data = replace_email_domain(data, '@amazon.de', '@amazon.com')
    # save to the new csv file
    save_csv_data(data, 'data/users_clean.csv')

    # print the average and median affinity level for real food
    avg, median = get_average_and_median_affinity_id(data, 'tech_gadget_affinity_category_id')
    print('The average affinity id for tech gadget is: {}.'.format(avg))
    print('The median affinity id for tech gadget is: {}.'.format(median))

if __name__ == "__main__":
    main()
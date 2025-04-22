# check if all elements in a list is unique or not
# if there is a duplicate then return the duplicate value

list_values = ['water', 'soda-water', 'mint-water', 'rasna-water', 'soda-water']

for val in list_values:
    value_count = list_values.count(val)
    if(value_count == 2):
        print('duplicate value:', val)
        break
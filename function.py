# user intertools
import itertools
#the global var
var_sum = 12

#fucntion for read file in utils folder
def read_file():
    try:
        with open('utils/list.txt') as f:
            for line in f:
                #read line by line and convert to list
                contents_line = line.strip().split(',')
                #convert in integers the items list
                contents_line_int = [eval(i) for i in contents_line]
                print(contents_line_int)
                #get print_pairs_numbers function
                print_pairs_numbers(contents_line_int)

    except Exception as e:
        print('error message in function -> read_file: '+ str(e))

#function for search pairs number that sum equals global var -> var_sum
def print_pairs_numbers(mylist):
    try:
        #loop for print the number that sum equals global var -> var_sum
        for x,y in itertools.combinations(list(set(mylist)), 2):
            if (x + y) == var_sum:
                print(x , y)

    except Exception as e:
        print('error message in function -> print_pairs_numbers: '+ str(e))

#execute function
read_file()
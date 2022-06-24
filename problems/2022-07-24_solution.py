# Takes array and builds out new ones, removing the current index i
def build_list_of_list(given_list):
    solution = []
    
    for i in given_list:
        temp = []
        cur_index = given_list.index(i)
        
        for j in given_list:
            loop_index = given_list.index(j)

            result = 1
            if cur_index != loop_index:
                temp.append(j)
            
        solution.append(temp)

    return(solution)

# Takes in a lit of list and iterates through each to get the product of all numbers
# It then builds a list with solution to each lists answer.
def multiply_list(list_of_list) :
    solution = []
    for i_list in list_of_list:
        result = 1
        for x in i_list:
            result = result * x
        solution.append(result)
    return(solution)

# Daily Problem 2022-07-24
if __name__ == '__main__':
    given_list = [1,2,3,4,5]
    list_of_list = build_list_of_list(given_list)
    print(multiply_list(list_of_list))

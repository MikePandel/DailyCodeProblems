import random

# Get Random Test - Randomly gen list & k vars
def random_test(list_length):
    random_k = random.randint(1,20)
    random_list = []
    i = 0
    while i < list_length:
        random_list.append(random.randint(1,10))
        i = i + 1
    
    return(random_k,random_list)

# Process Problem
def process_list(list,k):
    print('\t' + 'LIST: {} K: {}'.format(list,k))
    
    for l1 in list:
        for l2 in list:
            if (l1 + l2 == k):
                return('Solution: {} + {} = {}'.format(l1,l2,k))
        return('{}, not found by adding two # from {}'.format(k,list))

# Daily Problem 2022-07-23
if __name__ == '__main__':
    random_k, random_list = random_test(10)
    example_list_01 = [10,15,3,7]
    example_k_01 = 17
    
    print('Selected Test:')
    print('\t' + process_list(example_list_01,example_k_01))
    
    print('Random Test:')
    print('\t' + process_list(random_list,random_k))

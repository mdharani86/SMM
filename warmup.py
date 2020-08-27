from itertools import combinations

Node = {1:[3,4,5,6,8],2:[3,4,5,7,8],3:[1,2,7,4],4:[3,2,1,8],5:[1,2,6],6:[1,5],7:[2,3],8:[1,2,4]}

list = [1,2,3,4,5,6,7,8]
active = combinations(list,3)
set_cnt = 0
for active_tuple in active:
    set_cnt +=1
    active_list = [item for item in active_tuple]
    print(f'set count:{set_cnt}')
    print(f'active_set: {active_list}')
    inactive_list = [item for item in list if item not in active_list]
    print(f'inactive_list: {inactive_list}')
    print(f'Connections: {Node}')

    for key in Node.keys():
        count_active = 0
        count_inactive = 0
        for list_value in Node.get(key):
            if list_value in active_list:
                count_active +=1
            else:
                count_inactive +=1
        if key in  inactive_list:
            ratio = count_active/(count_active + count_inactive)
            print(f'Inactive Node#: {key}, active neighbours count:{count_active}, inactive neighbours count:{count_inactive}, active percent:{ratio}')
    print()


Node = {1:[3,4,5,6,8],2:[3,4,5,7,8],3:[1,2,7,4],4:[3,2,1,8],5:[1,2,6],6:[1,5],7:[2,3],8:[1,2,4]}

active_set = {6, 7, 8}
inactive_set = {1, 2, 3, 4, 5}
print('Original Sets:')
print(f'active set: {active_set}')
print(f'inactive_set: {inactive_set}')
print(f'connectivity: {Node}')
for key in Node.keys():
    count_active = 0
    count_inactive = 0
    ratio_list = []

    for list_value in Node.get(key):
        if list_value in active_set:
            count_active += 1
        else:
            count_inactive += 1
    if key in inactive_set:
        ratio = count_active / (count_active + count_inactive)
        ratio_list.append(ratio)
        # print()
        print(f'Inactive Node: {key}, active nodes connected:{count_active}, inactive nodes connected:{count_inactive}, percent active:{ratio}')
        # print()

set_cnt = 0
for i in active_set:
    for j in inactive_set:
        # swapping i and j between active and inactive sets
        temp_active = active_set.copy()
        temp_inactive = inactive_set.copy()
        temp_i = i
        temp_j = j
        temp_active.remove(temp_i)
        temp_inactive.remove(temp_j)
        temp_active.add(temp_j)
        temp_inactive.add(temp_i)
        set_cnt +=1
        print()
        print(f'Swapped set {set_cnt}, Swapped Nodes: {i},{j}')
        print(temp_active)
        print(temp_inactive)
        print(Node)
        print()
        ratio_list = []

        for key in Node.keys():
            count_active = 0
            count_inactive = 0

            for list_value in Node.get(key):
                if list_value in temp_active:
                    count_active +=1
                else:
                    count_inactive +=1
            if key in temp_inactive:
                ratio = count_active/(count_active + count_inactive)
                print(f'Inactive Node: {key}, active Nodes connected:{count_active}, inactive active nodes connected:{count_inactive}, active percent:{ratio}')

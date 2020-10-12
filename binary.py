def binary_search(data,search):
    print(data)
    if len(data) ==1 and search == data[0]:
        return True
    if len(data) ==1 and search != data[0]:
        return False
    if len(data) == 0:
        return False

    medium = len(data)// 2
    if search == data[medium]:
        return True
    else :
        if search > data[medium]:
            return binary_search(data[medium:],search)
        else :
            return binary_search(data[:medium],search)

import random
data_list = random.sample(range(100),10)
data_list.sort()
print(data_list)

data_list = [24, 30, 32, 35, 38, 48, 65, 76, 78, 81]
print(binary_search(data_list,30))
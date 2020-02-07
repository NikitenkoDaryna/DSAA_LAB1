import random
def print_array(list):
        print(list)
def sort(list,len):
    flag=False
    #n=len
    for i in range(len):
        flag=True
        for j in range(0,len-i-1):
            if list[j] > list[j + 1]:
             list[j],list[j+1]=list[j+1],list[j]
             flag=False
        if flag:break
    return list
def generate_rnd_list(length):
    items=[random.randint(-10000,10000) for i in range(length)]
    return items

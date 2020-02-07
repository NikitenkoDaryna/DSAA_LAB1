import functions.funcs
list=[]
length=0
length=int(input("Input length of your array:\n"))
list=functions.funcs.generate_rnd_list(length)
functions.funcs.sort(list,length)
functions.funcs.print_array(list)






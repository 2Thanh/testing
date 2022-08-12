lis = input().split() #List with strings
new_lis = list(map(int,lis)) #New list with integers

set_list = set(new_lis) #create a set
set_list.add(1) #If you add a value available in list => it'll not change
set_list.add((2,3)) #set contain any data type
# set_list.update("1","2","Hello Wall Street",{8, 9})
set_list.remove(10) # discard vs remove same function 
print(set_list)

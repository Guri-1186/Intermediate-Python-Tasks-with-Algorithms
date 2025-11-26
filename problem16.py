#write a program o count any item from nested list
myList = [[1,2,3],[1,1,1]]

def get_item(myList):
    item = int(input("get an item :"))
    result = sum(i.count(item) for i in myList)
    return result


print(get_item(myList))



   
        







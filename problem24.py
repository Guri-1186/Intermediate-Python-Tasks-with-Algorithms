#write a python program to filter odd numbers from a given dictionary keys.display only those values which have odd keys.        
odd_num = {1:"blue", 2:"black", 3:"green", 4:"yellow"}
def get_odd_keys(odd_num):
   for key,value in odd_num.items():
       if key%2!= 0:
           print(value)    
            
get_odd_keys(odd_num) 
    
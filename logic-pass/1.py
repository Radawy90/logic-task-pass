


# create a method that will remove any given character from a string ?

input_str =str(input( "Enter any word")) 
  
result_str = "" 
   
for i in range(0, len(input_str)): 
    if i != 3: 
        result_str = result_str + input_str[i]   
print ("String after removal of character : " + result_str)




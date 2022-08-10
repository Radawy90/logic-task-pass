# write s function that count how many the given character repeated in a given string ? 

string1=str(input('Enter any Sentence'))
def rep(string1):
   for i in range(0, len(string1)):  
    count = 1;  
    for j in range(i+1, len(string1)):  
        if(string1[i] == string1[j] and string1[i] != ' '):  
            count = count + 1;  
            string1 = string1[:j] + '0' + string1[j+1:];  
    
    if(count > 1 and string1[i] != '0'):  
        print(string1[i]," - ",count)

rep(string1)




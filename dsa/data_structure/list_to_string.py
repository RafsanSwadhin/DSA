def convert_list(c_list):  
  str=''  
  for i in c_list:  
    str=str+i  
  return str  
  
c_list=['P','p','t','h','o','n','a','t','J','T','P'] 
c_string=convert_list(c_list)  
print(c_string) 
print(type(c_string))
def convert_tuple(c_tuple):  
  str=''  
  for i in c_tuple:  
    str=str+i  
  return str  
  
c_tuple=('P','y','t','h','o','n','a','t','J','T','P')  
c_string=convert_tuple(c_tuple)  
print(c_string) 
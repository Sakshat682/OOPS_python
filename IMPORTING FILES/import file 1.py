import calculations as cal   # WE IMPORT THE CALCLATIONS.PY FILE
                             # CAL is the variable name we assigned to the file object 

#=======================================================================================================================================
##   TO USE VARIABLES AND FUNCTIONS OF THE FILE WE FIRST HAVE TO WRITE THE VARIABLE NAME STORING THE FILE OBJECT
##   FOLLOWED BY '.' AND THE FUNCTIONS OR THE VARIABLE WHICH WE WANT TO USE 
#=======================================================================================================================================

num = 20

print(f'The value of num is {num}')  #this should print 20
print(f'The value of cal.num is {cal.num}') #this should print 10


print(cal.add(4,5))          # WE CALL ADD METHOD OF THE FILE OBJECT           
print(cal.mul(4,5))          # WE CALL MUL METHOD OF THE FILE OBJECT 
print(cal.sub(4,5))          # WE CALL SUB METHOD OF THE FILE OBJECT 


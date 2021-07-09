#calling a python file from another python file
from lms_child import lms_engine as l1
#from MasterDataClass import master as m2
import sys
import os
# #---------------------Directly entering customer details-------------------------------------
# l_cust_name ='bbb'
# l_cust_creditscore = 340
# l_cust_requestedloanamount = 35000

##----------------------Entering customer details via command line--------------------------------
l_UserInput1 = input("Enter name and press enter: ")
l_cust_name = l_UserInput1
#greetings(l_cust_name)
l_UserInput2 = input("Enter required loan amount and press enter: ")
l_cust_requestedloanamount = int(l_UserInput2)
l_UserInput3 = input("Enter credit score and press enter: ")
l_cust_creditscore = int(l_UserInput3)

if l_cust_creditscore < 0:
    print('Error : Invalid Credit score')
    
elif l_cust_creditscore > 400:   
    print('Error : Maximum allowed credit score is 400')
    
else:
    lms_obj = l1(l_cust_name, l_cust_creditscore, l_cust_requestedloanamount)
    output_data = lms_obj.engine()
    print(output_data)
    #----------------------------------write output to a file--------------------------------------------------
    new_file = open("C:\\Users\\sreen\\OneDrive\\Desktop\\Python\\training/"+l_cust_name+".txt", "a")
    new_file.write(str(output_data))
    new_file.close()
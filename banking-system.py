print("Banking Transaction Processing System")
account_name= "Khadija Ibrahim"
account_number= "ACC1001"
balance= 5000
deposit= 1000
balance= balance + deposit
print("New balance:",balance)
withdrawal= 500
if withdrawal <= balance:
         balance= balance - withdrawal
         print("withdrawal successful")
print("Balance after withdrawal:",balance)  

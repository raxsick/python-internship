balance=5000
correct_pin=69

while True:
 pin_attempts = 0
 while pin_attempts < 3:
  pin=int(input("enter your pin :"))
  if pin == correct_pin:
   
   x=int(input("enter the amount you want to withdrawl :"))
   if x > balance:
    print("insufficient balance")
   else:
    balance = balance - x
    print("your remaining balance is :",balance)
    
   break
  else:
   print("wrong pin")
   pin_attempts = pin_attempts + 1

 if pin_attempts >= 3:
  print("blocked")
  break
  
 print("Do you want to continue (yes/no)?")
 continue_choice = input().lower()
 if continue_choice != 'yes':
  break
       








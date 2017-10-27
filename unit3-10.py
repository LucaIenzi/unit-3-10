user_input = input()

number_of_user_inputs = 0
answer = 0
while user_input != -1 : 
     if 0 <= user_input <= 100:
         answer = answer + user_input
         number_of_user_inputs = number_of_user_inputs + 1
         final_mark = answer / number_of_user_inputs
         print (final_mark)
         user_input = input()
     else:
        print("please enter a number inbetween 0 and 100")
        user_input = input()
else:
    print(final_mark)

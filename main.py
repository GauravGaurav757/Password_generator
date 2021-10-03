import random
import string


user_dict = {}

try:
    user_input = int(input("How many letters it should contain: "))

except:
    print("Error occured: Plss enter a correct value.")

else:
    
    print("Type 1 for Strong,2 for Medium,3 for Week")
    user_input_type = int(input("Strong Medium or Week: "))

    #Pass generator Strong
    if user_input_type == 1:
        ran = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = user_input))   
        print("\nThe password is: "+ran)


    #Pass generator Medium
    elif user_input_type == 2:
        med = ''.join(random.choices(string.ascii_uppercase + string.digits[0:9] , k = user_input))
        print("\nThe password is: "+med)


    #Pass generator weak
    elif user_input_type == 3:
        wek = ''.join(random.choices(string.ascii_uppercase , k = user_input))
        print("\nThe password is: "+wek)


    approvel = input("Do you want to save the password? [y , n]: ")

    if approvel == 'y':
        name = input("\nName the wesite or account for which you are saving: ")

        if user_input_type == 1:
            user_dict[name] = ran

        elif user_input_type == 2:
            user_dict[name] = med

        elif user_input_type == 3:
            user_dict[name] = wek

        elif approvel =='n':
            print("Thank you!")

# print(user_dict)
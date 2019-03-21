def age_program():
  seconds_or_years = input("Give me seconds (s) or years (y) :")
  if seconds_or_years == "s":
    user_value = input("Enter the number of seconds you've lived for: ")
    print ("You've lived for {} years".format(int(user_value) / 60 / 60 / 24 / 365))
  elif seconds_or_years == "y":
    user_value = input("Enter the number of years you've lived for: ")
    print ("You've lived for {} seconds".format(int(user_value) * 60 * 60 * 24 * 365))
  else:
    print("You've inputted an improper value")

age_program()
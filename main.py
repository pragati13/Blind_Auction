from replit import clear
import art

print(art.logo)
print("Welcome to the secret auction program.")
new_dictionary = {}
list_1 = []
tmp = 0
flag_1 = True

while flag_1:
  name = input("What is your name?: ")
  bid = input("What's your bid?: $")
  new_dictionary[name] = bid

  flag = True
  while flag:
    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if answer == "yes":
      clear()
      flag = False
    elif answer == "no":
      flag_1 = False
      break
    else:
      print("Please enter valid input...")


for thing in new_dictionary:
  if int(new_dictionary[thing]) > tmp:
    tmp = int(new_dictionary[thing])
    x = thing

print(f"The winner is {x} with a bid ${tmp}.")
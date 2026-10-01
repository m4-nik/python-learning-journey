#building a shopping cart program
cart = []
bill = 0
while True:
     ask = input("What would you like?(type nothing to quit)")
     if ask.lower() == "nothing":
          break
     else:
         x = input("Enter the item:")
         cart.append(x)
         y = float(input("Enter the price $"))
         bill = bill + y
print ("Ok so your final items are:", list)
print ("And your final price is", bill)

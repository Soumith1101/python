menu = {"Pizza":20, "Burger":15, "Cookies":17, "Samosa":14, "French Fries":11, "Nutella":16, "Croissant":6, "Cake":100, "Dosa":65, "Ice cream":35, "Cheese with bread":45, "Musli":39, "Salad":129, "Tea":2, "Cofee":7, "Cereals":109, "Chips":8, "Chocolate":105, "Noodles":25, "Nachos":59, "Pancakes":9, "Cocola":34, "Pepsi":67, "Sprite":89, "Apple juice":43, "Mango juice":45, "Orange juice":49, "Sevenup":10, "Milk":5, "Water":1}
for item, price in menu.items():
	print(f'{item} $ {price}')

order = ""
order_price = []
bill = 0
order_cart = []
while order != "Q":
	order = input("Enter your order press q to quit: - ").capitalize()
	if order in menu:
		print(f'{order} costs $ {menu[order]} and has been added to your cart')
		order_cart.append(order)
		order_price.append(menu[order])
	elif order == "Q":
		name = input("Enter Your Name -:")
		print("Thanks for visiting")
		print(f"You brought these items")
		for item in order_cart:
			print(item)
		for price in order_price:
			bill = bill + price
		print(f'Your total price is {bill}')
		mybill = open('Your total order.txt', 'w')
		mybill.write(f'{name}, you bought{order_cart} and your total order is {bill}')

	else:
		print("Sorry, Its not available")
print("Check your txt file")
		

		


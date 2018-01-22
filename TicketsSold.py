import sys

def TicketPricing():
	price = 15	
	tickets_sold = input("Enter a number ")
	profit = tickets_sold * price
	print(profit)
	print("We made $%s from ticket sales today" %(profit))

def main():
	TicketPricing()

if __name__ == '__main__':
	main()

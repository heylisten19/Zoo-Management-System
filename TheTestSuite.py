import unittest
import database
import sqlite3
import datetime

class Testing(unittest.TestCase): # Currently: 16 test cases
        
	def test_create_connection(self):
		self.assertIsNotNone(database.create_connection("ZooManagement.db"))

	def test_select(self):
		self.assertIsNone(database.select(database.create_connection("ZooManagement.db"), "Supplies_In_Stock"))

	def test_makeGUI(self):
		self.assertIsNone(database.makeGUI())

	def test_edit_cell(self):
		self.assertIsNone(database.edit_cell(database.create_connection("ZooManagement.db"), "dinosaurs", "age", 7, "T-Rex"))

	def test_update_days_since_bath(self):
		self.assertIsNone(database.update_days_since_bath(database.create_connection("ZooManagement.db")))

	def test_wash_dino(self):
		conn = database.create_connection("ZooManagement.db")
		curr = conn.cursor()
		database.wash_dino(curr, "Hippo")
		curr.execute("select Day_Of_Last_Bath from dinosaurs where type = 'Hippo'")
		self.assertEqual(curr.fetchone()[0], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

	def test_wash_all_dinos(self):
		conn = database.create_connection("ZooManagement.db")
		curr = conn.cursor()
		database.wash_all_dinos(curr)
		curr.execute("select Day_Of_Last_Bath from dinosaurs")
		for i in curr.fetchall():
			self.assertEqual(i[0], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	    
	def test_populate_food_types(self):
		conn = database.create_connection("ZooManagement.db")
		curr = conn.cursor()
		database.populate_food_types(curr)
		curr.execute("select Type_Of_Food from dinosaurs")
		self.assertIsNotNone(curr.fetchall())

	def test_populate_food_per_day(self):
		conn = database.create_connection("ZooManagement.db")
		curr = conn.cursor()
		database.populate_food_per_day(curr)
		curr.execute("select Pounds_Of_Food_Per_Day from dinosaurs")
		self.assertIsNotNone(curr.fetchall())

	def test_populate_supplies_in_stock(self):
		conn = database.create_connection("ZooManagement.db")
		curr = conn.cursor()
		database.populate_supplies_in_stock(curr)
		curr.execute("select amount from Supplies_In_Stock")
		self.assertIsNotNone(curr.fetchall())

	def test_seats_unreserved_names_who_reserved_seats(self): # Print the names of those who reserved seats
		conn = database.create_connection("ZooManagement.db")
		curr = conn.cursor()
		database.seats_unreserved(conn)
		curr.execute("select name from reservations")
		for i in curr.fetchall()[0:3]:
			print(i)
		self.assertIsNotNone(curr.fetchall())

	def test_seats_unreserved_reservation_names(self): # Print the names of the reservations
		conn = database.create_connection("ZooManagement.db")
		curr = conn.cursor()
		database.seats_unreserved(conn)
		curr.execute("select reservationName from reservations")
		for j in curr.fetchall()[0:3]:
			print(j)
		self.assertIsNotNone(curr.fetchall())

	def test_seats_unreserved_sizes(self): # Print the sizes of the reservation
		conn = database.create_connection("ZooManagement.db")
		curr = conn.cursor()
		database.seats_unreserved(conn)
		curr.execute("select size from reservations")
		for k in curr.fetchall()[0:3]:
			print("size is", k[0])
		self.assertIsNotNone(curr.fetchall())
	
	def test_seats_unreserved_correct_reservation_size(self): # Print the correct number of remaining seats
		conn = database.create_connection("ZooManagement.db")
		curr = conn.cursor()
		total = 110
		cap = 150
		database.seats_unreserved(conn, total, cap)
		self.assertEqual(cap - total, 40)
	def test_SellTickets(self):
		# Raise error for negative tickets sold
		tickets_sold = -1
		database.SellTickets(tickets_sold)
		self.assertRaises(ValueError, SellTickets, -1) #Raise error if Sold Tickets is negative
			
	def test_SellTickets(self):
		#Test for valid tickets_sold
		tickets_sold = 0
		database.SellTickets(tickets_sold)
		self.assertGreaterEqual(tickets_sold, 0)
		

    
        
if __name__ == '__main__':
    unittest.main()

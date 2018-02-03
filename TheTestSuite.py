import unittest
import database
import sqlite3
import datetime

class Testing(unittest.TestCase):
        
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
       
    def test_feed_dinos(self):   
        conn = database.create_connection("ZooManagement.db")
        curr = conn.cursor()
        curr.execute("select amount from Supplies_In_Stock where type = 'Meat'")
        before = curr.fetchall()[0][0]
        database.feed_dinos(curr)
        curr.execute("select amount from Supplies_In_Stock where type = 'Meat'")
        after = curr.fetchall()[0][0]
        if before == 0:
            self.assertEqual(before, after)
        else:
            self.assertIsNot(before, after)
            
    def test_order_more_supplies(self):
        conn = database.create_connection("ZooManagement.db")
        curr = conn.cursor()
        curr.execute("select amount from Supplies_In_Stock where type = 'Money'")
        before = curr.fetchall()[0][0]
        database.order_more_supplies(curr, 1, "Vegetables")
        curr.execute("select amount from Supplies_In_Stock where type = 'Money'")
        after = curr.fetchall()[0][0]
        if before == 0:
            self.assertEqual(before, after)
        else:
            self.assertIsNot(before, after)
    
    def test_seats_unreserved(self):
        conn = database.create_connection("ZooManagement.db")
        seats_taken = database.seats_unreserved(conn)
        self.assertIsNotNone(seats_taken)
        
    def test_sellTickets(self):
        conn = database.create_connection("ZooManagement.db")
        profit = database.SellTickets()
        self.assertIsNotNone(profit)
    
    
    
if __name__ == '__main__':
    unittest.main()

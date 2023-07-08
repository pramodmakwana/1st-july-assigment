#!/usr/bin/env python
# coding: utf-8
1. What is the primary goal of Object-Oriented Programming ?

The main goal of Object-Oriented Programming (OOP) is to make code more organized and reusable. In OOP, we 
think of real-world things or ideas as objects, which have both data and actions. We create these objects 
from blueprints called classes. Classes define what objects of a certain type can do and what information 
they can store. OOP allows objects to communicate and work together to solve problems. It's like a way of 
modeling the real world in code, making it easier to understand and manage. The important principles in OOP 
are encapsulation, inheritance, and polymorphism


2.	What is an object in Python?

An Object is an instance of a Class. A class is like a blueprint while an instance is a copy of the class with actual values. Python is an object-oriented programming language that stresses objects i.e. it mainly emphasizes functions.

3.	What is a class in Python?

A class is a code template for creating objects. Objects have member variables and have behaviour associated with them. In python a class is created by the keyword class . An object is created using the constructor of the class. This object will then be called the instance of the class

4.	What are attributes and methods in a class?

Any variable that is bound in a class is a class attribute . Any function defined within a class is a method . Methods receive an instance of the class, conventionally called self , as the first argument


5.	What is the difference between class variables and instance variables in Python?

Class variables are useful for storing data that is shared among all instances of a class, such as constants or default values. Instance variables are used to store data that is unique to each instance of a class, such as object properties.
class variables are shared between a class and all its subclasses, while class instance variables only belong to one specific class.

6.	What is the purpose of the self parameter in Python class methods?

self represents the instance of the class. By using the “self” we can access the attributes and methods of the class in python. It binds the attributes with the given arguments. The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes.


# 7.	For a library management system, you have to design the "Book" class with OOP principles in mind. The “Book” class will have following attributes:
# a.	title: Represents the title of the book.
# b.	author: Represents the author(s) of the book.
# c.	isbn: Represents the ISBN (International Standard Book Number) of the book.
# d.	publication_year: Represents the year of publication of the book.
# e.	available_copies: Represents the number of copies available for checkout. The class will also include the following methods:
# a.	check_out(self): Decrements the available copies by one if there are copies available for checkout.
# b.	return_book(self): Increments the available copies by one when a book is returned.
# c.	display_book_info(self): Displays the information about the book, including its attributes and the number of available copies.
# 
# 
# 
#     

# In[76]:


class Book:
    def __init__(self, title, author, isbn, publication_year, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.available_copies = available_copies

    def check_out(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return("Book checked out successfully!")
        else:
            return("Sorry, no copies available for checkout.")

    def return_book(self):
        self.available_copies += 1
        return("Book returned successfully!")

    def display_book_info(self):
        return f'''
    "Book Information:"
    "Title:", {self.title}
    "Author:", {self.author}
    "ISBN:", {self.isbn}
    "Publication Year:", {self.publication_year}
    "Available Copies:", {self.available_copies}
    '''


book = Book("Lost in space", "john mathew", "257957017", 2023, 40)
print(book.display_book_info())
print(book.check_out())
print(book.display_book_info())
print(book.return_book())
print(book.display_book_info())


# 8.	For a ticket booking system, you have to design the "Ticket" class with OOP principles in mind. The “Ticket” class should have the following attributes:
# a.	ticket_id: Represents the unique identifier for the ticket.
# b.	event_name: Represents the name of the event.
# c.	event_date: Represents the date of the event.
# d.	venue: Represents the venue of the event.
# e.	seat_number: Represents the seat number associated with the ticket.
# f.	price: Represents the price of the ticket.
# g.	is_reserved: Represents the reservation status of the ticket. The class also includes the following methods:
# a.	reserve_ticket(self): Marks the ticket as reserved if it is not already reserved.
# b.	cancel_reservation(self): Cancels the reservation of the ticket if it is already reserved.
# c.	display_ticket_info(self): Displays the information about the ticket, including its attributes and reservation status.
# 

# In[72]:


class Ticket:
    def __init__(self, ticket_id, event_name, event_date, venue, seat_number, price):
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.event_date = event_date
        self.venue = venue
        self.seat_number = seat_number
        self.price = price
        self.is_reserved = False
    
    def reserve_ticket(self):
        if self.is_reserved == False:
            self.is_reserved = True
            return("Ticket reserved successfully!")
        else:
            return("Ticket is already reserved.")
    
    def cancel_reservation(self):
        if self.is_reserved :
            self.is_reserved = False
            return("Ticket reservation canceled successfully!")
        else:
            return("Ticket is not reserved.")
            
    def display_ticket_info(self):
        return f'''
        "Ticket Information:"
        "Ticket ID:", {self.ticket_id}
        "Event Name:", {self.event_name}
        "Event Date:", {self.event_date}
        "Venue:", {self.venue}
        "Seat Number:", {self.seat_number}
        "Price:", {self.price}
        "Reservation Status:", {"Reserved" if self.is_reserved else "Not Reserved"}
        '''

ticket1 = Ticket("G1234", "stand up ", "01-07-2-23", "Concert Hall", "p30", 300)
print(ticket1.display_ticket_info())
print(ticket1.reserve_ticket())
print(ticket1.display_ticket_info())
print(ticket1.cancel_reservation())


# 9.	You are creating a shopping cart for an e-commerce website. Using OOP to model the "ShoppingCart" functionality the class should contain following attributes and methods:
# a.	items: Represents the list of items in the shopping cart. The class also includes the following methods:
# a.	add_item(self, item): Adds an item to the shopping cart by appending it to the list of items.
# b.	remove_item(self, item): Removes an item from the shopping cart if it exists in the list.
# c.	view_cart(self): Displays the items currently present in the shopping cart.
# d.	clear_cart(self): Clears all items from the shopping cart by reassigning an empty list to the items attribute.
# 

# In[68]:


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        return "Item added to the shopping cart."

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return "Item removed from the shopping cart."
        else:
            return "Item is not present in the shopping cart."

    def view_cart(self):
        if self.items:
            cart_items = "\n".join(self.items)
            return f"\nShopping Cart:\n{cart_items}\n"
        else:
            return "Your shopping cart is empty."
    
    def clear_cart(self):
        self.items = []
        return "Shopping cart cleared."


cart = ShoppingCart()

print(cart.add_item("oil"))
print(cart.add_item("rice"))
print(cart.add_item("soap"))
print(cart.view_cart())
print(cart.remove_item("Koh-i-Noor"))
print(cart.view_cart())
print(cart.clear_cart())
print(cart.view_cart())
    


# 10.	Imagine a school management system. You have to design the "Student" class using OOP concepts.The “Student” class has the following attributes:
# a.	name: Represents the name of the student.
# b.	age: Represents the age of the student.
# c.	grade: Represents the grade or class of the student.
# d.	student_id: Represents the unique identifier for the student.
# e.	attendance: Represents the attendance record of the student. The class should also include the following methods:
# a.	update_attendance(self, date, status): Updates the attendance record of the student for a given date with the provided status (e.g., present or absent).
# b.	get_attendance(self): Returns the attendance record of the student.
# c.	get_average_attendance(self): Calculates and returns the average attendance percentage of the student based on their attendance record.
# 
#     
#     
# 

# In[65]:


class Student():
    
    def __init__(self,name,age,grade,student_id):
        self.name=name
        self.age=age
        self.grade=grade
        self.student_id=student_id
        self.attendance={}
        
    def update_attendance(self,date,status):
        self.attendance[date]=status
        
    def get_attendance(self,):
        return self.attendance
        
        
    def get_average_attendance(self):
        total_days = len(self.attendance)
        present_days = list(self.attendance.values()).count("present")
        if total_days > 0:
            attendance_percentage =(present_days/total_days)*100
            return attendance_percentage
        else:
            return 0.0
        
        
student1=Student("rahul singh",32,30,"r002")
        
student1.update_attendance("2023-07-01", "present")
student1.update_attendance("2023-07-02", "absent")
student1.update_attendance("2023-07-03", "present")

attendance_record = student1.get_attendance()
print("attendance_record -->", attendance_record)
average_attendance = student1.get_average_attendance()
print("average_attendance -->", average_attendance)
        
    
    


# In[ ]:





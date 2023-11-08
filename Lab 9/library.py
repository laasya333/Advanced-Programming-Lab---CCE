class Book:
    def __init__(self, title, author, price, publisher, stock):
        self.title = title
        self.author = author
        self.price = price
        self.publisher = publisher
        self.stock = stock

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")
        print(f"Publisher: {self.publisher}")
        print(f"Stock: {self.stock} copies available")

    def sell_books(self, num_copies):
        try:
            num_copies = int(num_copies)
            if num_copies <= 0:
                raise ValueError("Invalid input. Please enter a positive number.")
            
            if self.stock >= num_copies:
                total_cost = self.price * num_copies
                print(f"Total Cost: ${total_cost}")
                self.stock -= num_copies
            else:
                print("Required copies not in stock")
        except ValueError as e:
            print(f"Error: {e}")

# Sample usage of the Book class
if __name__ == "__main__":
    # Creating book objects
    book1 = Book("The Alchemist", "Paulo Coelho", 15.99, "HarperCollins", 50)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 12.99, "HarperCollins", 30)

    # Displaying book details
    print("Book 1 Details:")
    book1.display_details()
    print("\nBook 2 Details:")
    book2.display_details()

    # Selling books
    num_copies = input("Enter the number of copies you want to purchase for Book 1: ")
    print("Book 1 - Purchase Details:")
    book1.sell_books(num_copies)

    num_copies = input("Enter the number of copies you want to purchase for Book 2: ")
    print("Book 2 - Purchase Details:")
    book2.sell_books(num_copies)

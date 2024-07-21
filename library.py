class LibraryItem:
    def __init__(self, title, author, category, item_id):
        self.title = title
        self.author = author
        self.category = category
        self.item_id = item_id
        self.is_checked_out = False

class Library:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.item_id] = item
        print(f"Item '{item.title}' added successfully.")

    def check_out_item(self, item_id):
        if item_id in self.items:
            item = self.items[item_id]
            if not item.is_checked_out:
                item.is_checked_out = True
                print(f"Item '{item.title}' checked out successfully.")
            else:
                print(f"Item '{item.title}' is already checked out.")
        else:
            print("Item not found.")

    def return_item(self, item_id):
        if item_id in self.items:
            item = self.items[item_id]
            if item.is_checked_out:
                item.is_checked_out = False
                print(f"Item '{item.title}' returned successfully.")
            else:
                print(f"Item '{item.title}' is not checked out.")
        else:
            print("Item not found.")

    def search_items(self, query, search_type):
        results = []
        for item in self.items.values():
            if search_type == "title" and query.lower() in item.title.lower():
                results.append(item)
            elif search_type == "author" and query.lower() in item.author.lower():
                results.append(item)
            elif search_type == "category" and query.lower() in item.category.lower():
                results.append(item)
        return results

if __name__ == "__main__":
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add New Item")
        print("2. Check Out Item")
        print("3. Return Item")
        print("4. Search Items")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            category = input("Enter category: ")
            item_id = input("Enter item ID: ")
            item = LibraryItem(title, author, category, item_id)
            library.add_item(item)
        elif choice == '2':
            item_id = input("Enter item ID: ")
            library.check_out_item(item_id)
        elif choice == '3':
            item_id = input("Enter item ID: ")
            library.return_item(item_id)
        elif choice == '4':
            search_type = input("Search by (title/author/category): ")
            query = input("Enter search query: ")
            results = library.search_items(query, search_type)
            if results:
                print("Search Results:")
                for item in results:
                    print(f"Title: {item.title}, Author: {item.author}, Category: {item.category}, Checked Out: {item.is_checked_out}")
            else:
                print("No items found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

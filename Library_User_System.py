import sys


class Library:
    def __init__(self):
        self.books = {}  # {book: amount}
        self.labs = {}  # {date: [lab_id]}
        self.conferences = {}  # {date: [room_id]}

    # Validation functions
    def is_book_exist(self, book):
        if book in self.books:
            return True
        else:
            print(f"{book} is not available in the library.")
            return False

    def have_book_copies(self, book):
        if book in self.books and self.books[book] > 0:
            return True
        else:
            print(f"No copies of {book} left.")
            return False

    def is_lab_available(self, date, lab_id):
        if lab_id in self.labs.get(date, []):
            print(f"Lab {lab_id} is already booked on {date}.")
            return False
        return True

    def is_conference_available(self, date, room_id):
        if room_id in self.conferences.get(date, []):
            print(f"Conference Room {room_id} is already booked on {date}.")
            return False
        return True

    # Library functions
    def add_book(self, book, amount):
        self.books[book] = amount

    def search_book(self, book):
        if self.is_book_exist(book) and self.have_book_copies(book):
            print(f"{book} has {self.books[book]} copies left.")

    def borrow_book(self, book):
        self.books[book] -= 1

    def return_book(self, book):
        self.books[book] += 1

    def apply_lab(self, date, lab_id):
        if date not in self.labs:
            self.labs[date] = []
        self.labs[date].append(lab_id)

    def apply_conference(self, date, room_id):
        if date not in self.conferences:
            self.conferences[date] = []
        self.conferences[date].append(room_id)


class User:
    def __init__(self, type, name):
        self.name = name
        self.type = type
        self.books = []  # [book]
        self.borrow_limit = {"U": 5, "G": 8, "P": 10}
        self.labs = {}  # {date: lab_id}
        self.conferences = {}  # {date: room_id}

    def __str__(self):
        print()  # blank line before status

        if self.type == "U":
            print(f"--- {self.name}'s Status ---")
            print(f"Borrowed Books: {sorted(self.books)}")

        elif self.type == "G":
            print(f"--- {self.name}'s Status ---")
            print(f"Borrowed Books: {sorted(self.books)}")
            # >>> changed label
            print(f"Reserved Labs: {dict(sorted(self.labs.items()))}")

        elif self.type == "P":
            print(f"--- {self.name}'s Status ---")
            print(f"Borrowed Books: {sorted(self.books)}")
            print(f"Reserved Labs: {dict(sorted(self.labs.items()))}")
            print(f"Reserved Conferences: {dict(sorted(self.conferences.items()))}")

        print()  # blank line after status

    def borrow_book(self, book, library: Library):
        if library.is_book_exist(book) and library.have_book_copies(book):
            total_borrowed = len(self.books)
            if total_borrowed >= self.borrow_limit[self.type]:
                print(
                    f"{self.name} has reached the borrow limit of {self.borrow_limit[self.type]} books."
                )
            else:
                library.borrow_book(book)
                self.books.append(book)

    def return_book(self, book, library: Library):
        if library.is_book_exist(book):
            if book not in self.books:
                print(f"{self.name} did not borrow {book}.")
            else:
                library.return_book(book)
                self.books.remove(book)

    def apply_lab(self, date, lab_id, library: Library):
        if self.type == "U":
            print(f"{self.name} is not allowed to reserve labs.")
        elif library.is_lab_available(date, lab_id):
            library.apply_lab(date, lab_id)
            self.labs[date] = lab_id

    def apply_conference(self, date, room_id, library: Library):
        if self.type in ["U", "G"]:
            print(f"{self.name} is not allowed to reserve conference rooms.")
        elif library.is_conference_available(date, room_id):
            library.apply_conference(date, room_id)
            self.conferences[date] = room_id


if __name__ == "__main__":
    input_str = sys.stdin.read()

    system_info = input_str.splitlines()

    # library initialization
    library = Library()
    initial_books = system_info[0].split()
    for i in range(0, len(initial_books), 2):
        book = initial_books[i]
        amount = int(initial_books[i + 1])
        library.add_book(book, amount)

    users = {"": User}

    for i in range(1, len(system_info)):
        if system_info[i] == "EXIT":
            break

        op = system_info[i].split(" ")

        if op[0] == "CREATE_USER":
            users[op[2]] = User(op[1], op[2])
        elif op[0] == "SEARCH":
            library.search_book(op[1])
        elif op[0] == "BORROW":
            users[op[1]].borrow_book(op[2], library)
        elif op[0] == "RETURN":
            users[op[1]].return_book(op[2], library)
        elif op[0] == "SHOW":
            users[op[1]].__str__()
        elif op[0] == "APPLY_LAB":
            users[op[1]].apply_lab(op[2], op[3], library)
        elif op[0] == "APPLY_CONFERENCE":
            users[op[1]].apply_conference(op[2], op[3], library)

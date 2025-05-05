import sys


class Book:
    def __init__(self, title, authors, publication_year, edition):
        self.title = title
        self.authors = sorted(authors.split(", "))
        self.publication_year = publication_year
        self.edition = edition

    def __str__(self):
        author_str = ", ".join(self.authors)
        return f"Title: {self.title}; Authors: {author_str}; Year: {self.publication_year}; Edition: {self.edition}"

    def add_author(self, new_author):
        self.authors.append(new_author)
        self.authors.sort()

    def remove_author(self, author_to_remove):
        if author_to_remove in self.authors:
            self.authors.remove(author_to_remove)

    def update_edition(self, new_edition):
        self.edition = new_edition

    def update_publication_year(self, new_year):
        self.publication_year = new_year

    def update_title(self, new_title):
        self.title = new_title


if __name__ == "__main__":
    input_str = sys.stdin.read()

    book_info = input_str.splitlines()

    n = int(book_info[0])
    book_index = 1

    for _ in range(n):
        book = Book(
            book_info[book_index + 1],
            book_info[book_index + 2],
            book_info[book_index + 3],
            book_info[book_index + 4],
        )

        for i in range(book_index + 6, len(book_info)):
            if book_info[i] == "---":
                book_index = i
                break

            if book_info[i] == "print":
                print(book.__str__())
                continue

            op, obj = book_info[i].split(" ", 1)

            if op == "add_author":
                book.add_author(obj)
            elif op == "rm_author":
                book.remove_author(obj)
            elif op == "update_edition":
                book.update_edition(obj)
            elif op == "update_pubyear":
                book.update_publication_year(obj)
            elif op == "update_title":
                book.update_title(obj)

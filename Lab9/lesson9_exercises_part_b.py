# Part B, Polymorphism with inheritance

# 1. Create a base class Document with title attribute and a method describe()
class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return "This is a generic document"


# 2. Create PDFDocument(Document) and TextDocument(Document)
# 3. Override describe() in both subclasses so they return different descriptions
class PDFDocument(Document):
    def describe(self):
        return "This is a PDF document"  # Task 3: Overriding base class' describe() method


class TextDocument(Document):
    def describe(self):
        return "This is a text document"  # Task 3: Overriding base class' describe() method


# 4. Create several PDFDocument and TextDocument objects and store them in one list
pdf_document_1 = PDFDocument("PDF Document 1")
pdf_document_2 = PDFDocument("PDF Document 2")
text_document_1 = TextDocument("Text Document 1")
text_document_2 = TextDocument("Text Document 2")

documents = [pdf_document_1, pdf_document_2, text_document_1, text_document_2]


# 5. Loop through the list and print each document's title and the result of describe()
for document in documents:
    print(document.title, document.describe(), sep=" | ")
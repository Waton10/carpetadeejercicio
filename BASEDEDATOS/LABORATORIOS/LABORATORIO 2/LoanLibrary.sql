USE LoanLibrary;

CREATE TABLE Books (
    BookID INT PRIMARY KEY IDENTITY(1,1),
    Title VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    ISBN VARCHAR(13) UNIQUE,
    PublicationDate DATE
);

CREATE TABLE Members (
    MemberID INT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(255) NOT NULL,
    ContactInformation VARCHAR(255)
);

CREATE TABLE Loans (
    LoanID INT PRIMARY KEY IDENTITY(1,1),
    BookID INT FOREIGN KEY REFERENCES Books(BookID),
    MemberID INT FOREIGN KEY REFERENCES Members(MemberID),
    LoanDate DATE NOT NULL,
    DueDate DATE NOT NULL,
    ReturnDate DATE
);


INSERT INTO Books (Title, Author, ISBN, PublicationDate) VALUES ('Cien Años de Soledad', 'Gabriel Garcia Marquez', '9780307389732', '1967-05-30');
INSERT INTO Members (Name, ContactInformation) VALUES ('Alexander Mejia', 'alexander@gmail.com');


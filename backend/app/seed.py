from sqlalchemy import select

from app.core.database import Base, SessionLocal, engine
from app.models.book import Book


BOOKS = [
    {
        "id": "BOOK-001",
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "description": "A classic novel about love, society, manners, and personal growth.",
        "price": 29900,
        "stock": 12,
        "category": "Classic",
    },
    {
        "id": "BOOK-002",
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "description": "A story of ambition, wealth, love, and the American Dream.",
        "price": 24900,
        "stock": 10,
        "category": "Classic",
    },
    {
        "id": "BOOK-003",
        "title": "Jane Eyre",
        "author": "Charlotte Brontë",
        "description": "A coming-of-age story about independence, love, and resilience.",
        "price": 32900,
        "stock": 8,
        "category": "Classic",
    },
    {
        "id": "BOOK-004",
        "title": "Little Women",
        "author": "Louisa May Alcott",
        "description": "The story of four sisters growing up and finding their own paths.",
        "price": 27900,
        "stock": 14,
        "category": "Fiction",
    },
    {
        "id": "BOOK-005",
        "title": "The Picture of Dorian Gray",
        "author": "Oscar Wilde",
        "description": "A philosophical tale exploring beauty, morality, and corruption.",
        "price": 28900,
        "stock": 9,
        "category": "Classic",
    },
    {
        "id": "BOOK-006",
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "description": "A young shepherd follows his dreams in search of his personal legend.",
        "price": 39900,
        "stock": 15,
        "category": "Fiction",
    },
    {
        "id": "BOOK-007",
        "title": "Atomic Habits",
        "author": "James Clear",
        "description": "A practical guide to building better habits through small improvements.",
        "price": 49900,
        "stock": 20,
        "category": "Self Development",
    },
    {
        "id": "BOOK-008",
        "title": "Deep Work",
        "author": "Cal Newport",
        "description": "Strategies for developing focused work and reducing distractions.",
        "price": 44900,
        "stock": 11,
        "category": "Productivity",
    },
    {
        "id": "BOOK-009",
        "title": "The Psychology of Money",
        "author": "Morgan Housel",
        "description": "Lessons about money, behavior, wealth, and financial decision-making.",
        "price": 42900,
        "stock": 13,
        "category": "Business",
    },
    {
        "id": "BOOK-010",
        "title": "Zero to One",
        "author": "Peter Thiel",
        "description": "Ideas about startups, innovation, competition, and building the future.",
        "price": 45900,
        "stock": 7,
        "category": "Business",
    },
    {
        "id": "BOOK-011",
        "title": "Sapiens",
        "author": "Yuval Noah Harari",
        "description": "An exploration of human history and the development of civilization.",
        "price": 54900,
        "stock": 10,
        "category": "History",
    },
    {
        "id": "BOOK-012",
        "title": "Meditations",
        "author": "Marcus Aurelius",
        "description": "Reflections on discipline, resilience, responsibility, and Stoic philosophy.",
        "price": 25900,
        "stock": 16,
        "category": "Philosophy",
    },
    {
        "id": "BOOK-013",
        "title": "The Design of Everyday Things",
        "author": "Don Norman",
        "description": "An introduction to human-centered design and everyday usability.",
        "price": 59900,
        "stock": 6,
        "category": "Design",
    },
    {
        "id": "BOOK-014",
        "title": "The Pragmatic Programmer",
        "author": "David Thomas & Andrew Hunt",
        "description": "Practical principles and techniques for becoming a better software developer.",
        "price": 69900,
        "stock": 9,
        "category": "Technology",
    },
    {
        "id": "BOOK-015",
        "title": "Ikigai",
        "author": "Héctor García & Francesc Miralles",
        "description": "Ideas about purpose, balance, longevity, and finding meaning in everyday life.",
        "price": 34900,
        "stock": 18,
        "category": "Self Development",
    },
]


def seed():
    # Make sure the tables exist.
    Base.metadata.create_all(bind=engine)

    # Open a database session.
    db = SessionLocal()

    try:
        # Don't insert the books again if they already exist.
        existing_book = db.scalar(select(Book.id).limit(1))

        if existing_book:
            print("Books already exist. Nothing to seed.")
            return

        # Convert each dictionary into a Book object.
        for book_data in BOOKS:
            book = Book(**book_data)
            db.add(book)

        # Permanently save all books.
        db.commit()

        print(f"Seeded {len(BOOKS)} books successfully.")

    finally:
        # Always close the database session.
        db.close()


if __name__ == "__main__":
    seed()
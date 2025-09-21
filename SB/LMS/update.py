from supabase import create_client, Client
from dotenv import load_dotenv
import os


load_dotenv()

url = os.getenv("supabaseUrl")
key = os.getenv("supabaseKey")

if not url or not key:
    raise ValueError("SUPABASE_URL or SUPABASE_KEY not set in .env file")

sb: Client = create_client(url, key)


def update_member(member_id: int, name: str = None, email: str = None):
    """Update member details (name or email)."""
    data = {}
    if name:
        data["name"] = name
    if email:
        data["email"] = email
    
    if not data:
        print("❌ No updates provided.")
        return
    
    resp = sb.table("members").update(data).eq("member_id", member_id).execute()
    if resp.data:
        print("✅ Member updated:", resp.data)
    else:
        print("❌ Member not found.")


def update_book(book_id: int, title: str = None, author: str = None, category: str = None, stock: int = None):
    """Update book details (title, author, category, stock)."""
    data = {}
    if title:
        data["title"] = title
    if author:
        data["author"] = author
    if category:
        data["category"] = category
    if stock is not None:
        data["stock"] = stock
    
    if not data:
        print("❌ No updates provided.")
        return
    
    resp = sb.table("books").update(data).eq("book_id", book_id).execute()
    if resp.data:
        print("✅ Book updated:", resp.data)
    else:
        print("❌ Book not found.")


if __name__ == "__main__":
    print("\n--- Update Menu ---")
    print("1. Update Member")
    print("2. Update Book")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        member_id = int(input("Enter Member ID: ").strip())
        name = input("Enter new name (leave blank to skip): ").strip()
        email = input("Enter new email (leave blank to skip): ").strip()
        update_member(member_id, name or None, email or None)

    elif choice == "2":
        book_id = int(input("Enter Book ID: ").strip())
        title = input("Enter new title (leave blank to skip): ").strip()
        author = input("Enter new author (leave blank to skip): ").strip()
        category = input("Enter new category (leave blank to skip): ").strip()
        stock_input = input("Enter new stock (leave blank to skip): ").strip()
        stock = int(stock_input) if stock_input else None
        update_book(book_id, title or None, author or None, category or None, stock)

    else:
        print("❌ Invalid choice.")

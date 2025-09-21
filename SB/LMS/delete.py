from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
url = os.getenv("supabaseUrl")   # 👈 from your .env file
key = os.getenv("supabaseKey")

if not url or not key:
    raise ValueError("supabaseUrl or supabaseKey not found in .env file")

sb: Client = create_client(url, key)


# -------------------------
# Delete Member
# -------------------------
def delete_member(member_id: int):
    """Delete a member only if they have no unreturned borrowed books."""
    borrowed = (
        sb.table("borrow_records")
        .select("*")
        .eq("member_id", member_id)
        .is_("return_date", "null")   # ✅ check if book not yet returned
        .execute()
    )

    if borrowed.data:
        print("❌ Cannot delete member. They have unreturned books.")
        return

    resp = sb.table("members").delete().eq("member_id", member_id).execute()
    if resp.data:
        print("✅ Member deleted:", resp.data)
    else:
        print("❌ Member not found.")


# -------------------------
# Delete Book
# -------------------------
def delete_book(book_id: int):
    """Delete a book only if it is not currently borrowed."""
    borrowed = (
        sb.table("borrow_records")
        .select("*")
        .eq("book_id", book_id)
        .is_("return_date", "null")   # ✅ check if book is currently borrowed
        .execute()
    )

    if borrowed.data:
        print("❌ Cannot delete book. It is currently borrowed.")
        return

    resp = sb.table("books").delete().eq("book_id", book_id).execute()
    if resp.data:
        print("✅ Book deleted:", resp.data)
    else:
        print("❌ Book not found.")


# -------------------------
# Main Program (CLI)
# -------------------------
if __name__ == "__main__":
    print("\n📚 Online Library Management System — Delete Page")
    print("1. Delete Member")
    print("2. Delete Book")
    choice = input("Choose option: ").strip()

    if choice == "1":
        member_id = int(input("Enter Member ID: "))
        delete_member(member_id)
    elif choice == "2":
        book_id = int(input("Enter Book ID: "))
        delete_book(book_id)
    else:
        print("❌ Invalid choice.")

from supabase import create_client, Client
from dotenv import load_dotenv
import os
 
load_dotenv()
 
url = os.getenv("supabaseUrl")
key = os.getenv("supabaseKey")
sb: Client = create_client(url, key)
 
def read():
    resp = sb.table("books").select("*").order("book_id", desc=False).execute()
    return resp.data
 
if __name__ == "__main__":
    books = read()
    if books:
        print("Books:")
        for b in books:
            if b['stock']>0:
                print(f"{b['book_id']}: {b['title']} - (Author:{b['author']}) — (Category:{b['category']}) — stock: {b['stock']}")
    else:
        print("No books found.")


    
def search_books(keyword: str):
    resp = sb.table("books").select("*").ilike("title", f"%{keyword}%").execute()
    resp_author = sb.table("books").select("*").ilike("author", f"%{keyword}%").execute()
    resp_category = sb.table("books").select("*").ilike("category", f"%{keyword}%").execute()
    results = {b['book_id']: b for b in resp.data + resp_author.data + resp_category.data}.values()
    
    if results:
        print(f"Search results for '{keyword}':")
        for b in results:
            print(f"{b['book_id']}: {b['title']} - Author: {b['author']} - Category: {b['category']} - Stock: {b['stock']}")
    else:
        print(f"No books found matching '{keyword}'.")


def member_details(member_id: int):
    member = sb.table("members").select("*").eq("member_id", member_id).execute()
    if not member.data:
        print("Member not found.")
        return
    
    print("Member Info:", member.data[0])
    
    borrowed = sb.table("borrow_records").select("record_id, book_id, borrow_date, return_date, books(title, author)").eq("member_id", member_id).execute()
    if borrowed.data:
        print("Borrowed Books:")
        for record in borrowed.data:
            book_title = record.get("books", {}).get("title", "Unknown")
            book_author = record.get("books", {}).get("author", "Unknown")
            status = "Returned" if record["return_date"] else "Borrowed"
            print(f"Record ID: {record['record_id']}, Book: {book_title} (Author: {book_author}), Borrow Date: {record['borrow_date']}, Status: {status}")
    else:
        print("No borrowed books found.")


if __name__ == "__main__":
    while True:
        print("\n--- Library System ---")
        print("1. List all books")
        print("2. Search books")
        print("3. Show member details")
        print("4. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            read()
        elif choice == "2":
            keyword = input("Enter title/author/category to search: ").strip()
            search_books(keyword)
        elif choice == "3":
            member_id = int(input("Enter Member ID: ").strip())
            member_details(member_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")
 
 
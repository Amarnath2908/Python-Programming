import os
from supabase import create_client, Client  
from dotenv import load_dotenv  


load_dotenv()

url = os.getenv("supabaseurl")
key = os.getenv("supabasekey")

sb: Client = create_client(url, key)
    
def add_member(name: str, email: str):
    payload = {"name": name, "email": email}
    resp = sb.table("members").insert(payload).execute()
    return resp.data

def add_book(title: str, author: str, category: str, stock: int = 1):
    payload = {"title": title, "author": author, "category": category, "stock": stock}
    resp = sb.table("books").insert(payload).execute()
    return resp.data


if __name__ == "__main__":
    print("1. Add Member")
    print("2. Add Book")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        name = input("Member Name: ").strip()
        email = input("Member Email: ").strip()
        created = add_member(name, email)
        print("Inserted Member:", created)

    elif choice == "2":
        title = input("Book Title: ").strip()
        author = input("Author: ").strip()
        category = input("Category: ").strip()
        stock = int(input("Stock (default 1): ").strip() or 1)
        created = add_book(title, author, category, stock)
        print("Inserted Book:", created)

    else:
        print("Invalid choice!")

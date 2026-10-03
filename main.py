import firebase_admin
from firebase_admin import credentials, firestore
import datetime

# 1. Connect to Firebase using your secret key file
try:
    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    print("✅ Successfully connected to the cloud database.")
except Exception as e:
    print(f"❌ Error connecting to Firebase: {e}")
    exit()

# --- CRUD FUNCTIONS ---

def add_product():
    print("\n--- ADD NEW PRODUCT ---")
    prod_id = input("Product ID (e.g., prod1): ")
    name = input("Product Name: ")
    price = float(input("Price: $"))
    stock = int(input("Quantity in stock: "))
    
    # Insert into the cloud
    db.collection('products').document(prod_id).set({
        'name': name,
        'price': price,
        'stock': stock
    })
    print(f"✅ Product '{name}' saved to the cloud.")

def view_products():
    print("\n--- PRODUCT CATALOG ---")
    products = db.collection('products').stream()
    for doc in products:
        data = doc.to_dict()
        print(f"ID: {doc.id} | {data['name']} | Price: ${data['price']} | Stock: {data['stock']}")

def delete_product():
    print("\n--- DELETE PRODUCT ---")
    prod_id = input("Enter the ID of the product to delete: ")
    db.collection('products').document(prod_id).delete()
    print(f" Product '{prod_id}' permanently deleted from the cloud.")

def register_user():
    print("\n--- REGISTER USER ---")
    user_id = input("User ID (e.g., user1): ")
    name = input("User Name: ")
    email = input("Email address: ")
    
    db.collection('users').document(user_id).set({
        'name': name,
        'email': email
    })
    print(f" User '{name}' registered in the cloud.")

def create_order():
    print("\n--- CREATE NEW ORDER ---")
    order_id = input("Order ID (e.g., ord1): ")
    user_id = input("Buyer User ID: ")
    
    # 1. Check if the user exists and get their name (Demostrando la relación)
    user_ref = db.collection('users').document(user_id)
    user = user_ref.get()
    
    if not user.exists:
        print("❌ User does not exist. Please register the user first.")
        return
        
    user_data = user.to_dict()
    user_name = user_data['name']
    print(f"✅ User found: {user_name}") # Aquí mostramos el nombre del usuario

    prod_id = input("Product ID to purchase: ")
    quantity = int(input("Quantity to purchase: "))
    
    # 2. Check if the product exists and has stock
    prod_ref = db.collection('products').document(prod_id)
    product = prod_ref.get()
    
    if not product.exists:
        print("❌ Product does not exist.")
        return
        
    prod_data = product.to_dict()
    if prod_data['stock'] < quantity:
        print("❌ Not enough stock available.")
        return
        
    #  Calculate total and create the order (Relating tables)
    total = prod_data['price'] * quantity
    db.collection('orders').document(order_id).set({
        'user_id': user_id,
        'product_id': prod_id,
        'quantity': quantity,
        'total_price': total,
        'date': datetime.datetime.now()
    })
    
    # Modify the product stock in the cloud
    new_stock = prod_data['stock'] - quantity
    prod_ref.update({'stock': new_stock})
    

    print(f" Order successfully created for {user_name}. Total to pay: ${total}")
    print(f" Stock for '{prod_data['name']}' updated to {new_stock}.")

# --- MAIN MENU ---
def main_menu():
    while True:
        print("\n" + "="*30)
        print(" E-COMMERCE CLOUD DATABASE ")
        print("="*30)
        print("1. Add a product")
        print("2. View all products")
        print("3. Delete a product")
        print("4. Register a user")
        print("5. Create an order")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            view_products()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            register_user()
        elif choice == '5':
            create_order()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main_menu()
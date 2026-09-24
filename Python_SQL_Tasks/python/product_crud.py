import mysql.connector


def get_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="product_db"
    )

    return connection


# CREATE - Add Product
def add_product():

    connection = get_connection()
    cursor = connection.cursor()

    product_name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    query = """
    INSERT INTO products
    (Product_Name, Category, Price, Quantity)
    VALUES (%s, %s, %s, %s)
    """

    values = (product_name, category, price, quantity)

    cursor.execute(query, values)
    connection.commit()

    print("Product added successfully.")

    cursor.close()
    connection.close()


# READ - View Products
def view_products():

    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM products"

    cursor.execute(query)

    products = cursor.fetchall()

    print("\n----- Product List -----")

    for product in products:

        print("Product ID:", product[0])
        print("Product Name:", product[1])
        print("Category:", product[2])
        print("Price:", product[3])
        print("Quantity:", product[4])
        print("------------------------")

    cursor.close()
    connection.close()


# UPDATE - Update Product
def update_product():

    connection = get_connection()
    cursor = connection.cursor()

    product_id = int(input("Enter Product ID: "))
    new_price = float(input("Enter New Price: "))

    query = """
    UPDATE products
    SET Price = %s
    WHERE Product_ID = %s
    """

    values = (new_price, product_id)

    cursor.execute(query, values)

    connection.commit()

    if cursor.rowcount > 0:
        print("Product updated successfully.")
    else:
        print("Product not found.")

    cursor.close()
    connection.close()


# DELETE - Delete Product
def delete_product():

    connection = get_connection()
    cursor = connection.cursor()

    product_id = int(input("Enter Product ID: "))

    query = """
    DELETE FROM products
    WHERE Product_ID = %s
    """

    cursor.execute(query, (product_id,))

    connection.commit()

    if cursor.rowcount > 0:
        print("Product deleted successfully.")
    else:
        print("Product not found.")

    cursor.close()
    connection.close()


# MENU
def main():

    while True:

        print("\n===== Product CRUD =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            update_product()

        elif choice == "4":
            delete_product()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
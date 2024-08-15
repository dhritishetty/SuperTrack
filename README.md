# SuperTrack: Supermarket Management System
This is a Python-based project for managing supermarket inventory. The system allows employees to perform various operations such as adding new items, updating existing items, searching for items, restocking items, and managing discounts. The data is stored in a MySQL database.

## Features - 
- **Insert Records:** Add new items to the supermarket inventory.
- **Display Records:** View all the items in the inventory.
- **Search Records:** Search for specific items using the item code.
- **Update Records:** Modify details of existing items in the inventory.
- **Delete Records:** Remove items from the inventory.
- **Restock Items:** Add more stock to existing items.
- **Manage Discounts:** Increase or decrease item discount percentage.

## Technologies Used -
- **Python:** The main programming language used for the project.
- **MySQL:** The database system stores and manages inventory data.
- **MySQL Connector:** A Python library used to connect Python applications to MySQL databases.

## Installation-
1. **Clone the repository**
   ```bash
    git clone https://github.com/dhritishetty/SuperTrack.git
    ```
2. **Install MySQL:**
    - Install MySQL on your system if not already installed.
3. **Install MySQL Connector:**
    ```bash
    pip install mysql-connector-python
    ```
4. **Set up the database:**
    - Create a MySQL database named `smktmngmt`.
    - Create a table in the database with the following structure:
        ```sql
        CREATE TABLE supermarket (
        ItemCode VARCHAR(10) PRIMARY KEY,
        ItemName VARCHAR(30),
        BrandName VARCHAR(30),
        QuantityAvailable INT DEFAULT 0,
        MRP DECIMAL(6,2),
        DiscountPercentage DECIMAL(6,2),
        DiscountedPrice DECIMAL(6,2)
        );
        ```

## Usage

- Run the `supermarket.py` script to start the program.
- Follow the on-screen menu to perform various inventory management tasks.

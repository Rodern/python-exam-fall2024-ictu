import sqlite3
from sqlite3 import Error

# Function to create a database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established.")
    except Error as e:
        print(e)
    return conn

# Function to create a table
def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)

# Function to create cursor
def create_cursor(conn):
    try:
        return conn.cursor()
    except Error as e:
        print(e)

def create_inventory_db():
    return InventoryPlusDB('db/inventoryplus.db')


class InventoryPlusDB:
    def __init__(self, db_file):
        self.conn = create_connection(db_file)
        self.create_tables()

    def create_tables(self):
        # SQL statements for creating tables (same as before)
        create_address_table = """
        CREATE TABLE IF NOT EXISTS address (
            addressId INTEGER PRIMARY KEY AUTOINCREMENT,
            cityId INTEGER NOT NULL,
            regionId INTEGER NOT NULL,
            countyId INTEGER NOT NULL,
            street_one TEXT NOT NULL,
            street_two TEXT NOT NULL,
            FOREIGN KEY (cityId) REFERENCES city (cityId),
            FOREIGN KEY (regionId) REFERENCES region (regionId),
            FOREIGN KEY (countyId) REFERENCES country (countryId)
        );"""

        create_budget_table = """
        CREATE TABLE IF NOT EXISTS budget (
            budgetId INTEGER PRIMARY KEY AUTOINCREMENT,
            userId TEXT NOT NULL,
            name TEXT NOT NULL,
            total_amount REAL NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            date_created TEXT NOT NULL,
            last_modified TEXT NOT NULL,
            FOREIGN KEY (userId) REFERENCES user (userId)
        );"""

        create_category_table = """
        CREATE TABLE IF NOT EXISTS category (
            categoryId INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        );"""

        create_city_table = """
        CREATE TABLE IF NOT EXISTS city (
            cityId INTEGER PRIMARY KEY AUTOINCREMENT,
            countryId INTEGER NOT NULL,
            guid TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            FOREIGN KEY (countryId) REFERENCES country (countryId)
        );"""

        create_country_table = """
        CREATE TABLE IF NOT EXISTS country (
            countryId INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            code TEXT NOT NULL,
            dial_code INTEGER NOT NULL,
            symbol TEXT NOT NULL,
            capital TEXT NOT NULL,
            currency TEXT NOT NULL,
            continent TEXT NOT NULL,
            continent_code TEXT NOT NULL,
            alpha_3 TEXT NOT NULL
        );"""

        create_financial_goal_table = """
        CREATE TABLE IF NOT EXISTS financial_goal (
            goalId INTEGER PRIMARY KEY AUTOINCREMENT,
            userId TEXT NOT NULL,
            name TEXT NOT NULL,
            target_amount REAL NOT NULL,
            current_amount REAL NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            date_created TEXT NOT NULL,
            last_modified TEXT NOT NULL,
            FOREIGN KEY (userId) REFERENCES user (userId)
        );"""

        create_income_table = """
        CREATE TABLE IF NOT EXISTS income (
            incomeId INTEGER PRIMARY KEY AUTOINCREMENT,
            userId TEXT NOT NULL,
            source TEXT CHECK(source IN ('Job','Business','Allowance','Other')) NOT NULL,
            amount REAL NOT NULL,
            date_added TEXT NOT NULL,
            FOREIGN KEY (userId) REFERENCES user (userId)
        );"""

        create_inventory_item_table = """
        CREATE TABLE IF NOT EXISTS inventory_item (
            itemId TEXT PRIMARY KEY,
            userId TEXT NOT NULL,
            categoryId INTEGER,
            spaceId INTEGER,
            manufacturerId INTEGER,
            name TEXT NOT NULL,
            value REAL NOT NULL,
            item_count INTEGER NOT NULL,
            description TEXT NOT NULL,
            purchase_date TEXT NOT NULL,
            date_manufactured TEXT NOT NULL,
            expiry_date TEXT NOT NULL,
            warranty INTEGER NOT NULL,
            barcode TEXT NOT NULL UNIQUE,
            date_created TEXT NOT NULL,
            last_modified TEXT NOT NULL,
            FOREIGN KEY (categoryId) REFERENCES category (categoryId),
            FOREIGN KEY (userId) REFERENCES user (userId),
            FOREIGN KEY (manufacturerId) REFERENCES manufacturer (manufacturerId)
        );"""

        create_manufacturer_table = """
        CREATE TABLE IF NOT EXISTS manufacturer (
            manufacturerId INTEGER PRIMARY KEY AUTOINCREMENT,
            addressId INTEGER,
            name TEXT NOT NULL,
            logo_url TEXT NOT NULL,
            website TEXT NOT NULL,
            email TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            date_created TEXT NOT NULL,
            last_modified TEXT NOT NULL,
            FOREIGN KEY (addressId) REFERENCES address (addressId)
        );"""

        create_region_table = """
        CREATE TABLE IF NOT EXISTS region (
            regionId INTEGER PRIMARY KEY AUTOINCREMENT,
            countryId INTEGER NOT NULL,
            guid TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            short_code TEXT NOT NULL,
            capital_city INTEGER NOT NULL,
            latitude TEXT NOT NULL,
            longitude TEXT NOT NULL,
            FOREIGN KEY (countryId) REFERENCES country (countryId)
        );"""

        create_space_table = """
        CREATE TABLE IF NOT EXISTS space (
            spaceId INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT CHECK(type IN ('Parlour','Kitchen','Room','Garage','Basement')) NOT NULL,
            description TEXT NOT NULL
        );"""

        create_financial_transaction_table = """
        CREATE TABLE IF NOT EXISTS financial_transaction (
            transactionId INTEGER PRIMARY KEY AUTOINCREMENT,
            userId TEXT NOT NULL,
            walletId INTEGER,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            description TEXT NOT NULL,
            type TEXT CHECK(type IN ('Income','Expense')) NOT NULL,
            last_modified TEXT NOT NULL,
            FOREIGN KEY (userId) REFERENCES user (userId),
            FOREIGN KEY (walletId) REFERENCES wallet (walletId)
        );"""

        create_user_table = """
        CREATE TABLE IF NOT EXISTS user (
            userId TEXT PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            role TEXT CHECK(role IN ('Father','Mother','Child','Relative','Guest', 'User')) NOT NULL,
            date_created TEXT NOT NULL,
            last_modified TEXT NOT NULL
        );"""

        create_wallet_table = """
        CREATE TABLE IF NOT EXISTS wallet (
            walletId INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            date_created TEXT NOT NULL,
            last_modified TEXT NOT NULL
        );"""

        # Create all tables
        self.create_table(create_address_table)
        self.create_table(create_budget_table)
        self.create_table(create_category_table)
        self.create_table(create_city_table)
        self.create_table(create_country_table)
        self.create_table(create_financial_goal_table)
        self.create_table(create_income_table)
        self.create_table(create_inventory_item_table)
        self.create_table(create_manufacturer_table)
        self.create_table(create_region_table)
        self.create_table(create_space_table)
        self.create_table(create_financial_transaction_table)
        self.create_table(create_user_table)
        self.create_table(create_wallet_table)

    def create_table(self, create_table_sql):
        create_table(self.conn, create_table_sql)

    # CRUD methods for Address
    def create_address(self, cityId, regionId, countyId, street_one, street_two):
        sql = '''INSERT INTO address(cityId, regionId, countyId, street_one, street_two)
                 VALUES(?, ?, ?, ?, ?)'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (cityId, regionId, countyId, street_one, street_two))
        self.conn.commit()
        return cur.lastrowid

    def read_address(self, addressId):
        sql = '''SELECT * FROM address WHERE addressId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (addressId,))
        return cur.fetchone()

    def update_address(self, addressId, cityId, regionId, countyId, street_one, street_two):
        sql = '''UPDATE address
                 SET cityId = ?, regionId = ?, countyId = ?, street_one = ?, street_two = ?
                 WHERE addressId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (cityId, regionId, countyId, street_one, street_two, addressId))
        self.conn.commit()

    def delete_address(self, addressId):
        sql = '''DELETE FROM address WHERE addressId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (addressId,))
        self.conn.commit()

    # CRUD methods for Budget
    def create_budget(self, userId, name, total_amount, start_date, end_date, date_created, last_modified):
        sql = '''INSERT INTO budget(userId, name, total_amount, start_date, end_date, date_created, last_modified)
                 VALUES(?, ?, ?, ?, ?, ?, ?)'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (userId, name, total_amount, start_date, end_date, date_created, last_modified))
        self.conn.commit()
        return cur.lastrowid

    def read_budget(self, budgetId):
        sql = '''SELECT * FROM budget WHERE budgetId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (budgetId,))
        return cur.fetchone()

    def update_budget(self, budgetId, userId, name, total_amount, start_date, end_date, date_created, last_modified):
        sql = '''UPDATE budget
                 SET userId = ?, name = ?, total_amount = ?, start_date = ?, end_date = ?, date_created = ?, last_modified = ?
                 WHERE budgetId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (userId, name, total_amount, start_date, end_date, date_created, last_modified, budgetId))
        self.conn.commit()

    def delete_budget(self, budgetId):
        sql = '''DELETE FROM budget WHERE budgetId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (budgetId,))
        self.conn.commit()

    # CRUD methods for Category
    def create_category(self, name, description):
        sql = '''INSERT INTO category(name, description)
                 VALUES(?, ?)'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (name, description))
        self.conn.commit()
        return cur.lastrowid

    def read_category(self, categoryId):
        sql = '''SELECT * FROM category WHERE categoryId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (categoryId,))
        return cur.fetchone()

    def update_category(self, categoryId, name, description):
        sql = '''UPDATE category
                 SET name = ?, description = ?
                 WHERE categoryId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (name, description, categoryId))
        self.conn.commit()

    def delete_category(self, categoryId):
        sql = '''DELETE FROM category WHERE categoryId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (categoryId,))
        self.conn.commit()

    # CRUD methods for City
    def create_city(self, countryId, guid, name, latitude, longitude):
        sql = '''INSERT INTO city(countryId, guid, name, latitude, longitude)
                 VALUES(?, ?, ?, ?, ?)'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (countryId, guid, name, latitude, longitude))
        self.conn.commit()
        return cur.lastrowid

    def read_city(self, cityId):
        sql = '''SELECT * FROM city WHERE cityId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (cityId,))
        return cur.fetchone()

    def update_city(self, cityId, countryId, guid, name, latitude, longitude):
        sql = '''UPDATE city
                 SET countryId = ?, guid = ?, name = ?, latitude = ?, longitude = ?
                 WHERE cityId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (countryId, guid, name, latitude, longitude, cityId))
        self.conn.commit()

    def delete_city(self, cityId):
        sql = '''DELETE FROM city WHERE cityId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (cityId,))
        self.conn.commit()

    # CRUD methods for Country
    def create_country(self, name, code, dial_code, symbol, capital, currency, continent, continent_code, alpha_3):
        sql = '''INSERT INTO country(name, code, dial_code, symbol, capital, currency, continent, continent_code, alpha_3)
                 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (name, code, dial_code, symbol, capital, currency, continent, continent_code, alpha_3))
        self.conn.commit()
        return cur.lastrowid

    def read_country(self, countryId):
        sql = '''SELECT * FROM country WHERE countryId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (countryId,))
        return cur.fetchone()

    def update_country(self, countryId, name, code, dial_code, symbol, capital, currency, continent, continent_code, alpha_3):
        sql = '''UPDATE country
                 SET name = ?, code = ?, dial_code = ?, symbol = ?, capital = ?, currency = ?, continent = ?, continent_code = ?, alpha_3 = ?
                 WHERE countryId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (name, code, dial_code, symbol, capital, currency, continent, continent_code, alpha_3, countryId))
        self.conn.commit()

    def delete_country(self, countryId):
        sql = '''DELETE FROM country WHERE countryId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (countryId,))
        self.conn.commit()

    # CRUD methods for Financial Goal
    def create_financial_goal(self, userId, name, target_amount, current_amount, start_date, end_date, date_created, last_modified):
        sql = '''INSERT INTO financial_goal(userId, name, target_amount, current_amount, start_date, end_date, date_created, last_modified)
                 VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (userId, name, target_amount, current_amount, start_date, end_date, date_created, last_modified))
        self.conn.commit()
        return cur.lastrowid

    def read_financial_goal(self, goalId):
        sql = '''SELECT * FROM financial_goal WHERE goalId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (goalId,))
        return cur.fetchone()

    def update_financial_goal(self, goalId, userId, name, target_amount, current_amount, start_date, end_date, date_created, last_modified):
        sql = '''UPDATE financial_goal
                 SET userId = ?, name = ?, target_amount = ?, current_amount = ?, start_date = ?, end_date = ?, date_created = ?, last_modified = ?
                 WHERE goalId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (userId, name, target_amount, current_amount, start_date, end_date, date_created, last_modified, goalId))
        self.conn.commit()

    def delete_financial_goal(self, goalId):
        sql = '''DELETE FROM financial_goal WHERE goalId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (goalId,))
        self.conn.commit()

    # CRUD methods for Income
    def create_income(self, userId, source, amount, date_added):
        sql = '''INSERT INTO income(userId, source, amount, date_added)
                 VALUES(?, ?, ?, ?)'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (userId, source, amount, date_added))
        self.conn.commit()
        return cur.lastrowid

    def read_income(self, incomeId):
        sql = '''SELECT * FROM income WHERE incomeId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (incomeId,))
        return cur.fetchone()

    def update_income(self, incomeId, userId, source, amount, date_added):
        sql = '''UPDATE income
                 SET userId = ?, source = ?, amount = ?, date_added = ?
                 WHERE incomeId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (userId, source, amount, date_added, incomeId))
        self.conn.commit()

    def delete_income(self, incomeId):
        sql = '''DELETE FROM income WHERE incomeId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (incomeId,))
        self.conn.commit()

    # CRUD methods for Inventory Item
    def create_inventory_item(self, itemId, userId, categoryId, spaceId, manufacturerId, name, value, item_count, description, purchase_date, date_manufactured, expiry_date, warranty, barcode, date_created, last_modified):
        sql = '''INSERT INTO inventory_item(itemId, userId, categoryId, spaceId, manufacturerId, name, value, item_count, description, purchase_date, date_manufactured, expiry_date, warranty, barcode, date_created, last_modified)
                 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (itemId, userId, categoryId, spaceId, manufacturerId, name, value, item_count, description, purchase_date, date_manufactured, expiry_date, warranty, barcode, date_created, last_modified))
        self.conn.commit()
        return cur.lastrowid

    def read_inventory_item(self, itemId):
        sql = '''SELECT * FROM inventory_item WHERE itemId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (itemId,))
        return cur.fetchone()

    def update_inventory_item(self, itemId, userId, categoryId, spaceId, manufacturerId, name, value, item_count, description, purchase_date, date_manufactured, expiry_date, warranty, barcode, date_created, last_modified):
        sql = '''UPDATE inventory_item
                 SET userId = ?, categoryId = ?, spaceId = ?, manufacturerId = ?, name = ?, value = ?, item_count = ?, description = ?, purchase_date = ?, date_manufactured = ?, expiry_date = ?, warranty = ?, barcode = ?, date_created = ?, last_modified = ?
                 WHERE itemId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (userId, categoryId, spaceId, manufacturerId, name, value, item_count, description, purchase_date, date_manufactured, expiry_date, warranty, barcode, date_created, last_modified, itemId))
        self.conn.commit()

    def delete_inventory_item(self, itemId):
        sql = '''DELETE FROM inventory_item WHERE itemId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (itemId,))
        self.conn.commit()

    # CRUD methods for Manufacturer
    def create_manufacturer(self, addressId, name, logo_url, website, email, phone_number, date_created, last_modified):
        sql = '''INSERT INTO manufacturer(addressId, name, logo_url, website, email, phone_number, date_created, last_modified)
                 VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (addressId, name, logo_url, website, email, phone_number, date_created, last_modified))
        self.conn.commit()
        return cur.lastrowid

    def read_manufacturer(self, manufacturerId):
        sql = '''SELECT * FROM manufacturer WHERE manufacturerId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (manufacturerId,))
        return cur.fetchone()

    def update_manufacturer(self, manufacturerId, addressId, name, logo_url, website, email, phone_number, date_created, last_modified):
        sql = '''UPDATE manufacturer
                 SET addressId = ?, name = ?, logo_url = ?, website = ?, email = ?, phone_number = ?, date_created = ?, last_modified = ?
                 WHERE manufacturerId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (addressId, name, logo_url, website, email, phone_number, date_created, last_modified, manufacturerId))
        self.conn.commit()

    def delete_manufacturer(self, manufacturerId):
        sql = '''DELETE FROM manufacturer WHERE manufacturerId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (manufacturerId,))
        self.conn.commit()

    # CRUD methods for Region
    def create_region(self, countryId, guid, name, short_code, capital_city, latitude, longitude):
        sql = '''INSERT INTO region(countryId, guid, name, short_code, capital_city, latitude, longitude)
                 VALUES(?, ?, ?, ?, ?, ?, ?)'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (countryId, guid, name, short_code, capital_city, latitude, longitude))
        self.conn.commit()
        return cur.lastrowid

    def read_region(self, regionId):
        sql = '''SELECT * FROM region WHERE regionId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (regionId,))
        return cur.fetchone()

    def update_region(self, regionId, countryId, guid, name, short_code, capital_city, latitude, longitude):
        sql = '''UPDATE region
                 SET countryId = ?, guid = ?, name = ?, short_code = ?, capital_city = ?, latitude = ?, longitude = ?
                 WHERE regionId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (countryId, guid, name, short_code, capital_city, latitude, longitude, regionId))
        self.conn.commit()

    def delete_region(self, regionId):
        sql = '''DELETE FROM region WHERE regionId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (regionId,))
        self.conn.commit()

    # CRUD methods for Space
    def create_space(self, name, type, description):
        sql = '''INSERT INTO space(name, type, description)
                 VALUES(?, ?, ?)'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (name, type, description))
        self.conn.commit()
        return cur.lastrowid

    def read_space(self, spaceId):
        sql = '''SELECT * FROM space WHERE spaceId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (spaceId,))
        return cur.fetchone()

    def update_space(self, spaceId, name, type, description):
        sql = '''UPDATE space
                 SET name = ?, type = ?, description = ?
                 WHERE spaceId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (name, type, description, spaceId))
        self.conn.commit()

    def delete_space(self, spaceId):
        sql = '''DELETE FROM space WHERE spaceId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (spaceId,))
        self.conn.commit()

    # CRUD methods for Transaction
    def create_financial_transaction(self, userId, walletId, amount, date, description, type, last_modified):
        sql = '''INSERT INTO financial_transaction(userId, walletId, amount, date, description, type, last_modified)
                 VALUES(?, ?, ?, ?, ?, ?, ?)'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (userId, walletId, amount, date, description, type, last_modified))
        self.conn.commit()
        return cur.lastrowid

    def read_financial_transaction(self, transactionId):
        sql = '''SELECT * FROM financial_transaction WHERE transactionId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (transactionId,))
        return cur.fetchone()

    def update_financial_transaction(self, transactionId, userId, walletId, amount, date, description, type, last_modified):
        sql = '''UPDATE financial_transaction
                 SET userId = ?, walletId = ?, amount = ?, date = ?, description = ?, type = ?, last_modified = ?
                 WHERE transactionId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (userId, walletId, amount, date, description, type, last_modified, transactionId))
        self.conn.commit()

    def delete_financial_transaction(self, transactionId):
        sql = '''DELETE FROM financial_transaction WHERE transactionId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (transactionId,))
        self.conn.commit()

    # CRUD methods for User
    def create_user(self, userId, username, password, email, first_name, last_name, phone_number, role, date_created, last_modified):
        sql = '''INSERT INTO user(userId, username, password, email, first_name, last_name, phone_number, role, date_created, last_modified)
                 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (userId, username, password, email, first_name, last_name, phone_number, role, date_created, last_modified))
        self.conn.commit()
        return cur.lastrowid

    def read_user(self, userId):
        sql = '''SELECT * FROM user WHERE userId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (userId,))
        return cur.fetchone()

    def read_users(self):
        sql = '''SELECT * FROM user'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql)
        return cur.fetchall()

    def update_user(self, userId, username, password, email, first_name, last_name, phone_number, role, date_created, last_modified):
        sql = '''UPDATE user
                 SET username = ?, password = ?, email = ?, first_name = ?, last_name = ?, phone_number = ?, role = ?, date_created = ?, last_modified = ?
                 WHERE userId = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, (username, password, email, first_name, last_name, phone_number, role, date_created, last_modified, userId))
        self.conn.commit()

    def delete_user(self, userId):
        sql = '''DELETE FROM user WHERE userId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (userId,))
        self.conn.commit()

    # CRUD methods for Wallet
    def create_wallet(self, amount, date_created, last_modified):
        sql = '''INSERT INTO wallet(amount, date_created, last_modified)
                 VALUES(?, ?, ?)'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (amount, date_created, last_modified))
        self.conn.commit()
        return cur.lastrowid

    def read_wallet(self, walletId):
        sql = '''SELECT * FROM wallet WHERE walletId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (walletId,))
        return cur.fetchone()

    def update_wallet(self, walletId, amount, date_created, last_modified):
        sql = '''UPDATE wallet
                 SET amount = ?, date_created = ?, last_modified = ?
                 WHERE walletId = ?'''
        cur = self.conn.cursor()
        
        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (amount, date_created, last_modified, walletId))
        self.conn.commit()

    def delete_wallet(self, walletId):
        sql = '''DELETE FROM wallet WHERE walletId = ?'''
        cur = self.conn.cursor()

        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, (walletId,))
        self.conn.commit()

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Connection closed.")
    
    # CRUD operations
    def create_record(self, table, data):
        placeholders = ', '.join(['?'] * len(data))
        columns = ', '.join(data.keys())
        sql = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
        cur = self.conn.cursor()

        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, list(data.values()))
        self.conn.commit()

    def read_record(self, table, condition):
        sql = f'SELECT * FROM {table} WHERE {condition}'
        cur = self.conn.cursor()

        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql)
        val = cur.fetchone()
        return val

    def update_record(self, table, updates, condition):
        set_clause = ', '.join([f'{k} = ?' for k in updates.keys()])
        sql = f'UPDATE {table} SET {set_clause} WHERE {condition}'
        cur = self.conn.cursor()

        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql, list(updates.values()))
        self.conn.commit()

    def delete_record(self, table, condition):
        sql = f'DELETE FROM {table} WHERE {condition}'
        cur = self.conn.cursor()

        # Enable foreign key support
        cur.execute('PRAGMA foreign_keys = ON;')

        cur.execute(sql)
        self.conn.commit()

# Example usage
if __name__ == '__main__':
    try:
        db = create_inventory_db()

        # Example CRUD operations
        # Create a new user
        userId = db.create_user("1", "john_doe", "password123", "john@example.com", "John", "Doe", "123456789", "Father", "2023-01-01", "2023-01-01")
        print("User created with ID:", userId)

        # Read user
        user = db.read_user("1")
        print("User details:", user)

        # Update user
        db.update_user("1", "john_doe_updated", "newpassword", "john_updated@example.com", "John", "Doe", "987654321", "Father", "2023-01-01", "2023-01-01")

        # Read updated user
        user = db.read_user("1")
        print("Updated user details:", user)

        # Delete user
        #db.delete_user("1")
        print("User deleted.")

        # Don't forget to close the connection
        db.close_connection()
    except:
        print("An exception occurred!")
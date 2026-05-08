import sqlite3

def init_db():
    conn = sqlite3.connect('bus_system.db')
    cursor = conn.cursor()
    
    # Create the table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            card_id TEXT PRIMARY KEY, 
            password TEXT, 
            balance REAL
        )
    ''')
    
    # Add a test user
    cursor.execute("INSERT OR IGNORE INTO accounts VALUES ('LION-001', '1234', 1000.0)")
    
    conn.commit()
    conn.close()
    print("✅ Database created and test user (LION-001) added!")

if __name__ == '__main__':
    init_db()
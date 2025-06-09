import json
import sqlite3

# Load JSON data
with open('data.json') as f:
    data = json.load(f)

print('data',data)

# Connect to SQLite (or create)
conn = sqlite3.connect('my_database.db')
c = conn.cursor()

# Create table (adjust fields/types as needed)



# Insert data
for entry in data:
    print('entry',entry)
    # c.execute('INSERT INTO users (id, name, age) VALUES (?, ?, ?)',
    #           (entry['id'], entry['name'], entry['age']))

# # Commit and close
conn.commit()
conn.close()
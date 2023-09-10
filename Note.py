
import tkinter as tk
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",
    database="update_qustion"
)

# Create a cursor object
mycursor = conn.cursor()

# Execute the SELECT query to fetch data from the table
query = 'SELECT * FROM answer'
mycursor.execute(query)

# Fetch all rows from the result set
data = mycursor.fetchall()

# Create a Tkinter window
root = tk.Tk()

# Create a text area to display the data
text_area = tk.Text(root)
text_area.pack()

# Insert the data into the text area
for row in data:
    text_area.insert(tk.END, str(row) + "\n")

# Close the cursor and the database connection
mycursor.close()
conn.close()

# Run the Tkinter event loop
root.mainloop()

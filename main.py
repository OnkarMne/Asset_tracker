from tkinter import *
from tkinter import messagebox
import mysql.connector
import login_form
import pandas as pd
from tkinter.ttk import Combobox
import openpyxl


def submit():
    emp_id = empid_entry.get()
    name = Name_entry.get()
    email = Email_entry.get()
    project = Project_entry.get()
    contact = contact_entry.get()
    address = Address_entry.get("1.0", END)
    reason = Reason_combobox.get()
    it_request = Itrequest_entry.get()
    comment = comment_entry.get("1.0", END)

    # Create a connection to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        port="3306",
        username="root",
        password="Solaris@123",
        database="my_db",
    )


    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()


    # Insert the data into the database
    query = "INSERT INTO asset_tracker (emp_id, name, email, project, contact, address, reason, it_request, comment, status) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (emp_id, name, email, project, contact, address, reason, it_request, comment, status.get())
    cursor.execute(query, values)
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    empid_entry.delete(0, END)
    Name_entry.delete(0, END)
    Email_entry.delete(0, END)
    Project_entry.delete(0, END)
    contact_entry.delete(0, END)
    Address_entry.delete("1.0", END)
    Itrequest_entry.delete(0, END)
    comment_entry.delete("1.0", END)

    messagebox.showinfo("Success", "Data submitted successfully")





def download_report():
    # Create a connection to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        port="3306",
        username="root",
        password="Solaris@123",
        database="my_db",
    )

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Execute the SELECT query to retrieve all data from the asset_tracker table
    query = "SELECT * FROM asset_tracker"
    cursor.execute(query)
    results = cursor.fetchall()
    #print(results)
    # Create a pandas DataFrame from the retrieved data
    columns = [column[0] for column in cursor.description]
    #print(columns)
    df = pd.DataFrame(results, columns=columns)
    #print(df)
    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Save the DataFrame as an Excel file
    df.to_excel("report.xlsx", index=False)
    messagebox.showinfo("Success", "Report downloaded successfully")


def search():
    emp_id = empid_entry.get()

    if emp_id == "":
        messagebox.showerror("Error", "Please enter Employee ID")
    else:
        # Create a connection to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            username="root",
            password="Solaris@123",
            database="my_db",
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute the SELECT query to retrieve data for the given Employee ID
        query = "SELECT * FROM asset_tracker WHERE emp_id = %s"
        values = (emp_id,)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            # Populate the fields with the retrieved data
            empid_entry.delete(0, END)
            empid_entry.insert(0, result[0])

            Name_entry.delete(0, END)
            Name_entry.insert(0, result[1])

            Email_entry.delete(0, END)
            Email_entry.insert(0, result[2])

            Project_entry.delete(0, END)
            Project_entry.insert(0, result[3])

            contact_entry.delete(0, END)
            contact_entry.insert(0, result[4])

            Address_entry.delete("1.0", END)
            Address_entry.insert(END, result[5])

            Reason_combobox.set(result[6])

            Itrequest_entry.delete(0, END)
            Itrequest_entry.insert(0, result[7])

            comment_entry.delete("1.0", END)
            comment_entry.insert(END, result[8])

            status.delete(0, END)
            status.insert(END, result[9])

        else:
            messagebox.showinfo("No Data", "No data found for the given Employee ID")

        # Close the cursor and connection
        cursor.close()
        connection.close()


window = Tk()
window.title("Asset Tracker")
window.config(padx=50, pady=50)

empid_label = Label(text="Employee ID:")
empid_label.grid(row=1, column=0)
empid_entry = Entry(width=20)
empid_entry.grid(row=1, column=1, padx=5)

Name_label = Label(text="Name:")
Name_label.grid(row=1, column=2)
Name_entry = Entry(width=30)
Name_entry.grid(row=1, column=3, padx=5)

Email_label = Label(text="Email:")
Email_label.grid(row=1, column=4)
Email_entry = Entry(width=30)
Email_entry.grid(row=1, column=5, padx=5)

Project_label = Label(text="Project name:")
Project_label.grid(row=2, column=0, pady=10)
Project_entry = Entry(width=20)
Project_entry.grid(row=2, column=1, padx=5, pady=10)


contact_label = Label(text="Contact Number:")
contact_label.grid(row=2, column=2, pady=10)
contact_entry = Entry(width=30)
contact_entry.grid(row=2, column=3, padx=5, pady=10)

Address_label = Label(text="Address:")
Address_label.grid(row=2, column=4, pady=10)
Address_entry = Text(height=2, width=30)
Address_entry.grid(row=2, column=5, padx=5, pady=10)


Reason_label = Label(text="Reason:")
Reason_label.grid(row=3, column=0, pady=5)
Reason_combobox = Combobox(values=["New Joinee", "Laptop issue"], width=20)
Reason_combobox.current(0)  # Set Open as the default option
Reason_combobox.grid(row=3, column=1)

Itrequest_label = Label(text="IT Request Ticket:")
Itrequest_label.grid(row=3, column=2, pady=10)
Itrequest_entry = Entry(width=30)
Itrequest_entry.grid(row=3, column=3, padx=5, pady=10)

comment_label = Label(text="Requester Comment:")
comment_label.grid(row=3, column=4, pady=10)
comment_entry = Text(height=2, width=30)
comment_entry.grid(row=3, column=5, padx=5, pady=10)

# menu = StringVar()
# menu.set("InProgress")

status_label = Label(text="STATUS:")
status_label.grid(row=4, column=2, padx=2)
status = Entry(width=30)
status.grid(row=4, column=3)


submit_button = Button(text="Submit", width=10, command=submit)
submit_button.grid(row=5, column=2, pady=10)

admin_button = Button(text="Admin", width=10, command=login_form.open_login_form)
admin_button.grid(row=5, column=3, pady=10)

search_button = Button(text="Search", width=10, command=search)
search_button.grid(row=5, column=4, pady=10)

download_button = Button(text="Download Report", width=20, command=download_report)
download_button.grid(row=5, column=5, pady=10)

window.mainloop()


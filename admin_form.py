from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter.ttk import Combobox


def open_admin_form():
    def update():
        emp_id = empid_entry.get()
        new_status = status_combobox.get()

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

            # Execute the UPDATE query to update the status for the given Employee ID
            query = "UPDATE asset_tracker SET status = %s WHERE emp_id = %s"
            values = (new_status, emp_id)
            cursor.execute(query, values)
            connection.commit()

            # Close the cursor and connection
            cursor.close()
            connection.close()

            messagebox.showinfo("Success", "Status updated successfully")




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

                status_combobox.set(result[9])

            else:
                messagebox.showinfo("No Data", "No data found for the given Employee ID")

            # Close the cursor and connection
            cursor.close()
            connection.close()

    #window.destroy()
    admin_window = Toplevel()
    admin_window.title("Admin_Form")
    admin_window.config(padx=50, pady=50)

    empid_label = Label(admin_window, text="Employee ID:")
    empid_label.grid(row=1, column=0)
    empid_entry = Entry(admin_window, width=20)
    empid_entry.grid(row=1, column=1, padx=5)

    Name_label = Label(admin_window, text="Name:")
    Name_label.grid(row=1, column=2)
    Name_entry = Entry(admin_window, width=30)
    Name_entry.grid(row=1, column=3, padx=5)

    Email_label = Label(admin_window, text="Email:")
    Email_label.grid(row=1, column=4)
    Email_entry = Entry(admin_window, width=30)
    Email_entry.grid(row=1, column=5, padx=5)

    Project_label = Label(admin_window, text="Project name:")
    Project_label.grid(row=2, column=0, pady=10)
    Project_entry = Entry(admin_window, width=20)
    Project_entry.grid(row=2, column=1, padx=5, pady=10)

    contact_label = Label(admin_window, text="Contact Number:")
    contact_label.grid(row=2, column=2, pady=10)
    contact_entry = Entry(admin_window, width=30)
    contact_entry.grid(row=2, column=3, padx=5, pady=10)

    Address_label = Label(admin_window, text="Address:")
    Address_label.grid(row=2, column=4, pady=10)
    Address_entry = Text(admin_window, height=2, width=30)
    Address_entry.grid(row=2, column=5, padx=5, pady=10)

    Reason_label = Label(admin_window, text="Reason:")
    Reason_label.grid(row=3, column=0, pady=5)
    Reason_combobox = Combobox(admin_window, values=["New Joinee", "Laptop issue"], width=27)
    Reason_combobox.current(0)  # Set Open as the default option
    Reason_combobox.grid(row=3, column=1)

    Itrequest_label = Label(admin_window, text="IT Request Ticket:")
    Itrequest_label.grid(row=3, column=2, pady=10)
    Itrequest_entry = Entry(admin_window, width=30)
    Itrequest_entry.grid(row=3, column=3, padx=5, pady=10)

    comment_label = Label(admin_window, text="Requester Comment:")
    comment_label.grid(row=3, column=4, pady=10)
    comment_entry = Text(admin_window, height=2, width=30)
    comment_entry.grid(row=3, column=5, padx=5, pady=10)

    # menu = StringVar()
    # menu.set("InProgress")

    status_label = Label(admin_window, text="STATUS:")
    status_label.grid(row=4, column=2, padx=2)
    status_combobox = Combobox(admin_window, values=["Open", "Inprogress", "Delivered"], width=27)
    status_combobox.current(0)  # Set Open as the default option
    status_combobox.grid(row=4, column=3)

    search_button = Button(admin_window, text="Search", width=10, command=search)
    search_button.grid(row=5, column=2, pady=10)

    # admin_button = Button(text="Admin", width=10)
    # admin_button.grid(row=5, column=3, pady=10)

    update_button = Button(admin_window, text="Update", width=10, command=update)
    update_button.grid(row=5, column=4, pady=10)

    #admin_window.mainloop()

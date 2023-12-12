# Importing tkinter and messagebox modules
import tkinter as tk
import tkinter.messagebox as mb

# Creating a root window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("300x400")

# Creating a list to store the tasks
tasks = []

# Creating a function to add a new task
def add_task():
    # Getting the task from the entry
    task = entry.get()
    # Checking if the task is not empty
    if task:
        # Appending the task to the list
        tasks.append(task)
        # Updating the listbox
        update_listbox()
        # Clearing the entry
        entry.delete(0, tk.END)
    else:
        # Showing an error message
        mb.showerror("Error", "Please enter a task")

# Creating a function to delete a selected task
def delete_task():
    # Getting the index of the selected task
    index = listbox.curselection()
    # Checking if the index is not empty
    if index:
        # Deleting the task from the list
        tasks.pop(index[0])
        # Updating the listbox
        update_listbox()
    else:
        # Showing an error message
        mb.showerror("Error", "Please select a task")

# Creating a function to update the listbox
def update_listbox():
    # Clearing the listbox
    listbox.delete(0, tk.END)
    # Looping through the tasks and inserting them into the listbox
    for task in tasks:
        listbox.insert(tk.END, task)

# Creating a label for the entry
label = tk.Label(root, text="Enter a task:")
label.pack(padx=10, pady=10)

# Creating an entry for the task
entry = tk.Entry(root)
entry.pack(padx=10, pady=10)

# Creating a button to add the task
add_button = tk.Button(root, text="Add", command=add_task)
add_button.pack(padx=10, pady=10)

# Creating a listbox to display the tasks
listbox = tk.Listbox(root)
listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Creating a button to delete the task
delete_button = tk.Button(root, text="Delete", command=delete_task)
delete_button.pack(padx=10, pady=10)

# Starting the main loop
root.mainloop()

from tkinter import *
from db import Database
from tkinter import messagebox

# making the db
db = Database('store.db')

# selected item variable for the listbox printing in entries
selected_item = ''


# to add data in list box, use this function if you make changes so that listbox data can also be changed
def populate_item():
    orders_list.delete(0, END)
    for row in db.fetch():
        orders_list.insert(END, row)


# adding data into database
def add_item():
    # if any fields are left
    if not Item_text.get() or not customer_text.get() or not seller_text.get() or not price_text.get():
        messagebox.showerror('Required Fields', "Please fill all the Fields!")
    else:
        # insertion of data
        db.insert(Item_text.get(), customer_text.get(), seller_text.get(), price_text.get())
        messagebox.showinfo('WORK DONE', "Information added")
        # used to make changes in listbox
        populate_item()
        # clearing the entries
        clear_txt()


# removing the data from data base
def rem_item():
    # removing the selected item from the list box
    db.remove(selected_item[0])
    # clearing all the entries
    clear_txt()
    # making changes in the listbox
    populate_item()


def update_item():
    db.update(selected_item[0], Item_text.get(), customer_text.get(), seller_text.get(), price_text.get())
    clear_txt()
    populate_item()


def clear_txt():
    global selected_item
    item_entry.delete(0, END)
    customer_entry.delete(0, END)
    seller_entry.delete(0, END)
    price_entry.delete(0, END)
    selected_item = ''


def select_item(item):
    clear_txt()

    # getting the value from list box
    global selected_item
    index = orders_list.curselection()[0]
    selected_item = orders_list.get(index)

    # printing all the values in the entry
    item_entry.insert(END, selected_item[1])
    customer_entry.insert(END, selected_item[2])
    seller_entry.insert(END, selected_item[3])
    price_entry.insert(END, selected_item[4])

# initializing tkinter
app = Tk()
# giving the title
app.title('Store Management')
# window size
app.geometry('700x350')

# ITEM LABEL AND ENTRY

# creating variable to hold the value of data entered into item entry
Item_text = StringVar()
# creating item label
item_label = Label(app, text="Item name", font=('bold', 13), pady=20, padx=20)
item_label.grid(row=0, column=0, sticky=W)
# creating item entry
item_entry = Entry(app, textvariable=Item_text)
item_entry.grid(row=0, column=1, pady=20)

customer_text = StringVar()
customer_label = Label(app, text="customer name", font=('bold', 13), pady=20, padx=20)
customer_label.grid(row=0, column=2, sticky=E)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3, pady=20)


seller_text = StringVar()
seller_label = Label(app, text="Retailer", font=('bold', 13), pady=20, padx=20)
seller_label.grid(row=2, column=0, sticky=W)
seller_entry = Entry(app, textvariable=seller_text)
seller_entry.grid(row=2, column=1, pady=20)

price_text = StringVar()
price_label = Label(app, text="Price", font=('bold', 13), pady=20, padx=20)
price_label.grid(row=2, column=2, sticky=E)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=2, column=3, pady=20)


add_btn = Button(app, text='Add order', width=12, command=add_item)
add_btn.grid(row=5, column=0, pady=20,padx=20)


rem_btn = Button(app, text='Remove order', width=12, command=rem_item)
rem_btn.grid(row=5, column=1, pady=20,padx=20)


update_btn = Button(app, text='Update order', width=12, command=update_item)
update_btn.grid(row=5, column=2, pady=20,padx=20)


clear_btn = Button(app, text='Clear all', width=12, command=clear_txt)
clear_btn.grid(row=5, column=3, pady=20,padx=20)


orders_list = Listbox(app, height=5, width=50, borderwidth=1)
orders_list.grid(row=7, column=0, columnspan=2, rowspan=6, padx=20, pady=20)

scroll_bar = Scrollbar(app, orient=VERTICAL, command=orders_list.yview)
scroll_bar.grid(row=7, column=0, columnspan=2, rowspan=6, sticky=E, pady=20)

orders_list.configure(yscrollcommand=scroll_bar.set)
orders_list.bind("<<ListboxSelect>>", select_item)


populate_item()

app.mainloop()
from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3

#Подключение к базе данных
conn = sqlite3.connect('database.db')
cur = conn.cursor()

#Создание окна программы
root = tk.Tk()
root.title('Список сотрудников компании')
root.geometry('1310x350')

#Функция создания таблицы ListOfCompanyEmployees в базе данных
def connect():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS ListOfCompanyEmployees(id TEXT, FullName TEXT,PhoneNumber TEXT, Email TEXT, Wage TEXT);")
    conn.commit()
    conn.close()

#Функция для очистки всей таблицы в базе данных
def clear():
    tree.delete(*tree.get_children())
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    sql_delete_query = """DELETE from ListOfCompanyEmployees"""
    conn.execute(sql_delete_query)
    conn.commit()
    conn.close()

#Функция для обновления информации в виджите Treeview из таблицы в базе данных
def openl():
    tree.delete(*tree.get_children())
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM ListOfCompanyEmployees")
    rows = cur.fetchall()
    for row in rows:
        tree.insert("",tk.END, text=row[0], values=row[1:])
    conn.close()

#Функция для добовления новой информации в таблицу в базе данных
def write():
    tree.delete(*tree.get_children())

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    try:
        cur.execute(
            "CREATE TABLE ListOfCompanyEmployees(id TEXT, FullName TEXT,PhoneNumber TEXT, Email TEXT, Wage TEXT);")
    except:
        pass

    cur.execute("INSERT INTO ListOfCompanyEmployees VALUES (?, ?, ?, ?, ?);",
                (name0_entry.get(), name1_entry.get(), name2_entry.get(), name3_entry.get(), name4_entry.get(), ))
    conn.commit()

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM ListOfCompanyEmployees")
    rows = cur.fetchall()
    for row in rows:
        tree.insert("",tk.END, text=row[0], values=row[1:])
    conn.close()

#Фунция для нахождения значения в таблице в базе данных
def findl():
    tree.delete(*tree.get_children())
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM ListOfCompanyEmployees")
    rows = cur.fetchall()
    for row in rows:
        if name1_entry.get() == row[1]:
            tree.insert("", tk.END, text=row[0], values=row[1:])
        conn.close()

#Функция для очистки вджета Treeview
def clear_table():
    tree.delete(*tree.get_children())

#Функция для удаления значения из таблицы в базе данных
def Delete_String():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM ListOfCompanyEmployees")
    query = 'DELETE FROM ListOfCompanyEmployees WHERE id =?'
    cur.execute(query, (name0_entry.get(),))
    conn.commit()
    conn.close()

    tree.delete(*tree.get_children())

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM ListOfCompanyEmployees")
    rows = cur.fetchall()
    for row in rows:
        tree.insert("", tk.END, text=row[0], values=row[1:])
    conn.close()

#Функция для изменения значений в базе данных
def ToСhangeTheData():
    tree.delete(*tree.get_children())

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    update_query = "UPDATE ListOfCompanyEmployees SET FullName=?, PhoneNumber=?, Email=?, Wage=? WHERE id=?"

    cur.execute(update_query, (name1_entry.get(), name2_entry.get(), name3_entry.get(), name4_entry.get(), name0_entry.get(),))
    conn.commit()
    conn.close()

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM ListOfCompanyEmployees")
    rows = cur.fetchall()
    for row in rows:
        tree.insert("", tk.END, text=row[0], values=row[1:])
    conn.close()

#Создание полей ввода в окне программы и их размещение по X и Y
name0_entry = Entry(bd = 1,width = 49)
name0_entry.insert(0, 'id')
name0_entry.place(x = 5, y = 3)

name1_entry = Entry(bd = 1,width = 49)
name1_entry.insert(0, 'ФИО')
name1_entry.place(x = 5, y = 21 + 3)

name2_entry = Entry(bd = 1,width = 49)
name2_entry.insert(0, 'Номер телефона')
name2_entry.place(x = 5, y = (21*2) + 3)

name3_entry = Entry(bd = 1,width = 49)
name3_entry.insert(0, 'Адрес электронной почты')
name3_entry.place(x = 5, y = 21*3 + 3)

name4_entry = Entry(bd = 1,width = 49)
name4_entry.insert(0, 'Заработная плата')
name4_entry.place(x = 5, y = 21*4 + 3)

#Создание текстовох меткок в окне программы и их размещение по X и Y
label0 = Label(bd = 1,width = 49, text='Основной функционал')
label0.place(x = -20, y = 110)
label1 = Label(bd = 1,width = 49, text='Дополнительный функционал')
label1.place(x = -20, y = 245)

#Создание кнопок в окне программы и их размещение по X и Y
message1button = Button(bd = 1,width = 41 ,text="Добавить нового сотрудника", command=write).place(x = 6, y = 135)
message2button = Button(bd = 1,width = 41 ,text="Измененить данные сотрудника по id",command=ToСhangeTheData).place(x = 6, y = 27 + 135)
message3button = Button(bd = 1,width = 41 ,text="Удалить сотрудника из базы данных по id", command=Delete_String).place(x = 6, y = (27*2) + 135)
message4button = Button(bd = 1,width = 41 ,text="Найти сотрудника по ФИО", command=findl).place(x = 6, y = (27*3) + 135)

message5button = Button(bd = 1,width = 41 ,text="Очистить таблицу", command=clear_table).place(x = 6, y = 270)
message6button = Button(bd = 1,width = 41 ,text="Очистить базу данных", command=clear).place(x = 6, y = 27 + 270)
message7button = Button(bd = 1,width = 41 ,text="Открыть базу данных", command=openl).place(x = 6, y = (27*2) + 270)

#Создание виджета Treeview и размещение его по X и Y
tree = ttk.Treeview(column=("column0" ,"column1", "column2", "column3" , "column4"))
tree.heading("#0" , text="id")
tree.heading("#1" , text="ФИО")
tree.heading("#2" , text="Номер телефона")
tree.heading("#3" , text="Адрес электронной почты")
tree.heading("#4" , text="Заработная плата")

tree.place(x = 310, y = 0)
tree.place(width = 1000,height = 349)

root.mainloop()

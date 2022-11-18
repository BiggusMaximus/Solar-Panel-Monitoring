import customtkinter
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import os
import sys
import csv
import dateutil
import matplotlib.dates as md
import PIL
import pandas as pd
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from matplotlib.figure import Figure
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


def on_closing(event=0):
    app.quit()

# Main Controller


app = customtkinter.CTk()
app.title("Solar Panel Monitoring")
app.iconbitmap('icon.ico')
app.state('zoomed')
app.protocol("WM_DELETE_WINDOW", on_closing)
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=20)
app.rowconfigure(tuple(range(5)), weight=1)


# Left Frame
left_frame = customtkinter.CTkFrame(app)
left_frame.columnconfigure(0, weight=1)
left_frame.columnconfigure(1, weight=1)
left_frame.rowconfigure(tuple(range(99)), weight=1)
left_frame.configure(corner_radius=0)
left_frame.grid(
    row=0,
    column=0,
    rowspan=99,
    sticky="NSEW")
# Title Frame Application
title_frame = customtkinter.CTkFrame(master=left_frame)
title_frame.grid(
    row=0,
    column=0,
    rowspan=99,
    columnspan=2,
    sticky="NSEW",
    padx=15,
)
title_frame.columnconfigure(0, weight=1)
title_frame.rowconfigure(0, weight=1)

title_frame2 = customtkinter.CTkFrame(master=title_frame)
title_frame2.grid(
    row=0,
    column=0,
    rowspan=99,
    columnspan=2,
    sticky="nsew",
    padx=15,
    pady=15
)
title_frame2.columnconfigure(0, weight=1)
title_frame2.rowconfigure(tuple(range(99)), weight=1)

title_app = customtkinter.CTkLabel(
    title_frame2,
    text="SOLAR MONITORING",
    text_color="white",
    corner_radius=8,
    text_font=("Times", 16, "bold"),
    height=100,
    fg_color=(
        "white", "gray38"),
    justify=CENTER
)

title_app.grid(row=0, column=0,
               sticky="NSEW", padx=5, pady=(10, 5)
               )


# Combobox choose device
device_value = customtkinter.StringVar(value="Device 1")


def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)
    # Device
    columns = ('Parameter', 'Value')
    device_tree = ttk.Treeview(
        title_frame2,
        columns=columns,
        show='headings',
        height=5
    )
    device_tree.heading('Parameter', text='Parameter')
    device_tree.heading('Value', text='Value')
    col_width = device_tree.winfo_width()
    device_tree.column("# 1", anchor=CENTER, width=col_width)
    device_tree.column("# 2", anchor=CENTER, width=col_width)
    if choice == 'Device 1':
        device_tree.delete(*device_tree.get_children())
        device_tree.insert("", 'end', values=('Pmax', '50W'))
        device_tree.insert("", 'end', values=('Vmp', '18V'))
        device_tree.insert("", 'end', values=('Imp', '2.78A'))
        device_tree.insert("", 'end', values=('Voc', '22.11V'))
        device_tree.insert("", 'end', values=('Isc', '2.94'))

    elif choice == 'Device 2':
        device_tree.delete(*device_tree.get_children())
        device_tree.insert("", 'end', values=('Pmax', '10W'))
        device_tree.insert("", 'end', values=('Vmp', '18V'))
        device_tree.insert("", 'end', values=('Imp', '0.53A'))
        device_tree.insert("", 'end', values=('Voc', '18V'))
        device_tree.insert("", 'end', values=('Isc', '0.53A'))

    device_tree.grid(row=2, rowspan=1, column=0, padx=5,
                     sticky="ew")


choose_device = customtkinter.CTkComboBox(
    master=title_frame2,
    values=["Device 1", "Device 2"],
    variable=device_value,
    command=combobox_callback
)
choose_device.grid(row=1, padx=5, sticky="we")


# Status Connected
status_connect_label = customtkinter.CTkLabel(master=title_frame2,
                                              text="Connected",
                                              corner_radius=6,  # <- custom corner radius
                                              # <- custom tuple-color
                                                   fg_color=(
                                                       "white", "gray38"),
                                                   justify=LEFT)
status_connect_label.grid(row=3,  column=0, sticky="ew", padx=5, pady=5)

# Connect to Device
connect_device_button = customtkinter.CTkButton(
    title_frame2, text="Connect To Device", border_width=0.5, border_color="black")
connect_device_button.grid(row=4,  column=0, sticky="ew", padx=5)

# imgss
image = PIL.Image.open("logo.png")
basewidth = 200
wpercent = (basewidth/float(image.size[0]))
hsize = int((float(image.size[1])*float(wpercent)))
image = image.resize((basewidth, hsize), PIL.Image.Resampling.LANCZOS)
image = PIL.ImageTk.PhotoImage(image)
image_label = Label(title_frame2, image=image, background="#2a2d2e")
image_label.grid(
    row=90, column=0, columnspan=2, sticky=N+W+E)

# Right Frame
right_frame = customtkinter.CTkFrame(master=app)
right_frame.columnconfigure(0, weight=1)
right_frame.rowconfigure(tuple(range(99)), weight=1)
right_frame.configure(corner_radius=0)
right_frame.grid(
    row=0,
    column=1,
    rowspan=5,
    padx=20, pady=20,
    sticky="nsew")

# Graph
graph_frame = customtkinter.CTkFrame(master=right_frame)
graph_frame.grid(
    row=0,
    column=0,
    rowspan=90,
    sticky="nsew",
    padx=5,
    pady=1
)
graph_frame.columnconfigure(0, weight=1)
graph_frame.columnconfigure(1, weight=1)
graph_frame.rowconfigure(0, weight=1)
graph_frame.rowconfigure(1, weight=1)


plt.style.use('seaborn-dark-palette')
df = pd.read_csv('data.csv')
datestrings = df['time']
dates = [dateutil.parser.parse(s) for s in datestrings]
xfmt = md.DateFormatter('%H:%M:%S')

m = 0.3
n = 0.3
bottom = 0.25
right = 0.01
left = 0.1
top = 0.26

# Current
fig_cur, ax_curr = plt.subplots(figsize=(m, n))
ax_curr.set_xticks(dates)

canvas_curr = FigureCanvasTkAgg(fig_cur, graph_frame)
canvas_curr.get_tk_widget().grid(column=0, row=0, sticky=N+S+E+W)

ax_curr.xaxis.set_major_formatter(xfmt)
ax_curr.yaxis.set_major_locator(MaxNLocator(prune='lower'))
ax_curr.plot(dates, df['current'], "o-")
ax_curr.set_title("Current (A)")
ax_curr.tick_params(axis='both', which='major', labelsize=7)
fig_cur.autofmt_xdate()
fig_cur.subplots_adjust(bottom=bottom)

# Voltage
fig_volt, ax_volt = plt.subplots(figsize=(m, n))
ax_volt.set_xticks(dates)

canvas_volt = FigureCanvasTkAgg(fig_volt, graph_frame)
canvas_volt.get_tk_widget().grid(column=1, row=0, sticky=N+S+E+W)
ax_volt.xaxis.set_major_formatter(xfmt)
ax_volt.yaxis.set_major_locator(MaxNLocator(prune='lower'))
ax_volt.plot(dates, df['voltage'], "o-")
ax_volt.set_title("Voltage (V)")
ax_volt.tick_params(axis='both', which='major', labelsize=7)
fig_volt.autofmt_xdate()
fig_volt.subplots_adjust(bottom=bottom)

# Power
fig_power, ax_power = plt.subplots(figsize=(m, n))
ax_power.set_xticks(dates)

canvas_power = FigureCanvasTkAgg(fig_power, graph_frame)
canvas_power.get_tk_widget().grid(column=0, row=1,  sticky=N+S+E+W)
ax_power.xaxis.set_major_formatter(xfmt)
ax_power.yaxis.set_major_locator(MaxNLocator(prune='lower'))
ax_power.plot(dates, df['power'], "o-")
ax_power.set_title("Power (W)")
ax_power.tick_params(axis='both', which='major', labelsize=7)
fig_power.autofmt_xdate()
fig_power.subplots_adjust(bottom=bottom)

# VI
fig_VI, ax_VI = plt.subplots(figsize=(m, n))
ax_VI.set_xticks(dates)

canvas_VI = FigureCanvasTkAgg(fig_VI, graph_frame)
canvas_VI.get_tk_widget().grid(column=1, row=1,  sticky=N+S+E+W)
ax_VI.xaxis.set_major_formatter(xfmt)
ax_VI.yaxis.set_major_locator(MaxNLocator(prune='lower'))
ax_VI.plot(dates, df['current'], "o-")
ax_VI.plot(dates, df['voltage'], "o-")
ax_VI.tick_params(axis='both', which='major', labelsize=7)
ax_VI.set_title("VI")
fig_VI.autofmt_xdate()
# fig_VI.subplots_adjust(bottom=bottom, top=top, right=right, left=left)


canvas_curr.draw()


# Table
table_frame = customtkinter.CTkFrame(
    master=right_frame)
table_frame.grid(
    row=90,
    column=0,
    rowspan=10,
    sticky="ew",
    padx=5
)
table_frame.columnconfigure(0, weight=1)
table_frame.columnconfigure(1, weight=10)
table_frame.rowconfigure(0, weight=1)

style = ttk.Style(table_frame)
# set ttk theme to "clam" which support the fieldbackground option
style.theme_use("clam")
style.configure(
    "Treeview",
    background="#247084",
    fieldbackground="#2a2d2e",
    foreground="#247084"
)
style.configure("Treeview.Heading", background="#247084",
                fieldbackground="white", foreground="white")
columns = ('Time', 'Voltage', 'Current', 'Power')
table_data = ttk.Treeview(
    table_frame,
    columns=columns,
    show='headings'
)

table_data.heading('Time', text='Time')
table_data.heading('Voltage', text='Voltage')
table_data.heading('Current', text='Current')
table_data.heading('Power', text='Power')
col_width = table_data.winfo_width()
table_data.column("# 1", anchor=CENTER, width=col_width)
table_data.column("# 2", anchor=CENTER, width=col_width)
table_data.column("# 3", anchor=CENTER, width=col_width)
table_data.column("# 4", anchor=CENTER, width=col_width)
table_data.grid(row=0,  column=0, columnspan=2, sticky="nsew")


scrollbar = Scrollbar(
    table_frame,
    orient=VERTICAL,
    command=table_data.yview,
    activebackground='#00ff00'
)
table_data.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=0, columnspan=2, sticky=N+S+E)


def save_as_file():
    lst = []
    col = ['Yaw', 'Pitch', 'Lift', 'Drag']
    if (len(table_data.get_children()) < 1):
        messagebox.showinfo("Empty Data")
    else:
        filename = filedialog.asksaveasfilename(
            initialdir=os.getcwd(),
            title="Save To Excel",
            filetypes=(("xlsx File", "*.xlsx"), ("All Files", "*.*"))
        )

        with open('temp.csv', mode='w', newline='') as f:
            csvwriter = csv.writer(f, delimiter=',')
            for row_id in table_data.get_children():
                row = table_data.item(row_id, 'values')
                lst.append(row)
            lst = list(map(list, lst))
            lst.insert(0, col)
            for row in lst:
                csvwriter.writerow(row)
        writer = pd.ExcelWriter(filename + '.xlsx')
        df = pd.read_csv('temp.csv', delimiter=',')
        df.to_excel(writer, 'sheetname')
        writer.save()


def load_data():
    filename = filedialog.askopenfilename(
        title="Open a File",
        filetype=(("xlxs files", ".*xlsx"), ("All Files", "*.*"))
    )
    filename = r"{}".format(filename)
    df = pd.read_excel(filename, index_col=False)

    # Clear all the previous data in tree
    table_data.delete(*table_data.get_children())
    # Add new data in Treeview widget

    for col in table_data["column"]:
        table_data.heading(col, text=col)

    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        table_data.insert("", "end", values=row)


save_to_excel_button = customtkinter.CTkButton(
    table_frame, text="Save To Excel", command=save_as_file, border_width=0.5, border_color="black").grid(row=1,  column=1, sticky=W+E)

import_to_excel_button = customtkinter.CTkButton(
    table_frame, text="Load Excel", command=load_data, border_width=0.5, border_color="black").grid(row=1,  column=0, sticky=W+E)

app.mainloop()

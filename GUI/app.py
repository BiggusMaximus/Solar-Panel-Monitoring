import tkinter
import tkinter.messagebox
import customtkinter
import serial.tools.list_ports
from matplotlib.ticker import MaxNLocator
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from matplotlib.figure import Figure

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import dateutil
import matplotlib.ticker as plticker

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Solar Panel Monitoring")
        self.iconbitmap('icon.ico')
        self.state('zoomed')
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=20)
        self.rowconfigure(tuple(range(5)), weight=1)

        # Port Frame
        self.port = Port(self)
        self.port.grid(row=0, column=0, rowspan=5,
                       sticky="nsew")

        # Graph and Table Frame
        self.port = LiveGraph(self)
        self.port.grid(row=0, column=1, rowspan=5,
                       padx=20, pady=20, sticky="nsew")

    def on_closing(self, event=0):
        self.destroy()


class LiveGraph(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(tuple(range(99)), weight=1)

        # Table
        self.table_frame = customtkinter.CTkFrame(master=self)
        self.table_frame.grid(
            row=80,
            column=0,
            sticky="NSEW",
            padx=5,
        )
        self.table_frame.columnconfigure(0, weight=1)
        self.table_frame.rowconfigure(0, weight=1)

        # Graph
        self.fig, self.ax = plt.subplots(222)
        self.df = pd.read_csv('data.csv')
        self.datestrings = self.df['time']
        self.dates = [dateutil.parser.parse(s) for s in self.datestrings]
        self.xfmt = md.DateFormatter('%H:%M:%S')
        print(self.dates)
        print(self.df['current'])
        self.ax[0, 0].plot(self.dates, self.df['current'], "o-")
        self.ax[0, 1].plot(self.dates, self.df['voltage'], "o-")
        self.ax[1, 0].plot(self.dates, self.df['power'], "o-")
        self.ax[1, 1].plot(self.df['voltage'], self.df['current'], "o-")
        self.graph_frame = customtkinter.CTkFrame(master=self)
        self.graph_frame.grid(
            row=0,
            column=0,
            rowspan=80,
            sticky="NSEW",
            padx=5,
            pady=5
        )
        self.graph_frame.columnconfigure(0, weight=1)
        self.graph_frame.rowconfigure(0, weight=1)
        self.plot_graph = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.plot_graph.draw()
        self.plot_graph.get_tk_widget().grid(row=0, column=0, sticky="nesw")


class Port(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Port Frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(tuple(range(99)), weight=1)
        self.configure(corner_radius=0)

        # Title Frame Application
        self.title_frame = customtkinter.CTkFrame(master=self)
        self.title_frame.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=5,
            pady=5
        )
        self.title_frame.columnconfigure(0, weight=1)
        self.title_frame.rowconfigure(0, weight=1)
        self.title_app = customtkinter.CTkLabel(
            self.title_frame,
            text="SOLAR MONITORING",
            text_color="white",
            corner_radius=10,
            text_font=("Roboto Medium", -15, "bold")
        )
        self.title_app.grid(row=0, column=0,
                            sticky="NSEW")


if __name__ == "__main__":
    app = App()
    app.mainloop()

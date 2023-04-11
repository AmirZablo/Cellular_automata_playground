import tkinter as tk
import subprocess

class App:
    def __init__(self, master):
        self.master = master
        master.title("Cellular Automata Playground")

        self.label = tk.Label(master, text="Choose a cellular automaton:")
        self.label.pack()

        self.ca1_button = tk.Button(master, text="Conway's game of life", command=self.open_ca1)
        self.ca1_button.pack()

        self.ca2_button = tk.Button(master, text="Wireworld", command=self.open_ca2)
        self.ca2_button.pack()

        self.ca3_button = tk.Button(master, text="Langton's ant", command=self.open_ca3)
        self.ca3_button.pack()

        self.ca4_button = tk.Button(master, text="Brian's brain", command=self.open_ca4)
        self.ca4_button.pack()

    def open_ca1(self):
        subprocess.Popen(['python3', 'game_of_life.py'])

    def open_ca2(self):
        subprocess.Popen(['python3', 'wireworld.py'])

    def open_ca3(self):
        subprocess.Popen(['python3', 'ant.py'])

    def open_ca4(self):
        subprocess.Popen(['python3', 'brain.py'])

root = tk.Tk()
app = App(root)
root.mainloop()

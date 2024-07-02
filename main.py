import os
from azure_dl import cosmosdb, storage
import tkinter as tk
from config import *

if __name__ == "__main__":
	print(storage_account)

	root = tk.Tk()
	root.title('Data Linguist')
	root.geometry('600x400+50+50')
	root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='icon.png'))
	root.mainloop()



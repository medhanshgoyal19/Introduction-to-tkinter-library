import tkinter as tk
# Import tkinter library.
# tkinter is used to create GUI (Graphical User Interface) applications in Python.
# "tk" is a short name (alias) that we use to write tkinter more easily.

root=tk.Tk()
# tk.Tk() creates a new window or the main window of our application.
# "root" is the variable that stores this window.

root.title('Introduction to tkinter')
# title() is a method in the tkinter library that sets the title of the window.
# The text 'Introduction to tkinter' will be displayed in the title bar of the window.

root.geometry('500x500')
# geometry() is a method in the tkinter library that sets the size of the window.
# The dimensions are stored in a string format.
# '500x500' means the window will be 500 pixels wide and 500 pixels high.

root.mainloop()
# mainloop() is a method in the tkinter library that starts the event loop.
# It keeps the window open and running.
# It waits for the user to interact with the window, such as clicking, typing or closing it.
# Without mainloop(), the window would open and immediately close.
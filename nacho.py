from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
root = ttk.Window(themename="litera")
root.geometry("600x600")
root.title("fibo-nacho")
def fiboall():
   num = entry.get()
   counter = 1
   first = 0
   second = 1
   dsum = 0
   while(counter <= int(num)):
       if int(num) != counter:
           text1["text"] += str(dsum)+","
       else:
           text1["text"] += str(dsum)+" "
       counter = counter + 1
       first = second
       second = dsum
       dsum = first + second
   txt = text1["text"]
   txt = txt[19:]
   print(txt)
   a = str(txt).split(",")
   print(a)
   for i in range(0, len(a)):
    a[i] = int(a[i])
   print(a)
   b = sum(a)
   print(b)
   text2["text"]="Sum of all numbers: "+ str(b)
text1 = ttk.Label(root, text="Generated  Series: ")
text2 = ttk.Label(root)
btn = ttk.Button(root, command=fiboall, text="Show the fibonacci series", bootstyle="success")
entry = ttk.Entry()
newline = ttk.Label(root, text="\n")
entry.pack()
newline.pack()
btn.pack()
newline.pack()
text1.pack()
text2.pack()

root.mainloop()

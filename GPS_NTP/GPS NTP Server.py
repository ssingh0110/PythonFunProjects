# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:58:14 2018

@author: Shashank
"""
#import Tkinter as tk
import tkinter as tk
import ntplib
from time import ctime

counter = 0 
def counter_label(label):
  def count():
    global counter
    counter += 1
    c = ntplib.NTPClient()
    #resp = c.request('time.nplindia.org')
    resp = c.request('1.in.pool.ntp.org')
    x = ctime(resp.tx_time)
    label.config(text=str(x))
    label.after(1000, count)
  count()
 
root = tk.Tk()
root.title("GPS Time")
label = tk.Label(root, fg="blue")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()


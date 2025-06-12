import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
from tkinter import filedialog

# filename = input("enter path to lightfield image: ")
file = filedialog.askopenfile(title='select input image')
entered = False
"""
killeroo:
p_width = 15.397
N = 519
offset = 5
"""
while True:
    key = input("enter microlense width or q to quit: ")
    if key == "q":
        break
    else:
        entered = True
        p_width = float(key)
        N = int(input("enter line numbers (microlens number N): "))
        offset = int(input("enter initial pixel offset: "))

    lf_im = cv2.imread(file.name)

    for i in range(0,N):
        lf_im[:,int(p_width*i)+offset,:] = 255
        lf_im[int(p_width*i)+offset,:,:] = 255
    
    plt.imshow(lf_im)
    plt.show()

if entered:
    print("final parameters:")
    print(f"lens_p_width: {p_width}")
    print(f"N: {N}")
    print(f"offset: {offset}")
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
from tkinter import filedialog

file = filedialog.askopenfile(title='select input image')
lf_im = cv2.imread(file.name)
lens_p_width = float(input("lens_p_width: "))
N = int(input("N: "))
offset = int(input("offset: "))
save_dir = filedialog.askdirectory(title='select save directory')

light_field_d = int(round(lens_p_width))
print(f"light_field_d: {light_field_d}")

for i in range(light_field_d):
    for j in range(light_field_d):
        print(f"processing: {i}, {j}  ", end='\r')
        cur_im = np.zeros((N,N,3)).astype(np.uint8)
        for x in range(N):
            for y in range(N):
                original_lf = lf_im[offset+int(lens_p_width*x):offset+int(lens_p_width*(x+1)),offset+int(lens_p_width*y):offset+int(lens_p_width*(y+1)),:]
                upsampled_lf = cv2.resize(original_lf, (light_field_d, light_field_d))
                cur_im[x][y] = upsampled_lf[i][j]
        
        cv2.imwrite(os.path.join(save_dir, f"image_{i}_{j}.png"), cur_im)
                # cv2.imwrite(save_dir+f"lens_{x}_{y}.png", lf_im[offset+int(lens_p_width*x):offset+int(lens_p_width*(x+1))+1,offset+int(lens_p_width*y):offset+int(lens_p_width*(y+1))+1,:])

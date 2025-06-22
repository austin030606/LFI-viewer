import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
from tkinter import filedialog

lf_images_dir = filedialog.askdirectory(title='select processed lightfield images directory')
save_dir = filedialog.askdirectory(title='select save directory')
N = int(input("N: "))
light_field_d = int(input("light_field_d: "))

lf_imgs = [[None for _ in range(light_field_d)] for _ in range(light_field_d)]
for i in range(light_field_d):
    for j in range(light_field_d):
        lf_imgs[i][j] = cv2.imread(os.path.join(lf_images_dir, f"image_{i}_{j}.png")).astype(np.float32)

u_center = (light_field_d) / 2.0
v_center = (light_field_d) / 2.0
alpha_inv_min = float(input("alpha_inv min: "))
alpha_inv_max = float(input("alpha_inv max: "))
alpha_inv_num = int(input("alpha_inv num: "))
alpha_invs = np.linspace(alpha_inv_min, alpha_inv_max, alpha_inv_num)
# -0.5 0.8 80

cnt = 0
for alpha_inv in alpha_invs:
    refocused_image = np.zeros((N, N, 3), dtype=np.float32)
    image_count = 0
    for u in range(light_field_d):
        for v in range(light_field_d):
            if (u-(light_field_d+1)//2)**2 + (v-(light_field_d+1)//2)**2 > ((light_field_d+1)//2)**2:
                continue
            print(f"processing refocused image {cnt}: ({u}, {v})  ", end='\r')
            current_image = lf_imgs[u][v]
            # shift
            shift_x = alpha_inv * (u - u_center)
            shift_y = alpha_inv * (v - v_center)
            M = np.float32([[1, 0, shift_y],
                            [0, 1, shift_x]])

            shifted_image = cv2.warpAffine(current_image, M, (N, N),
                                            flags=cv2.INTER_LINEAR,
                                            borderMode=cv2.BORDER_CONSTANT,
                                            borderValue=0)

            # and sum
            refocused_image += shifted_image.astype(np.float32)
            image_count += 1

    refocused_image /= image_count

    refocused_image_uint8 = np.clip(refocused_image, 0, 255).astype(np.uint8)
    cv2.imwrite(os.path.join(save_dir,f"{cnt}_refocused_{alpha_inv}.png"), refocused_image_uint8)
    cnt += 1
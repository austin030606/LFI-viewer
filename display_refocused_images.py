import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import re

class ImageSliderApp:
    def __init__(self, root, image_dir):
        self.root = root
        self.root.title('Image Slider Viewer')
        files = [f for f in os.listdir(image_dir) if f.lower().endswith('png')]
        
        def extract_number(filename):
            return int(filename.split("_")[0])
        
        files.sort(key=extract_number)
        self.image_paths = [os.path.join(image_dir, f) for f in files]


        self.img_label = tk.Label(root)
        self.img_label.pack(padx=10, pady=10)

        self.slider = tk.Scale(root, from_=0, to=len(self.image_paths)-1,
                               orient=tk.HORIZONTAL, command=self.on_slide,
                               length=400)
        self.slider.pack(pady=10)

        self.photo_cache = None

        self.show_image(0)

    def show_image(self, index):
        path = self.image_paths[index]
        img = Image.open(path)

        self.photo_cache = ImageTk.PhotoImage(img)
        self.img_label.config(image=self.photo_cache)
        self.root.title(f'Image Slider Viewer - {os.path.basename(path)}')

    def on_slide(self, val):
        index = int(val)
        self.show_image(index)

if __name__ == '__main__':
    root = tk.Tk()
    directory = filedialog.askdirectory(title='Select Image Directory')
    if not directory:
        exit()
    root.deiconify()
    app = ImageSliderApp(root, directory)
    root.mainloop()

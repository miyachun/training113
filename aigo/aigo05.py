#pip install matplotlib
#pip install numpy
#pip install ipython
import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output


def show_img(img):
#     plt.figure(figsize=(15,15))
    plt.style.use('dark_background')
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.show()

def img_processing(img):
    # do something here
    
    titles = ["Origin Picture", "COLORMAP_AUTUMN", "COLORMAP_BONE","COLORMAP_JET",
              "COLORMAP_WINTER","COLORMAP_RAINBOW","COLORMAP_OCEAN", "COLORMAP_SUMMER",
              "COLORMAP_SPRING","COLORMAP_COOL", "COLORMAP_HSV","COLORMAP_PINK",
              "COLORMAP_HOT", "COLORMAP_PARULA","COLORMAP_MAGMA","COLORMAP_INFERNO",
              "COLORMAP_PLASMA","COLORMAP_VIRIDIS","COLORMAP_CIVIDIS", "COLORMAP_TWILIGHT",
              "COLORMAP_TWILIGHT_SHIFTED","COLORMAP_TURBO","COLORMAP_DEEPGREEN",""]
    
    img_list = []
    
#     for idx in range(len(titles)-1):
#         colormap_mode = "cv2.{}".format(titles[idx])
#         print(colormap_mode)
#         print(idx)
#         img_list.append(cv2.applyColorMap(img, idx))

    img_list.append(img)
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_AUTUMN))
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_BONE))  
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_JET))
    
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_WINTER))    
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_RAINBOW))  
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_OCEAN))    
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_SUMMER))
    
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_SPRING)) 
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_COOL))    
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_HSV))  
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_PINK)) 
    
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_HOT))
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_PARULA)) 
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_MAGMA)) 
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_INFERNO)) 
    
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_PLASMA)) 
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_VIRIDIS)) 
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_CIVIDIS)) 
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_TWILIGHT)) 
    
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_TWILIGHT_SHIFTED)) 
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_TURBO)) 
    img_list.append(cv2.applyColorMap(img, cv2.COLORMAP_DEEPGREEN)) 
    img_list.append(np.zeros(img.shape, np.uint8))
    
    
    # ---------------- 印出結果圖表 ---------------- #

    plt.figure(figsize=(15,20)) 
    h = 6
    w = 4
    
    for i in range(h):        
        plt.subplot(h,w,i*w+1)
        plt.imshow(cv2.cvtColor(img_list[i*w], cv2.COLOR_BGR2RGB))
        plt.title(titles[i*w]) 
        
        plt.subplot(h,w,i*w+2)
        plt.imshow(cv2.cvtColor(img_list[i*w+1], cv2.COLOR_BGR2RGB))
        plt.title(titles[i*w+1]) 
        
        plt.subplot(h,w,i*w+3)
        plt.imshow(cv2.cvtColor(img_list[i*w+2], cv2.COLOR_BGR2RGB))
        plt.title(titles[i*w+2]) 
        
        plt.subplot(h,w,i*w+4)
        plt.imshow(cv2.cvtColor(img_list[i*w+3], cv2.COLOR_BGR2RGB))
        plt.title(titles[i*w+3])
    
    plt.show()

file_name = "002.jpg"
origin_img = cv2.imread(file_name)
print("origin picture:")
show_img(origin_img)

img_processing(origin_img)



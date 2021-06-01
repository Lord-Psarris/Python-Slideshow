# imports
import cv2
import glob
import os
import numpy as np

resolution = (500, 500)
_ = cv2.VideoWriter_fourcc(*'XVID')
rate = 40

# Creating a VideoWriter object
out = cv2.VideoWriter('slideshow.avi', _, rate, resolution)


# making the slideshow file
def slideshow():
    print('started')

    path = "images/"
    images_files = glob.glob(os.path.join(path, "*"))

    prev_image = np.zeros((500, 500, 3), np.uint8)
    for image in images_files:
        img = cv2.imread(image)

        height, width, _ = img.shape
        if width < height:
            height = int(height * 500 / width)
            width = 500
            img = cv2.resize(img, (width, height))
            shift = height - 500
            img = img[shift // 2:-shift // 2, :, :]
        else:
            width = int(width * 500 / height)
            height = 500
            shift = width - 500
            img = cv2.resize(img, (width, height))
            img = img[:, shift // 2:-shift // 2, :]

        for i in range(101):
            alpha = i / 100
            beta = 1.0 - alpha
            dst = cv2.addWeighted(img, alpha, prev_image, beta, 0.0)
            if i == 100:
                for j in range(100):
                    out.write(dst)

            out.write(dst)
            if cv2.waitKey(1) == ord('q'):
                return

        prev_image = img

        if cv2.waitKey(5000) == ord('q'):
            return
    out.release()
    print('finished')


slideshow()

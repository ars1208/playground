import cv2

def process_frame(img):
    print(img.shape)

if __name__ == "__main__":
    cop = cv2.VideoCapture("video/test001.mp4")

    while cop.isOpened():
        ret, frame = cop.read()
        if ret == True:
            process_frame(frame)
        else:
            break
import cv2

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

def process_frame(img):
    img = cv2.resize(img, (3840//2, 2160//2))
    cv2.imshow('image', img)
    cv2.waitKey()
    print(img.shape)

if __name__ == "__main__":
    cop = cv2.VideoCapture("video/test001.mp4")

    while cop.isOpened():
        ret, frame = cop.read()
        if ret == True:
            process_frame(frame)
        else:
            break
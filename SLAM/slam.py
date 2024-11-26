import cv2
import pygame

W = 3840 // 2
H = 2160 // 2

pygame.init()
screen = pygame.display.set_mode((W,H))
# surface = pygame.Surface((W,H)).convert()
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)

def process_frame(img):
    img = cv2.resize(img, (W, H))
    surf = pygame.surfarray.make_surface(img)
    
    screen.blit(surf, (0,0))
    pygame.display.flip()
    print(img.shape)

if __name__ == "__main__":
    cop = cv2.VideoCapture("video/test001.mp4")

    while cop.isOpened():
        ret, frame = cop.read()
        if ret == True:
            process_frame(frame)
        else:
            break
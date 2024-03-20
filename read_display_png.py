import cv2


def display_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)  # Use the variable image_path here
    if img is None:
        print("Error: Could not open or read the image.")
        return
    cv2.imshow('tuan', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


display_image('tuan.png')

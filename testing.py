import cv2,sys

original = cv2.imread(sys.argv[1])
duplicate = cv2.imread(sys.argv[2])  # 1) Check if 2 images are equals
if original.shape == duplicate.shape:
    print("The images have same size and channels")
    difference = cv2.subtract(original, duplicate)
    b, g, r = cv2.split(difference)

    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The images are completely Equal")
    else:
        print("The images are different")

else:
    print("the images are not equal")
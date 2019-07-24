import cv2

cap = cv2.VideoCapture(0)
alpha = .4


def lineAdder(image):
    # type: (image) -> image
    lineThickness = 1
    (l, w, c) = image.shape
    mid1 = w / 3
    mid2 = (2 * w) / 3
    cv2.line(image, (mid1, 0), (mid1, l), (255, 255, 255), lineThickness)
    cv2.line(image, (mid2, 0), (mid2, l), (255, 255, 255), lineThickness)
    return image


def recAdder(image, pos):
    # type: (image, rectangleposition) -> object
    (l, w, c) = image.shape
    mid1 = w / 3
    img = image.copy()
    x = mid1 * pos[0]  # increment x by mid1 for each zone to have a red rectangle
    cv2.rectangle(img, (x, 0), (x + mid1, l), (0, 0, 255), -1)
    if pos[1] != -1:
        x = mid1 * pos[1]
        cv2.rectangle(img, (x, 0), (x + mid1, l), (0, 0, 255), -1)
    if pos[2] != -1:
        x = mid1 * pos[2]
        cv2.rectangle(img, (x, 0), (x + mid1, l), (0, 0, 255), -1)
    return cv2.addWeighted(img, alpha, image, 1 - alpha, 0)


while True:
    ret, frame = cap.read()
    frame = lineAdder(frame)
    frame = recAdder(frame, (0, 1, 2))
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow("window", frame)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

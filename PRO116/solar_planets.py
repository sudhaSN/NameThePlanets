import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(
    img,
    "Sun",
    (20,300),
    cv2.FONT_HERSHEY_TRIPLEX,
    1,
    (255,255,255)
)

cv2.putText(
    img,
    "Mercury",
    (100,220),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "Venus",
    (185,220),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.6,
    (255,255,255)
)

cv2.putText(
    img,
    "Earth",
    (280,220),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.6,
    (255,255,255)
)

cv2.putText(
    img,
    "Mars",
    (390,220),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.6,
    (255,255,255)
)

cv2.putText(
    img,
    "Jupiter",
    (550,220),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.8,
    (255,255,255)
)

cv2.putText(
    img,
    "Saturn",
    (720,220),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.8,
    (255,255,255)
)

cv2.putText(
    img,
    "Uranus",
    (950,220),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.7,
    (255,255,255)
)

cv2.putText(
    img,
    "Neptune",
    (1090,220),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.5,
    (255,255,255)
)

cv2.imshow("Output window", img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg", img)
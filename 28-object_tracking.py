import cv2

# the tracker KCF is faster but less accurate
tracker = cv2.TrackerKCF_create()
# the tracker CSRT is slower but more accurate
# tracker = cv2.TrackerCSRT_create()

video = cv2.VideoCapture("./img/race.mp4")

ok, frame = video.read()

bbox = cv2.selectROI(frame)

# print(bbox)

ok = tracker.init(frame, bbox)

while True:
    ok, frame = video.read()
    print(ok)
    if not ok:
        break

    ok, bbox = tracker.update(frame)
    print(bbox)
    print(ok)

    if ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    else:
        cv2.putText(
            frame,
            "Tracking failure detected",
            (100, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 0, 255),
            2,
        )

    cv2.imshow("Tracking", frame)

    # Exit if ESC pressed
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
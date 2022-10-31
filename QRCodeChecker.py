import cv2 as cv
import json

# TODO: check if the file exist
with open("participantes_data.json", "r") as data_file:
    json_data = json.load(data_file)


cap = cv.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv.QRCodeDetector()

while True:
    _, img = cap.read()

    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    # check if there is a QRCode in the image
    if data:
        prtcp_data = data.split("-")
        prtcp_info = json_data.get(prtcp_data[0], [0])
        prtcp_info[0] += 1
        print(data)

    cv.imshow("QRCODEscanner", img)
    if cv.waitKey(1) == ord("q"):
        break

print(json_data["1004220138"])
cap.release()
cv.destroyAllWindows()

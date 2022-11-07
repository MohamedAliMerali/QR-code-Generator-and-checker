import json
import cv2 as cv
from datetime import datetime

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
        prtcp_info = json_data.get(prtcp_data[0], 0)
        if not prtcp_info:
            print('>> PARTICIPANT DO NOT EXIST !!')
            continue
        # prtcp_info[0] += 1
        if len(prtcp_info[4]) == 0:
            prtcp_info[4].append(str(datetime.now()))
        elif int(prtcp_info[4][-1].split(" ")[0].split("-")[2]) == datetime.now().day:
               print(">> PARTICIPANT ALREADY CHECKED IN !!")
        else:
            prtcp_info[4].append(str(datetime.now()))
        print(data)

    cv.imshow("QRCODEscanner", img)
    if cv.waitKey(1) == ord("q"):
        break

with open("participantes_data.json", "w") as data_file:
    data_file.write(json.dumps(json_data, indent=4))

print(json_data["1004220138"])
cap.release()
cv.destroyAllWindows()

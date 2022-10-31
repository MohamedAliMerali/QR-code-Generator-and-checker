# def tstamp_to_id(tstamp):
#     date, time = tstamp.split(" ")
#     date = date.split("-")
#     time = time.split(":")
#     date.pop(0)
#     date.extend(time)
#     return "".join(date)


# print(tstamp_to_id("10/2/2022 21:01:53"))


# import cv2 as cv

# cap = cv.VideoCapture(0)
# # initialize the cv2 QRCode detector
# detector = cv.QRCodeDetector()

# while True:
#     _, img = cap.read()

#     # detect and decode
#     data, bbox, _ = detector.detectAndDecode(img)
#     # check if there is a QRCode in the image
#     if data:
#         pass

#     cv.imshow("QRCODEscanner", img)
#     if cv.waitKey(1) == ord("q"):
#         break


# cap.release()
# cv.destroyAllWindows()


# import winsound
# winsound.Beep(440, 500)
# winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

# import simpleaudio 

# wave_obj = simpleaudio.WaveObject.from_wave_file("bell.wav")
# play_obj = wave_obj.play()
# play_obj.wait_done()
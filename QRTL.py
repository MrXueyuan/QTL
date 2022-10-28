# This is a Python sample script for QR code detection.
import cv2
import numpy


# Identify the QR code
def readQRCode():
    # load image
    src_image = cv2.imread("./Test.png")
    # instantiate
    qrcode = cv2.QRCodeDetector()
    # QR code detection and decoding
    info, points, straight_qrcode = qrcode.detectAndDecode(src_image)
    # Redraw the detection result of the QR code
    out_image = cv2.drawContours(src_image, [numpy.int32(points)], 0, (0, 0, 255), 2)
    # print the decoded result
    print("qrcode :", info)
    cv2.imshow("result", src_image)
    cv2.imwrite("./QR.jpg", out_image)
    cv2.waitKey(0)
    return info


# Visit https://www.jetbrains.com/help/pycharm/ for PyCharm help

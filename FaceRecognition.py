import time

import cv2
# 人脸识别函数
def Face():
    # 初始化超时定时器
    timeout = time.time()
    timeout += 8
    # 初始化识别器
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # 加载训练好的模型文件
    recognizer.read('./Model/bricsskill-gd.yml')
    # 获取分类器
    faceCascade = cv2.CascadeClassifier(r'./cv2data/haarcascade_frontalface_default.xml')
    # 设置图片显示的字体
    font = cv2.FONT_HERSHEY_SIMPLEX
    idnum = 0  #用户ID
    # 用户需要在此添加自己的姓名(拼音)，下标序号要与名字对应(ID从0开始，依次递增)
    names = ['lsh','dhj']
    # 捕获图像
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # 设置格式
    minW = 0.1*camera.get(3)
    minH = 0.1*camera.get(4)
    print('请正对着摄像头...')
    confidence = 100.00  # 设置置信度初始值
    score = 0  # 设置匹配指数初始值
    err = 1    # 设置报错值
    name = "unknown"
    while timeout >= time.time():
        # 读取图片
        success,img = camera.read()
        # 图片灰度化
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 检测人脸
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(int(minW), int(minH))
        )
        for (x, y, w, h) in faces:
            # 画一个矩形
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            #  图像预测predict函数，返回值一个是id，一个是置信度confidence，置信度值越小越好
            idnum, confidence = recognizer.predict(gray[y:y+h, x:x+w])
            # 设置匹配指数
            score =int( "{0}".format(round(220 - confidence)))
            # 匹配指数大于等于95即可验证通过人脸  
            if score > 95:
                name = names[idnum]
                err = 0
            else:
                name = "unknown"
                err = 1
            cv2.putText(img, str(name), (x+5, y-5), font, 1, (230, 250, 100), 1)
            cv2.putText(img, str(score), (x+5, y+h-5), font, 1, (255, 0, 0), 1)
        cv2.imshow('camera', img)
        # 保持画面持续
        key = cv2.waitKey(10)
        # 按Esc键退出
        if key==27 or score > 95:
            cv2.imwrite('./setFace.jpg', img)
            break
    # 关闭摄像头
    camera.release()
    cv2.destroyAllWindows()
    return err,name,idnum,score
#
# if __name__ == '__main__':
#     err, name, idNumber, score = Face()
#     print("您的名字是:", name,"\tID:",idNumber)
#     print("匹配指数:", score)





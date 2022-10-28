import numpy as np

err = 0  # A0 B1 C2 D3
AData = [5, 3, 4, 4, 3, 5]  # 0AB 1AC 2AD 3BC 4BD 5CD
CData = [3,2,1,0]
if __name__ == '__main__':

    if err == 0:  # A BCD
        BData = [0, AData[0], AData[1], AData[2]]
    if err == 1:  # B ACD
        BData = [AData[0], 0, AData[3], AData[4]]
    if err == 2:  # C ABD
        BData = [AData[1], AData[3], 0, AData[5]]
    if err == 3:  # D ABC
        BData = [AData[2], AData[4], AData[5], 0]
    a = np.array(BData)
    b = np.argsort(a)
    print('C', BData)
    print('C', CData[b[0]], CData[b[1]], CData[b[2]], CData[b[3]])

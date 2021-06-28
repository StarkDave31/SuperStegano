import pandas as pd
import numpy as np
import cv2

WS = pd.read_excel('data2.xlsx')
WS_np = np.array(WS)


ret, thresh1 = cv2.threshold(WS_np, 1, 255, cv2.THRESH_BINARY)


cv2.imshow('Binary Threshold', thresh1)


df = pd.DataFrame (thresh1)


filepath = 'data3.xlsx'

df.to_excel(filepath, index=False)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
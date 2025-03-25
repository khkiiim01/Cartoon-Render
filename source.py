import cv2 as cv
import numpy as np

def cartoonify_image(image_path, output_path="cartoon_image.jpg"):
    # 이미지 읽기
    img = cv.imread(image_path)
    img = cv.resize(img, (600, 600))  # 크기 조정

    # **1. 색상을 부드럽게 하기 위해 양방향 필터 적용**
    smooth = cv.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

    # **2. 엣지 감지를 위한 그레이스케일 변환**
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)  # 노이즈 제거

    # **3. 적응형 임계처리(Adaptive Thresholding)로 엣지 검출**
    edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, 
                                  cv.THRESH_BINARY, blockSize=9, C=2)

    # **4. 컬러 이미지와 엣지를 결합하여 카툰 효과 적용**
    cartoon = cv.bitwise_and(smooth, smooth, mask=edges)

    # 결과 저장
    cv.imwrite(output_path, cartoon)

    # 원본 및 결과 이미지 출력
    cv.imshow("Original", img)
    cv.imshow("Cartoon", cartoon)
    cv.waitKey(0)
    cv.destroyAllWindows()

# 실행 예제
cartoonify_image("sample.jpg")

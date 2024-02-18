import pyautogui as pag
import time
import os

print("책 제목을 입력하세요 : ", end='')
bookName = input()
folderLocation = 'YOUR_FOLDER_NAME' +  '/' + bookName
os.mkdir(folderLocation)

print("페이지 수를 입력하세요 : ", end='')
pageCount = int(input())

print("캡처할 범위의 왼쪽 상단으로 마우스를 이동해주세요, 5초 후 위치가 입력됩니다.")
for i in range(5):
    print(i + 1)
    time.sleep(1)
leftTop = pag.position()

print("캡처할 범위의 오른쪽 하단으로 마우스를 이동해주세요, 5초 후 위치가 입력됩니다.")
for i in range(5):
    print(i + 1)
    time.sleep(1)
rightBottom = pag.position()

width = rightBottom[0] - leftTop[0]
height = rightBottom[1] - leftTop[1]

for i in range(pageCount):
    pag.screenshot(f"{folderLocation}/{i+1}.png",
                   region=(leftTop[0] * 2, leftTop[1] * 2, width * 2, height * 2))
    # mac은 고해상도를 위해 한 픽셀에 4개를 집어넣음, 그래서 2배 곱해줘야 함 (window 운영체제는 * 2 를 제거할 것)
    pag.press('right')
    print(f"page : {i+1}")
    time.sleep(0.1)

print("스캔 완료")


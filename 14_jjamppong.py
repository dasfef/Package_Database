from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *
import random
import pymysql
from tkinter import *

## 함수 선언부
## 공통 함수
def connectMySQL():
    global conn, curr, window, canvas
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='KingHotDB', charset='utf8')
    curr = conn.cursor()
def closeMySQL():
    global conn, curr, window, canvas
    curr.close()
    conn.close()
    curr, conn = None, None
def randomColor():
    COLORS = ["black", "yellow", "white", "red", "green", "blue", "magenta", "orange", "brown", "maroon", "coral"]
    return random.choice(COLORS)
def clearMap():
    global conn, curr, window, canvas
    canvas.destroy()
    canvas = Canvas(window, height=SCR_HEIGHT, width=SCR_WIDTH)
    canvas.pack()

## 체인점 보기
def displayRestaurant():
    connectMySQL()
    sql = "SELECT restName, ST_AsText((ST_Buffer(restLocation, 3))) FROM restaurant"
    curr.execute(sql)

    while True:
        row = curr.fetchone()
        if not row:
            break
        restName, gisStr = row

        start = gisStr.index('(')
        start = gisStr.index('(', start + 1)
        start += 1
        end = gisStr.index(')')
        gisStr = gisStr[start:end]
        gisList = gisStr.split(',')
        newGisList = []
        for xyStr in gisList:
            x, y = xyStr.split(' ')
            x, y = float(x), float(y)
            xyList = [(x+90)*2, SCR_HEIGHT-(y+90)*2]
            newGisList.append(xyList)

        myColor = randomColor()
        canvas.create_line(newGisList, fill=myColor, width=3)
        tx, ty = xyList[0], xyList[1] + 15
        canvas.create_text([tx, ty], fill=myColor, text=restName.split(' ')[2])

    closeMySQL()

#관리자 보기
def displayManager():
    global conn, curr, window, canvas
    connectMySQL()

    sql = "SELECT ManagerName, ST_AsText(Area) FROM Manager ORDER BY ManagerName"
    curr.execute(sql)

    while True:
        row = curr.fetchone()
        if not row:
            break

        managerName, gisStr = row
        start = gisStr.index('(')
        start = gisStr.index('(', start + 1)
        start += 1
        end = gisStr.index(')')
        gisStr = gisStr[start:end]
        gisList = gisStr.split(',')
        newGisList = []

        for xyStr in gisList:
            x, y = xyStr.split(' ')
            x, y = float(x), float(y)
            xyList = [(x + 90) * 2, SCR_HEIGHT - (y + 90) * 2]
            newGisList.append(xyList)

        canvas.create_polygon(newGisList, fill=randomColor())
    closeMySQL()

#도로 보기
def displayRoad():
    global conn, curr, window, canvas
    connectMySQL()

    sql = "SELECT RoadName, ST_AsText(ST_Buffer(RoadLine, 2)) FROM Road"
    curr.execute(sql)

    while True:
        row = curr.fetchone()
        if not row:
            break

        managerName, gisStr = row
        start = gisStr.index('(')
        start = gisStr.index('(', start + 1)
        start += 1
        end = gisStr.index(')')
        gisStr = gisStr[start:end]
        gisList = gisStr.split(',')
        newGisList = []

        for xyStr in gisList:
            x, y = xyStr.split(' ')
            x, y = float(x), float(y)
            xyList = [(x + 90) * 2, SCR_HEIGHT - (y + 90) * 2]
            newGisList.append(xyList)

        canvas.create_polygon(newGisList, fill=randomColor())
    closeMySQL()

#관리자별 담당 체인점
def showResMan():
    global conn, curr, window, canvas

    displayRestaurant()

    connectMySQL()
    sql = "SELECT M.ManagerName, R.restName, ST_AsText((ST_Buffer(R.restLocation, 3))) FROM Restaurant R, Manager M"
    sql += " WHERE ST_Contains(M.area, R.restLocation) = 1 ORDER BY R.restName"

    curr.execute(sql)

    saveRest = ''

    while True:
        row = curr.fetchone()
        if not row:
            break

        managerName, restName, gisStr = row
        start = gisStr.index('(')
        start = gisStr.index('(', start + 1)
        start += 1
        end = gisStr.index(')')
        gisStr = gisStr[start:end]
        gisList = gisStr.split(',')
        newGisList = []

        for xyStr in gisList:
            x, y = xyStr.split(' ')
            x, y = float(x), float(y)
            xyList = [(x + 90) * 2, SCR_HEIGHT - (y + 90) * 2]
            newGisList.append(xyList)

        myColor = randomColor()

        if saveRest == restName:
            canvas.create_polygon(newGisList, fill=myColor)

        # 해당 위치에 글자쓰기
        # 관리자가 2명인 경우에는 추가 관리자 이름에 뒤에 붙여서 쓰기
        if saveRest == restName:
            tx, ty = xyList[0], xyList[1]+45    # 두 번째 관리자 아래에 쓰기
        else:
            tx, ty = xyList[0], xyList[1]+30    # 첫 번째 관리자 아래에 쓰기

        canvas.create_text([tx, ty], fill=myColor, text=managerName)
        saveRest = restName

        # myColor = randomColor()
        # canvas.create_line(newGisList, fill=myColor, width=3)
        # tx, ty = xyList[0], xyList[1]+15
        # canvas.create_text([tx, ty], fill=myColor, text=restName.split(' ')[2])

    closeMySQL()
def showNearrest():
    global conn, curr, window, canvas

    baseRest = '왕매워 짬뽕 ' + askstring('기준 체인점', '체인점 번호를 입력하세요') + '호점'
    print(baseRest)
    connectMySQL()
    sql = "SELECT ST_AsText(R2.restLocation), ST_DIstance(R1.restLocation, R2.restLocation)"
    sql += " FROM Restaurant R1, Restaurant R2"
    sql += " WHERE R1.restName = '"+baseRest+"'"
    sql += " ORDER BY ST_Distance(R1.restLocation, R2.restLocation)"
    curr.execute(sql)

    row = curr.fetchone()
    gisStr, distance = row
    start = gisStr.index('(')
    start += 1
    end = gisStr.index(')')
    gisStr = gisStr[start:end]
    x, y = list(map(float, gisStr.split(' ')))
    baseXY = [ (x+90)*2, SCR_HEIGHT-(y+90)*2 ]

    lineWidth = 20

    while True:
        row = curr.fetchone()
        if not row:
            break

        gisStr, distance = row
        start = gisStr.index('(')
        start += 1
        end = gisStr.index(')')
        gisStr = gisStr[start:end]
        x, y = list(map(float, gisStr.split(' ')))
        targetXY = [ (x+90)*2, SCR_HEIGHT-(y+90)*2 ]

        myColor = randomColor()

        if lineWidth < 0:
            lineWidth = 0

        canvas.create_line([baseXY, targetXY], fill=myColor, width=lineWidth)
        lineWidth -= 5

    closeMySQL()

    displayRestaurant()

## 전역 변수부
conn, curr = None, None
window, canvas = None, None

SCR_WIDTH, SCR_HEIGHT = 360, 360

## 메인 코드부
window = Tk()
window.title("왕매워 짬뽕 ver 0.1")
canvas = Canvas(window, height=SCR_HEIGHT, width=SCR_WIDTH)
canvas.pack()

mainMenu = Menu(window)
window.config(menu=mainMenu)

gis1Menu = Menu(mainMenu)
mainMenu.add_cascade(label="GIS 데이터 보기", menu=gis1Menu)
gis1Menu.add_command(label="체인점 보기", command=displayRestaurant)
gis1Menu.add_command(label="관리자 보기", command=displayManager)
gis1Menu.add_command(label="도로 보기", command=displayRoad)
gis1Menu.add_separator()
# gis1Menu.add_command(label="화면 지우기", command=commonFunc.clearMap(canvas, window, SCR_HEIGHT, SCR_WIDTH))
gis1Menu.add_command(label="화면 지우기", command=clearMap)
gis1Menu.add_separator()

gis2Menu = Menu(mainMenu)
mainMenu.add_cascade(label="GIS 데이터 분석", menu=gis2Menu)
gis2Menu.add_command(label="관리자별 담당 체인점", command=showResMan)
gis2Menu.add_command(label="가장 가까운 체인점", command=showNearrest)

window.mainloop()



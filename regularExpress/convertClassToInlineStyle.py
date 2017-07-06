import re
import sys
import os


def getStringBetweenAnd(s, data, flag=True):
    '''get string betweenAnd such as: label <style type="text/css"> and </style>
    '''
    if flag:
        pattern = re.compile(s, re.S)
    else:
        pattern = re.compile(s)
    # type(res) == list
    res = pattern.findall(data)
    if len(res) == 1:
        return res[0]
    else:
        return res


def replaceAwithB(sA, sB, data):
    '''replace A with B in data'''
    data = re.sub(re.compile(sA), sB, data)
    return data


def removeRNTEmptySpace(temp):
    '''remove \r\n\t, \r\n and empty space'''
    sA = '\r\n\t'
    sB = ""
    temp = replaceAwithB(sA, sB, temp)

    sA = '\r\n'
    sB = ""
    temp = replaceAwithB(sA, sB, temp)

    sA = '\/\*(.*?)\*\/'
    sB = ""
    temp = replaceAwithB(sA, sB, temp)

    sA = '\n'
    sB = ""
    temp = replaceAwithB(sA, sB, temp)

    temp = temp.split(';')
    temp2 = []
    for x in temp:
        x = x.strip()
        if x:
            temp2.append(x)
    return ';'.join(temp2) + ';'


def convertStyleToInline(classStyle, inLineStyle, data):
    '''convert class style to inline style'''
    data = replaceAwithB(classStyle, inLineStyle, data)
    return data


def findStyleAndReplace(styleName, allStyle, classStyle, dataOrig):
    '''find style name from all style and if it exists,
    try to replace class with inline'''
    temp = getStringBetweenAnd(styleName, allStyle)
    if temp:
        temp = removeRNTEmptySpace(temp)
        inLineStyle = 'style=' + '"' + temp + '"'
        dataOrig = convertStyleToInline(classStyle, inLineStyle, dataOrig)
    return dataOrig


def getAllFilePath(fileDir, allFilePathList, fileSelf):
    if os.path.isfile(fileDir):
        allFilePathList.append(fileDir)
        return
    for fileName in os.listdir(fileDir):
        if fileName == fileSelf:
            continue
        filePath = os.path.join(fileDir, fileName)
        if os.path.isdir(filePath):
            getAllFilePath(filePath, allFilePathList, fileSelf)
        else:
            allFilePathList.append(filePath)

if __name__ == '__main__':
    allFilePathList = []
    getAllFilePath(sys.argv[1], allFilePathList, sys.argv[0])
    for filepath in allFilePathList:
        try:
            with open(filepath, "rb") as fp:
                dataOrig = fp.read()
            styleDict = {}
            '''get string between label <style type="text/css"> and </style>'''
            s = r'<style type="text\/css">(.*?)<\/style>'
            allStyle = getStringBetweenAnd(s, dataOrig)
            if not allStyle:
                print('warn file:%r, all style is not exist!' % filepath)
                continue

            # get data from special label
            styleName = r'container \{(.*?)\}'
            classStyle = 'class="container"'
            dataOrig = findStyleAndReplace(styleName, allStyle, classStyle,
                                           dataOrig)

            styleName = r'\.content \{(.*?)\}'
            classStyle = 'class="content"'
            dataOrig = findStyleAndReplace(styleName, allStyle, classStyle,
                                           dataOrig)

            styleName = r'\.company \{(.*?)\}'
            classStyle = 'class="company"'
            dataOrig = findStyleAndReplace(styleName, allStyle, classStyle,
                                           dataOrig)

            styleName = r'\#contentBg \{(.*?)\}'
            classStyle = 'id="contentBg"'
            dataOrig = findStyleAndReplace(styleName, allStyle, classStyle,
                                           dataOrig)

            styleName = r'\.notif \{(.*?)\}'
            classStyle = 'class="notif"'
            dataOrig = findStyleAndReplace(styleName, allStyle, classStyle,
                                           dataOrig)

            styleName = r'\.title \{(.*?)\}'
            classStyle = 'class="title"'
            dataOrig = findStyleAndReplace(styleName, allStyle, classStyle,
                                           dataOrig)

            styleName = r'\.septop \{(.*?)\}'
            classStyle = 'class="septop"'
            dataOrig = findStyleAndReplace(styleName, allStyle, classStyle,
                                           dataOrig)

            styleName = r'\.actionemphasis \{(.*?)\}'
            classStyle = 'class="actionemphasis"'
            dataOrig = findStyleAndReplace(styleName, allStyle, classStyle,
                                           dataOrig)

            styleName = r'\.details div\{(.*?)\}'
            classStyle = 'class="details"'
            dataOrig = findStyleAndReplace(styleName, allStyle, classStyle,
                                           dataOrig)

            styleName = r'\.sepbot \{(.*?)\}'
            classStyle = 'class="sepbot"'
            dataOrig = findStyleAndReplace(styleName, allStyle, classStyle,
                                           dataOrig)

            styleName = r'\.footer \{(.*?)\}'
            classStyle = 'class="footer"'
            dataOrig = findStyleAndReplace(styleName, allStyle, classStyle,
                                           dataOrig)

            styleName = r'\.highlight \{(.*?)\}'
            classStyle = 'class="highlight"'
            dataOrig = findStyleAndReplace(styleName, allStyle, classStyle,
                                           dataOrig)

            styleName = r'\.sub_title \{(.*?)\}'
            classStyle = 'class="sub_title"'
            dataOrig = findStyleAndReplace(styleName, allStyle, classStyle,
                                           dataOrig)
            # print dataOrig
            with open(filepath + '.rep', "wb") as fp:
                fp.write(dataOrig)
        except:
            print "Error! exception filepath:%r" % filepath

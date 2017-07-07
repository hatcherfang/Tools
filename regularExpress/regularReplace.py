import sys
import re
import os


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


def batchReplace(rA, rB, filePathList, repFilePathList):
    "replace all the string rA with rB in all the files from filePathList and \
    write all the replaced content into file with postfix .rep"
    if not filePathList or type(filePathList) != list:
        return
    for filePath in filePathList:
        with open(filePath, "r") as fp:
            content = fp.read()
        link = re.compile(rA)
        output = re.sub(link, rB, content)
        if content !=output:
	    repFilePathList.append(filePath+".rep")
            with open(filePath+".rep", "wb") as fp:
            	fp.write(output)

if __name__ == '__main__':
    allFilePathList = []
    repFilePathList = []
    getAllFilePath(sys.argv[1], allFilePathList, sys.argv[0])
    rA = "AAA"
    rB = "BBB"
    batchReplace(rA, rB, allFilePathList, repFilePathList)
    print len(allFilePathList)
    print repFilePathList, len(repFilePathList)


import sys
import os


def getAllFilePath(fileDir, allFilePathList, fileSelf):
    for fileName in os.listdir(fileDir):
        if fileName == fileSelf:
            continue
        filePath = os.path.join(fileDir, fileName)
        if os.path.isdir(filePath):
            getAllFilePath(filePath, allFilePathList, fileSelf)
        else:
            allFilePathList.append(filePath)


def batchReName(filePathList, repFileList):
    if not filePathList or type(filePathList) != list:
        return
    for filePath in filePathList:
        if not filePath.endswith(".rep"):
            continue
        reFilePath = filePath[:-4]
        os.rename(filePath, reFilePath)
        repFileList.append(reFilePath)
if __name__ == '__main__':
    allFilePathList = []
    repFilePathList = []
    getAllFilePath(sys.argv[1], allFilePathList, sys.argv[0])
    batchReName(allFilePathList, repFilePathList)
    print len(allFilePathList)
    print repFilePathList, len(repFilePathList)

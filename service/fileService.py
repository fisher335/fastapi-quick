import os
import time

import config.config


async def get_filelist():
    filePath = os.getcwd()+"/static/file"
    # print(filePath)
    fileList = []
    for home, dirs, files in os.walk(filePath):
        for filename in files:
            result = {}
            fullname = os.path.join(home, filename)
            fileinfo = os.stat(fullname)
            result['name'] = filename
            result['size'] = hum_convert(fileinfo.st_size)
            result['date'] = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(fileinfo.st_ctime))
            result['url'] = fullname
            fileList.append(result)
    # print(fileList)
    return fileList


def hum_convert(value):
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    size = 1024.0
    for i in range(len(units)):
        if (value / size) < 1:
            return "%.2f%s" % (value, units[i])
        value = value / size


if __name__ == "__main__":
    # .为遍历当前目录  其他的给绝对路径
    get_filelist()

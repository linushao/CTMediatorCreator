import os

# 打开文件夹
def mkDir(path):
    path = path.strip()
    # dir_path = self.path + path
    dir_path = path
    exists = os.path.exists(dir_path)
    if not exists:
        os.makedirs(dir_path)
        return dir_path
    else:
        return dir_path


# 获取当前时间戳（秒）
def ts():
    import time
    ticks = time.time()
    return int(ticks)

# 时间戳格式化日期
def dateFormer(timeStamp, formerStr):
    import time
    # timeStamp = 1381419600
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime(formerStr, timeArray)
    # otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    # otherStyletime == "2013-10-10 23:40:00"
    return otherStyleTime



# 创建文件
def savefile(content, dir_path):
    f = open(dir_path, "wb+")
    f.write(content.encode('utf-8'))
    f.close()

def readfile(dir_path):
    f = open(dir_path, "r")
    content = f.read()
    f.close()
    return content
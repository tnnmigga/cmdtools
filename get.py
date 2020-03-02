import urllib.request
import sys
import os


def Schedule(readCnt, blockSize, fileSize):
    percent = 100.0 * readCnt * blockSize / fileSize
    if percent > 100:
        percent = 100
    sys.stdout.write('\rDownloading %.1f%%' % (percent))
    sys.stdout.flush()


if __name__ == "__main__":
    url = ''.join(sys.argv[1:])
    #local = url.split('/')[-1]
    filename = url.split('/')[-1:][0]
    local = os.path.join('', filename)
    print('Begin download %s' % (filename))
    try:
        urllib.request.urlretrieve(url, local, Schedule)
    except Exception as error:
        print(str(error))
    else:
        print("\nFinish")

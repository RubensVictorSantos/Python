# coding: utf-8

import io
import sys
#import urllib.request
import urllib.request as request

BUFF_SIZE = 1024


def download_length(response, output, length):
    times = length // BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Downloaded %d" % (((time * BUFF_SIZE)/length)*100))

def download(response, output):
    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        output.write(data)
        print('Downloaded {bytes}'.format(bytes=total_downloaded))

def main():


    '''if len(sys.argv) != 2:
        print('usage: {} <url>'.format(sys.argv[0]))
        sys.exit()
    url = sys.argv[1]

    req = request.urlopen(url)
    print(req.read())'''

    
    response = request.urlopen(sys.argv[1])
    out_file = io.FileIO("saida.zip", mode="w")

    content_length = response.getheader('Content-Length')
    if content_length:
        length= int(content_length)
        download_length(respose, out_file, length)
    else:
        download(response, out_file)

    response.close()
    out_file.close()
    print("Fineshed")

if __name__ == "__main__":
    main()








    

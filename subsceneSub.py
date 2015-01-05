#-------------------------------------------------------------------------------
# Name:        Subscene Subtitle Downloader
# Purpose:
#
# Author:      Nagraj Gajengi
#
# Created:     1/3/2015
#-------------------------------------------------------------------------------

#change for loop to change the number of files to be downloaded
import urllib2                                                # needed for functions,classed for opening urls.
import json
import re
import zipfile
import os
import sys
import shutil
def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        zf.extractall(dest_dir)
        for info in zf.infolist():
            fname=info.filename
            return fname

def subDownloader(url,cname):
        usock = urllib2.urlopen(url)                                  #function for opening desired url
        file_name = cname+".zip"                                #Example : for given url "www.cs.berkeley.edu/~vazirani/algorithms/chap6.pdf" file_name will store "chap6.pdf"
        f = open(file_name, 'wb')                                     #opening file for write and that too in binary mode.
        file_size = int(usock.info().getheaders("Content-Length")[0]) #getting size in bytes of fi
        downloaded = 0
        block_size = 8192                                            #bytes to be downloaded in each loop till file pointer does not return eof
        while True:
                buff = usock.read(block_size)
                if not buff:                                             #file pointer reached the eof
                        break
                downloaded = downloaded + len(buff)
                f.write(buff)
        f.close()
        path=os.getcwd()
        name=unzip(file_name,path)
        os.rename(name,cname+".srt")
        os.remove(file_name)
        print cname+".srt"

def getSubtitleLink(page):
        start_link=page.find('/english')
        if start_link==-1:
                return False
        page=page[start_link-100:]
        start_link=page.find("<a href=")
        if start_link==-1:
                return False
        start_quote=page.find('"',start_link)
        end_quote=page.find('"',start_quote+1)
        url=page[start_quote+1:end_quote]
        return url
def get_page(url):
    hdr={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    req = urllib2.Request(url, headers=hdr)
    return urllib2.urlopen(req).read()
def get_download_link(url):
        page=get_page(url)
        start_link=page.find('<div class="download">')
        if start_link==-1:
                return False
        page=page[start_link-100:]
        start_link=page.find("<a href=")
        if start_link==-1:
                return False
        start_quote=page.find('"',start_link)
        end_quote=page.find('"',start_quote+1)
        url=page[start_quote+1:end_quote]
        return url
    
mainUrl="http://subscene.com"
path = sys.argv[1]
start_index=path.rindex("\\")
end_index=path.rindex(".")
filename=path[start_index+1:end_index]
url="http://subscene.com/subtitles/release?q="
fUrl=url+filename
extn=getSubtitleLink(get_page(fUrl))
url=mainUrl+extn
downlink=get_download_link(url)
fDownllink=mainUrl+downlink
subDownloader(fDownllink,filename)
a=raw_input("Done")

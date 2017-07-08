#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import youtube_dl
import os
import sys
import time
import shutil

reload(sys)
sys.setdefaultencoding('utf-8')

def getnow():
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
def  delfile(filename):
	if os.path.exists(filename):
	    os.remove(filename)

if len(sys.argv)!=3 :
        print ("invalid  args ;  downvideo.py {url} {savefolder}")
        exit()
#downurl="https://www.youtube.com/watch?v=i5IqVSOI3Ug"
#savepath="video-save"
downurl=sys.argv[1] 
savepath=sys.argv[2]

if os.path.exists(savepath):
	shutil.rmtree(savepath)
os.mkdir(savepath)

logfilename=savepath+"/"+'log.txt'
logfile=open(logfilename,'a')
logfile.write(getnow()+"\tbegin-download\t"+downurl+"\t"+savepath+"\n")

class MyLogger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        print(msg)

def my_hook(d):

#    print("\r\nfilename "+d['filename']+"\r\n")
#    print("tmpfilename "+d['tmpfilename'])
#    print("downloaded_bytes "+str(d['downloaded_bytes']))
#    print("total_bytes "+ str(d['total_bytes']))
#    print("total_bytes_estimate "+ str(d['total_bytes_estimate']))
#    print("elapsed "+ str(d['elapsed']))
#    print("eta "+ str(d['eta']))
#    print("speed "+ str(d['speed']+"\r\n"))

	
    if d['status'] == 'finished':
        print('download 100%')
	logfile.write(getnow()+"\tdownloaded\n")
	if str(d['filename']).endswith('.m4a') :
		logfile.write(getnow()+"\talldownloaded\tthen merging\n")
		logfile.close()
    else :
	print(d["status"]+" "+d["filename"])
	logfile.write(getnow()+"\t"+d['status']+"\t"+d['filename']+"\n")
	

ydl_opts = {
    # 'proxy': 'http://123.153.123.24:808',
    # 'proxy':'http://127.0.0.1:8123',
    # 'proxy':'socks5://127.0.0.1:1080',
    #%(title)s-%(id)s.%(ext)s
    'outtmpl' : savepath+"/"+'saved.%(ext)s' ,
    'writeinfojson': 'true`',
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio',
    'recode_video' :'mp4',
    'merge_output_format': 'mp4',
    'ignoreerrors': 'true',
    #'keepvideo': 'false',  
    # 'noplaylist': 'true', # default = true 
    # 'logger': MyLogger(),
    'progress_hooks': [my_hook],
    'postprocessors': [{
        'key': 'ExecAfterDownload',
        'exec_cmd': "echo \""+getnow()+"\tmerge-end\" >> xxx/log.txt || exit 0; ls "
    }]
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([downurl])
    # ydl.download(['https://www.youtube.com/watch?v=KaKq0UUTPU0&list=PLywfaJMr2okmMx9Ntlqq2YaEf7FQ8byq1'])







##依赖转码工具

ubuntu14.04 下安装ffmpeg
```bash
sudo apt-get install python-software-properties
sudo apt-add-repository ppa:mc3man/trusty-media
sudo apt-get update
sudo apt-get install ffmpeg gstreamer0.10-ffmpeg
```

ubuntu14.04 下安装avconv
```bash
sudo add-apt-repository ppa:heyarje/libav-11 && sudo apt-get update
sudo apt-get install libav-tools
```

##安装youtube-dl

```
pip install youtube-dl
```


##python脚本下载视频

主要作用是获取进行的状态, xxx/log.txt
是否正在下载,是否下载完成了(视频/音频) ,正在合并以及合并完成. 

执行 `python  111.py https://www.youtube.com/watch?v=lAaCeiqE6CE xxx`  即可下载指定的视频.
然后被存储在 xxx 文件夹下.

sys.argv[1]   才是第一个参数
sys.argv[0]  是文件本身的文件名,这里就是111.py





# Linux前台进程监视程序

> 本程序用于linux中gui界面活动前台程序的监视.

本程序基于`xdotool`进行开发. 使用`debian`的桌面小工具中的命令行周期性的调用本程序, 并将前台进程信息写入日志文档.



### xdotool工具说明

该工具可让您模拟键盘输入和鼠标活动，移动窗口并调整窗口大小等。它使用X11的XTEST扩展名和其他Xlib函数来完成此操作.

> 下面是xdotool的相关子命令. 这里只列举了相关的子命令.

|           子命令              |              说明                         |                   用法                |
|            :-:                |               :-:                         |                     :-:               |
| getactivewindow               |       获取当前活跃的前台进程的id          |  xdotool getactivewindow              |
| getwindowfocus                |       获取当前捕捉焦点的进程的id          | xdotool getwindowfocus                |
| getwindowname                 |       使用进程id获取进程窗口标题          |   xdotool getwindowname 67109223      |
| getwindowpid                  |       使用进程id获取OS中的pid             |  xdotool getwindowpid  67109223       |


### 监视程序流程
 
每一秒都启动一次. 使用`xdotool getactivewindow`获取到前台进程的id, 之后使用`getwindowpid`获取到系统pid. 最后使用`ps pid`获得前台进程属于哪一个进程.



### 强化想法
1. 记录窗口标题, 通过窗口标题进行更细粒度的分类.
    典型的如浏览器, 目前许多的活动都是通过浏览器完成的, 例如看直播, 看视频, 看文档等.
1. 增加忽略名单
    对于一些不希望存储的信息, 通过忽略名单进行忽略, 从标题和进程两个进行忽略.
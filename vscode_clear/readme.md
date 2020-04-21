用于清理vscode在运行过程中产生的一些无效工作区.

例如, 很久之前打开的一个工作区`~/project/some`在该工作区无用,并且在目录中删除的时候, `~/.config/Code/User/workspaceStorage/`目录中仍然会保留该工作区的信息. 

而vscode中`Ctrl+R`能够列出来的工作区信息在`~/.config/Code/storage.json`中.

在大多数时候, vscode的工作区配置并不需要清理, 因为占用空间并不大, 但是cpp-tools这个插件会在`~/.config/Code/User/workspaceStorage/XX`里面创建一个较大的文件, 在工作区无效的时候, 该文件就会浪费磁盘空间. 


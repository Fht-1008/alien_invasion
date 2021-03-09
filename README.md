# 《Python编程：从入门到实践》 项目一：外星人入侵

### 游戏规则

在游戏《外星人入侵》中，玩家控制着一艘最初出现在屏幕底部中央的飞船。玩家可以使用箭头键左右移动飞船，还可使用空格键进行射击。

游戏开始时，一群外星人出现在天空中，他们在屏幕中向下移动。玩家的任务是射杀这些外星人。玩家将所有外星人都消灭干净后，将出现一群新的外星人，他们移动的速度更快。只要有外星人撞到了玩家的飞船或到达了屏幕底部，玩家就损失一艘飞船。玩家损失三艘飞船后，游戏结束。

### 安装pygame（win10）

此项目完全通过`pygame`库编写而成，无需安装其他python库。

1. 在https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame中下载pygame相关的.whl安装包

   > 注意：若python版本为3.7，则下载cp37相关.whl，其他版本类似；64位操作系统需下载win_amd64版本的.whl；

2. 在终端中进入下载好的.whl文件所在目录，通过`$ python -m pip install pygame-1.9.6-cp37-cp37m-win_amd64.whl`安装pygame。

### 运行游戏
- `git clone https://github.com/Fht-1008/alien_invasion.git`
- `cd alien_invasion`
- `python alien_invasion.py`
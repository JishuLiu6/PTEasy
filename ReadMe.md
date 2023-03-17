# PTEasy

----

本项目主要为了解决，因为种子下载软件崩溃，导致记录丢失，无法保种的情况。

----

## 安装配置
* 暂时只支持恢复到`QBittorrent`保种，开发中...
* 本项目需使用 `python3`,暂不支持可视化页面，开发中...
* 下载项目后命令行运行以下代码,安装所需要的环境
    ```shell
    pip install -r requirements -i https://pypi.douban.com/simple
    ```
* `config.py`文件进行具体配置
    ```python
  qbtorrentcfg = {
    "host": "127.0.0.1:52005",  # QB主机地址:端口
    "username": "xxxxxx",  # 账户
    "password": "xxxx",  # 密码
    "torrent_path": 'E:\\PTDownload',  # 种子所在路径
    "search_path": 'E:\\',  # 资源所在路径
    "tag": "Free" # QT标签
    }
  ```
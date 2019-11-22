# 可视化进程（后端）

查看训练进度等



## 开始进程

``` python 
from trainer.backend import trainerApp

from trainer.core.config import PORT

if __name__ =="__main__":
    trainerApp.run(host='127.0.0.1', port=int(PORT))
```


## 查看日志

app 日志路径如下：

``` python 
if sysstr == "Windows":
    self.Trainer_APP_DIR = r"D:\.trainer\app"
    
else:
    self.Trainer_APP_DIR = r"~/.trainer\app"

# 日志目录 
self.Trainer_LOG_DIR = os.path.join(self.Trainer_APP_DIR,r"trainer-log") # 统一路径
```



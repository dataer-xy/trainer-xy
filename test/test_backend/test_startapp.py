
from trainer.backend import trainerApp

from trainer.core.config import PORT
from trainer.core.config import DEBUG

# OK
if __name__ =="__main__":
    trainerApp.run(host='127.0.0.1', port=int(PORT), debug=DEBUG) #  debug模式 网页上会有堆栈，第二个重要的调试模式下的功能，就是重载器，可以在源文件被修改时自动重启应用




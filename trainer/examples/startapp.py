"""运行 app """

from trainer.backend import trainerApp

from trainer.config.globalconfig import port
from trainer.config.globalconfig import DEBUG

# OK
if __name__ =="__main__":
    trainerApp.run(host='127.0.0.1', port=int(port), debug=DEBUG)




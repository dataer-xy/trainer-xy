""" app """

from trainer.backend import trainerApp

from trainer import trainerConfig

port = trainerConfig.port

# OK
if __name__ =="__main__":
    trainerApp.run(host='127.0.0.1', port=int(port))


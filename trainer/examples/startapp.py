""" app """

from trainer.backend import trainerApp

from trainer.core.config import PORT

# OK
if __name__ =="__main__":
    trainerApp.run(host='127.0.0.1', port=int(PORT))


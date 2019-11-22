
from trainer.core.msmg import MessageManager


# OK
def test_delete():
    msMg = MessageManager()

    msMg.clear_trainName("20191118145437")

    msMg.delete_queue("trainListStaticInfo")

def __main():
    test_delete()



if __name__ == "__main__":
    __main()


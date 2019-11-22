from trainer.core.msmg import MessageManager


def test():
    msMg = MessageManager()
    data = {
        "projectName":"testProj",
        "trainName":"20191118152056"
    }
    msMg.push(data,topic="trainListStaticInfo")

def main():
    test()

if __name__ == "__main__":
    main()

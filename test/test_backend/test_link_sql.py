from myutils.linksqlUtils import link_mysql_ifnotexit_creat

def test_link_sql1():
    
    print("begin")
    database = "20191118152056"
    conn = link_mysql_ifnotexit_creat(database)

    conn.close()

    print("end")

def __main():
    test_link_sql1()


if __name__ == "__main__":
    __main()
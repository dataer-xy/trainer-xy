# df保存到sql
def _my_dataframe_to_sql(df, savetablename, con, engine, if_exists="fail", index=False,**kargs):
    """df保存到sql
    
    有些情况下，con引擎不好用，要用engine引擎
    """
    try:
        try:
            df.to_sql(savetablename, con=con, if_exists=if_exists, index=index,**kargs)
            isSaveSuccessful = True
        except:
            df.to_sql(savetablename, con=engine, if_exists=if_exists, index=index,**kargs)
            isSaveSuccessful = True
        return isSaveSuccessful
    except Exception as e:
        raise e
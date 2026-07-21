import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:

    column_name=["student_id","age"]  #select

    df=pd.DataFrame(student_data, columns=column_name) #from and create new one

    return df  #printing the function output
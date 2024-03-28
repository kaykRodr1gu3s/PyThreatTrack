import pandas as pd
import os

class csv_creator:
    def verifing_directory(self, dir_name):
        """
        This function, acept the directory name as argument. It will return False if the directory is empty, if the directory isn't empty, will return True 
        
        """
        
        os.chdir(dir_name)
        dir_content = len(os.listdir()) > 0
        return dir_content


    def datas_to_csv(self, dir, datas) -> None:
        """
        This function , will create a dataframe or read a csv with pandas, and will concat both dataframe and create a csv or create a new csv.

        """

        if dir is False:
            df = pd.DataFrame(datas)

            df.to_csv("virustotal_result_ips.csv")
            print("the csv has been created")

        else:
            
  
            df = pd.read_csv("virustotal_result_ips.csv")

            datas_df = pd.DataFrame(datas)

            df1 = df._append(datas_df, ignore_index=True)
            df1.drop(df1.filter(regex="Unname"), axis=1, inplace=True)
            df1.to_csv("virustotal_result_ips.csv")\
            
            print("The datas has been concatenated")
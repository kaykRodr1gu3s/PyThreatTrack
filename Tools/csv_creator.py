import pandas as pd
import os


class csv_creator:
    def verifing_directory(self, dir_name):
        """
        This function, acept the directory name as argument. It will return False if the directory is empty, if the directory isn't empty, will return True 
        
        """
        
        os.chdir(dir_name)
        dir_content = len(os.listdir()) > 0
        print(dir_content)
        return dir_content


    def datas_to_csv(self, dir, datas) -> None:
        """
        This function , will create a dataframe with pandas, anf after will creat a csv file name ips.csv

        """

        if dir is False:
            print("tem algo")
            df = pd.DataFrame(datas)

            df.to_csv("ips.csv")

        else:
            print("aqui funfou")
            df = pd.read_csv("ips.csv")
            
            df1 = pd.DataFrame(datas)
            df1.drop(columns=df1.columns[df1.columns.str.contains('Unnamed', case=False)])
            data1 = df._append(df1, ignore_index=True)
            data1.to_csv("ips.csv")
            

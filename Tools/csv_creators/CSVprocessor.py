import pandas as pd
import os

class abuseip:
    def __init__(self, file_name):
        """
        The input is the file for the new csv or the csv that already exist
        """
        self.file_name = file_name

    def verifing_directory(self) -> bool:
        
        """
        This function, will change the current directory and list and verify the file in the directory!
        
        """
        os.chdir('ip_file')
        dir_content = os.listdir()
        
        for file in dir_content:
            if file == self.file_name:                
                return True
            
        return False
            
    def appending_datas(self, dir_verication: bool, datas: list):

        """
        This function, will read and append new datas to csv file, or will create a new file
        
        """ 

        if dir_verication == True:

            read_csv = pd.read_csv(self.file_name, index_col=0)
            df = pd.DataFrame(datas)
            df1 = read_csv._append(df, ignore_index=True)
            df1.to_csv(self.file_name)   

            print("New datas has been appended to the csv")

        else:       
            df = pd.DataFrame(datas)
            df.to_csv(self.file_name)
            print("A new csv file has been created")
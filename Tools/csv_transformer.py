import pandas as pd
import os
from datetime import datetime

class csv_creator:
    def datas_to_csv(self, datas : list) -> None:
        """
        This function , will create a dataframe with pandas, anf after will creat a csv file name ips.csv

        """
        os.chdir('ip_file')

        
        df = pd.DataFrame(datas)
        df.to_csv("ips.csv")

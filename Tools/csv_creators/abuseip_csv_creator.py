import pandas as pd
import Tools.ips as ips


class abuseip:
    def data(self, list_data):
        df = pd.DataFrame(list_data)
        df.to_csv("simple_example.csv")

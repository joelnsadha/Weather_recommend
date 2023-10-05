import pandas as pd
import numpy as np
data = "./uszip"


class ZipCodes:
    """
    Class defines zipcodes by state
    """
    def __init__(self):
        """
        Initializes zip code class.
        :param :
        """
        self.data = pd.read_csv("./files/uszips.csv")

    def get_zipcodes(self):
        """
        Returns sip-codes in a US state.
        :return:
        """

        zip_data = pd.DataFrame(self.data)
        z = np.array(zip_data.iloc[:, 0])
        return ["0{}".format(_) for _ in z]

    def all_data(self):
        df = pd.DataFrame(self.data)
        df['zip_code'] = df['zip_code'].apply(lambda x: "0" + str(x))
        return df

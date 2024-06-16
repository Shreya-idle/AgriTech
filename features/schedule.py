import pandas as pd 
class Schedule:
    def __init__(self , crop_name:str):
        self.crop_name = crop_name 
        self.__initialize_df()

    def __initialize_df(self):
        self.df = pd.read_csv("features/fertilizers.csv")
        self.crop = self.df["Crop"]

    def scheduler(self):
        self.crop_index = {value: key for key, value in enumerate(self.crop)}
        crop_index = self.crop_index[self.crop_name]
        return self.df.iloc[crop_index]

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

class EuropeStatistics:
    def __init__(self):
        file = "Project_File.xlsx"
        xls = pd.ExcelFile(file)

        self.dataFrame = xls.parse(0, usecols=[0, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                                   names=["MonthYear", "United Kingdom", "Germany", "France", "Italy", "Netherlands", "Greece", "Belgium & Luxembourg", "Switzerland", "Austria", "Scandinavia", "CIS & Eastern Europe"])

        self.splits = self.dataFrame['MonthYear'].str.split(' ', n=1, expand=True)
        #print(self.splits)
        self.dataFrame = self.dataFrame.assign(year=self.splits[0])

        self.dataFrame = self.dataFrame.replace(['na'], [0])
        #print(self.dataFrame["Greece"])

        # self.dataFrame = self.dataFrame.assign(year=self.splits)
        self.whatiwant = self.dataFrame[(self.dataFrame["year"].astype(int) >= 1978) & (self.dataFrame["year"].astype(int) <= 1987)]

    def TopThreeCountriesSum(self):
        self.filter7 = self.dataFrame[2: 121]["United Kingdom"].sum()
        self.filter8 = self.dataFrame[2: 121]["Germany"].sum()
        self.filter9 = self.dataFrame[2: 121]["France"].sum()
        self.filter10 = self.dataFrame[2: 121]["Italy"].sum()
        self.filter11 = self.dataFrame[2: 121]["Netherlands"].sum()
        self.filter12 = self.dataFrame[2: 121]["Greece"].sum()
        self.filter13 = self.dataFrame[2: 121]["Belgium & Luxembourg"].sum()
        self.filter14 = self.dataFrame[2: 121]["Switzerland"].sum()
        self.filter15 = self.dataFrame[2: 121]["Austria"].sum()
        self.filter16 = self.dataFrame[2: 121]["Scandinavia"].sum()
        self.filter17 = self.dataFrame[2: 121]["CIS & Eastern Europe"].sum()

        # print(self.filter7)
        # print(self.filter8)
        # print(self.filter9)
        # print(self.filter10)
        # print(self.filter11)
        # print(self.filter12)
        # print(self.filter13)
        # print(self.filter14)
        # print(self.filter15)
        # print(self.filter16)
        # print(self.filter17)

        print(f'The top 3 countries in Europe that visitors visit are United Kingdom {self.filter7}, Germany {self.filter8}, Netherlands {self.filter9}')


    def TopThreeCountriesMean(self):
        self.filter1 = self.dataFrame[2: 121]["United Kingdom"].mean()
        self.filter2 = self.dataFrame[2: 121]["Germany"].mean()
        self.filter3 = self.dataFrame[2: 121]["Netherlands"].mean()

        # print(self.filter1)
        # print(self.filter2)
        #print(self.filter3)

        print(f'The mean of United Kingdom is: {self.filter1}.')
        print(f'The mean of Germany is: {self.filter2}.')
        print(f'The mean of Netherlands is: {self.filter3}.')


    def TopThreeCountriesMedian(self):
        self.filter4 = self.dataFrame[2: 121]["United Kingdom"].median()
        self.filter5 = self.dataFrame[2: 121]["Germany"].median()
        self.filter6 = self.dataFrame[2: 121]["Netherlands"].median()

        # print(self.filter4)
        # print(self.filter5)
        #print(self.filter6)

        print(f'The median of United Kingdom is: {self.filter4}.')
        print(f'The median of Germany is: {self.filter5}.')
        print(f'The median of Netherlands is: {self.filter6}.')


    def TotalVisitorUnitedKingdom(self):
        self.filter7 = self.dataFrame[2: 121]["United Kingdom"].sum()
        print(self.filter7)
        return self.dataFrame[2: 121]["United Kingdom"].sum()


    def chart1(self):
        self.whatineed = self.whatiwant[
            (self.whatiwant["year"].astype(int) >= 1979)&
            (self.whatiwant["year"].astype(int) <= 1982)
        ]
        # print(self.whatineed)

        plt.scatter(self.whatineed['United Kingdom'], self.whatineed['year'], color=(0.5,0.1,0.5,0.6))
        plt.title("Number of Visitors in United Kingdom from 1979 - 1982", fontweight="bold", y=1.03)
        plt.xlabel("Number of Visitors", fontweight="bold")
        plt.ylabel("Year", fontweight="bold")
        plt.show();


    def chart2(self):
        self.ax = self.whatineed['Germany'].plot(kind='bar', title="Number of Visitors in Germany from 1979 - 1982", figsize=(10, 10), legend=True, fontsize=12, color=(0.5,0.1,0.5,0.6))
        plt.show()


europe = EuropeStatistics()
europe.TopThreeCountriesMean()
# europe.sumCountries()
europe.chart1()
europe.chart2()
# europe.medianOfTopThree()
#europe.meanOfTopThree()
europe.TopThreeCountriesMedian()
europe.TopThreeCountriesSum()
europe.TotalVisitorUnitedKingdom()

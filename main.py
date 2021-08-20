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


    def TopThreeCountriesMean(self):
        self.filter1 = self.dataFrame[26: 37]["United Kingdom"].mean()
        #print(self.filter1)

        self.filter2 = self.dataFrame[26: 37]["Germany"].mean()
        #print(self.filter2)

        self.filter3 = self.dataFrame[26: 37]["Netherlands"].mean()
        #print(self.filter3)

        print(f'Mean for the United Kingdom is: {self.filter1}.')
        print(f'Mean for the Germany is: {self.filter2}.')
        print(f'Mean for the Netherlands is: {self.filter3}.')

        # hello



    def TotalVisitorUnitedKingdom(self):
        self.filter7 = self.dataFrame[26: 37]["United Kingdom"].sum()
        print(self.filter7)
        return self.dataFrame[26: 37]["United Kingdom"].sum()



    def TopThreeCountriesMedian(self):
        self.filter4 = self.dataFrame[26: 37]["United Kingdom"].median()
        #print(self.filter4)

        self.filter5 = self.dataFrame[26: 37]["Germany"].median()
        #print(self.filter5)

        self.filter6 = self.dataFrame[26: 37]["Netherlands"].median()
        #print(self.filter6)

        print(f'Median for the United Kingdom is: {self.filter4}.')
        print(f'Median for the Germany is: {self.filter5}.')
        print(f'Median for the Netherlands is: {self.filter6}.')

    def TopThreeCountriesSum(self):
        self.filter7 = self.dataFrame[26: 37]["United Kingdom"].sum()
        #print(self.filter7)

        self.filter8 = self.dataFrame[26: 37]["Germany"].sum()
        #print(self.filter8)

        self.filter9 = self.dataFrame[26: 37]["Netherlands"].sum()
        #print(self.filter9)

        print(f'The top 3 countries in Europe that visitors visit are United Kingdom {self.filter7}, Germany {self.filter8}, Netherlands {self.filter9}')


    # def sumCountries(self):
    #
    #     self.sum1 = self.dataFrame["United Kingdom"].sum()
    #     self.sum2 = self.dataFrame["Germany"].sum()
    #     self.sum3 = self.dataFrame["France"].sum()
    #     self.sum4 = self.dataFrame["Italy"].sum()
    #     self.sum5 = self.dataFrame["Netherlands"].sum()
    #     self.sum6 = self.dataFrame["Greece"].sum()
    #     self.sum7 = self.dataFrame["Belgium & Luxembourg"].sum()
    #     self.sum8 = self.dataFrame["Switzerland"].sum()
    #     self.sum9 = self.dataFrame["Austria"].sum()
    #     self.sum10 = self.dataFrame["Scandinavia"].sum()
    #     self.sum11 = self.dataFrame["CIS & Eastern Europe"].sum()
    #
    #     print(self.sum1)
    #     print(self.sum2)
    #     print(self.sum3)
    #     print(self.sum4)
    #     print(self.sum5)
    #     print(self.sum6)
    #     print(self.sum7)
    #     print(self.sum8)
    #     print(self.sum9)
    #     print(self.sum10)
    #     print(self.sum11)
    #
    #     print(f'The top 3 countries in Europe that visitors visit are United Kingdom {self.sum1}, Germany {self.sum2}, Netherlands {self.sum5}')


    # def medianOfTopThree(self):
    #     self.median1 = self.dataFrame['United Kingdom'].median()
    #     self.median2 = self.dataFrame['Germany'].median()
    #     self.median3 = self.dataFrame['Netherlands'].median()
    #
    #     print(f'Median for the Top Three Countries is: {self.median1}.')
    #     print(f'Median for the Top Three Countries is: {self.median2}.')
    #     print(f'Median for the Top Three Countries is: {self.median3}.')

    # def meanOfTopThree(self):
    #     self.mean1 = self.dataFrame['United Kingdom'].mean()
    #     self.mean2 = self.dataFrame['Germany'].mean()
    #     self.mean3 = self.dataFrame['Netherlands'].mean()
    #
    #     print(f'Mean for the Top Three Countries is: {self.mean1}.')
    #     print(f'Mean for the Top Three Countries is: {self.mean2}.')
    #     print(f'Mean for the Top Three Countries is: {self.mean3}.')




    def chart1(self):
        self.whatineed = self.whatiwant[
            (self.whatiwant["year"].astype(int) >= 1979)&
            (self.whatiwant["year"].astype(int) <= 1982)
        ]
        # print(self.whatineed)

        plt.scatter(self.whatineed['United Kingdom'], self.whatineed['year'])
        plt.show();

    def chart2(self):
        self.ax = self.whatineed['Germany'].plot(kind='bar', title="Vistors", figsize=(10, 10), legend=True, fontsize=12)
        plt.show()




        #plt.scatter(self.dataFrame['United Kingdom'], self.dataFrame['year'])
        #plt.show();

        #self.targetRows = self.dataFrame[self.dataFrame["Year"].str.contains(“1980”)]
        #print(self.targetRows)


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

import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)
#       vv turns country code into lowercase
    df['country_code'] = country_code.lower()
#       vv gets the starting portion of the date (just the year)
    dfyear = df[df['date'].str.startswith(str(year))]
#       vv filters for country code using the already defined year variable
    dfcountry = dfyear[dfyear['iso_a3'].str.lower() == country_code]

    mean_price = dfcountry['dollar_price'].mean()

    rounded = round(mean_price, 2)

    return rounded



def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)


def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)


def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)


if __name__ == "__main__":

    # print(get_big_mac_price_by_year(2015, 'usa'))
    fun1year = int(input('what year?: '))
    fun1code = input('what code?: ')
    print(get_big_mac_price_by_year(fun1year, fun1code))
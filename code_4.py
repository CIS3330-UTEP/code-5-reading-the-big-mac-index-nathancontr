import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)

    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year

    df['currency_code'] = df['currency_code'].str.lower()

    query = (df['year'] == year) and (df['currency_code' == country_code])

    filter = df[query]

    mean_p = filter['dollar_price'].mean()

    return round(mean_p, 2)



def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)


def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)


def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)


if __name__ == "__main__":
    get_big_mac_price_by_year(2010, 'usa')
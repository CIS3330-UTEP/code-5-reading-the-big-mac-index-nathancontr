import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)

    country_code = str(country_code).lower()

    query = f"date.str.startswith('{year}') and iso_a3.str.lower() == '{country_code}'"

    yearavg_query = df.query(query)

    mean_year = yearavg_query['dollar_price'].mean()
    rounded = round(mean_year, 2)

    return rounded


def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)

    country_code = str(country_code).lower()


    query = f"(iso_a3.str.lower() == '{country_code}')"

    country_query = df.query(query)

    mean_country = country_query['dollar_price'].mean()
    rounded = round(mean_country, 2)

    return rounded


def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)

    query = f"date.str.startswith('{year}')"
    cheap_year_query = df.query(query)

    cheap = cheap_year_query['dollar_price'].idxmin()

    cheapest = cheap_year_query.loc[cheap]

    return f"{cheapest['name']}({cheapest['iso_a3']}): ${round(cheapest['dollar_price'], 2)}"


def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)

    query = f"date.str.startswith('{year}')"
    max_year_query = df.query(query)

    maxi = max_year_query['dollar_price'].idxmax()

    maxest = max_year_query.loc[maxi]

    return f"{maxest['name']}({maxest['iso_a3']}): ${round(maxest['dollar_price'], 2)}"

if __name__ == "__main__":
    
    print('Hello. Welcome to the Big Mac Index!')
    print('This code can tell you the: \
          \nAverage Price of a Big Mac in a Given Year \
          \nAverage Price of a Big Mac by Country \
          \nCheapest AND Most Expensive Big Mac in a Given Year \
          ')

    funyear = int(input('what Year would you like to search the database for?: '))
    funcode = input('what Country Code would you like to use?: ')

    print(f"\nThe average price of a Big Mac in '{funcode.upper()}' in {funyear} is ${get_big_mac_price_by_year(funyear, funcode)}")
    # print(get_big_mac_price_by_year(2015, 'usa'))
    # print(type(get_big_mac_price_by_year(2015, 'usa')))

    print(f"\nThe average price of a Big Mac in '{funcode.upper()}' is ${get_big_mac_price_by_country(funcode)}")
    # print(get_big_mac_price_by_country('USA'))
    # print(type(get_big_mac_price_by_country('USA')))
    
    print(f"\nThe cheapest big mac information for the year {funyear} is as follows: {get_the_cheapest_big_mac_price_by_year(funyear)}")
    # print(get_the_cheapest_big_mac_price_by_year(2019))

    print(f"\nThe most expensive big mac information for the year {funyear} is as follows: {get_the_most_expensive_big_mac_price_by_year(funyear)}")
    # print(get_the_most_expensive_big_mac_price_by_year(2019))

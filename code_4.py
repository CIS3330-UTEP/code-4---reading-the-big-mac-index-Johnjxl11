import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df= pd.read_csv(big_mac_file)
def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)
    get_country = df.query(f"(iso_a3 == '{country_code.upper()}') and (date >= '{year}-01-01' and date <= '{year}-12-31')")
    mean_price = round(float(get_country['dollar_price'].mean()), 2)
    return mean_price
    
    pass # Remove this line and code your function

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)
    get_country = df.query(f"(iso_a3 == '{country_code.upper()}')")
    mean_price = round(float(get_country['dollar_price'].mean()), 2)
    return mean_price
    

    pass # Remove this line and code your function

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    get_year = df.query(f"(date >= '{year}-01-01' and date <= '{year}-12-31')")
    get_min = get_year.loc[get_year['dollar_price'].idxmin()]
    get_round = round(get_min['dollar_price'], 2)
    get_output = (f"{get_min['name']}({get_min['iso_a3']}): ${get_round}")
    return get_output

    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    get_year = df.query(f"(date >= '{year}-01-01' and date <= '{year}-12-31')")
    get_min = get_year.loc[get_year['dollar_price'].idxmax()]
    get_round = round(get_min['dollar_price'], 2)
    get_output = (f"{get_min['name']}({get_min['iso_a3']}): ${get_round}")
    return get_output

    
    pass # Remove this line and code your function

if __name__ == "__main__":
    print(get_big_mac_price_by_year(2008,'arg'))
    print(get_big_mac_price_by_country('arg'))
    print(get_the_cheapest_big_mac_price_by_year(2008))
    print(get_the_most_expensive_big_mac_price_by_year(2003))





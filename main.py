from extract import extract
import pandas as pd


def main():
    """
    Run main function
    :return: --> Dataframe weather forecast by zip-code
    """
    weather = extract.Extracter().get_weather()
    # location.get_weather().to_csv(f"{zipcode}.csv", index=False)
    print(weather)
    # weather.to_csv("./files/final_test.csv")


if __name__ == '__main__':
    main()

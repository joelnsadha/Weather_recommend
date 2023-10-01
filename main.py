from extract import extract


lat = "34.0901"
lon = "-118.4065"


def main():
    beverly_hills = extract.Extracter(lat, lon)
    print(beverly_hills.get_weather())


if __name__ == '__main__':
    main()

from extract import extract


lat = "34.0901"
lon = "-118.4065"


def main():
    beverly_hills = extract.get_weather(lat, lon)
    print(beverly_hills)


if __name__ == '__main__':
    main()

def format_city_country(city: str, country: str) -> str:
    """
    Format the name of a city and country.

    :param city: Name of city.
    :param country: Name of country.

    :return: Returns the location in City, Country format.
    """
    returning = f"{city}, {country}"
    return returning.title()
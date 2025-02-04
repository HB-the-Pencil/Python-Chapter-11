def format_city_country(city: str, country: str, population=0) -> str:
    """
    Format the name of a city and country.

    :param city: Name of city.
    :param country: Name of country.
    :param population: Population of the city.

    :return: Returns the location in "City, Country - Population XXX" format.
    """
    returning = f"{city}, {country} - Population {population}"
    return returning.title()
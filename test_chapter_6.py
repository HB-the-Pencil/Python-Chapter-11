def mock_6_1():
    """Put the code for 6-1 in here."""
    person = {
        "first_name": "John",
        "last_name": "Studly",
        "city": "Catalina",
    }
    return person


def test_tiy_6_1():
    person = mock_6_1()

    assert type(person) == dict

    for key, value in person.items():
        assert type(key) == str
        assert type(value) == str


def mock_6_2():
    """Put the code for 6-2 in here."""
    favorite_numbers = {
        "john": 5,
        "joe": 17,
        "sally": 23,
        "jane": 14,
        "sue": 15,
    }
    return favorite_numbers


def test_tiy_6_2():
    favorite_numbers = mock_6_2()

    assert type(favorite_numbers) == dict
    assert len(favorite_numbers.keys()) >= 5

    for key, value in favorite_numbers.items():
        assert type(key) == str
        assert type(value) == int


def mock_6_3():
    """Put the code for 6-3 in here."""
    glossary = {
        "if": "A loop that runs if a condition is true.",
        "elif": "A loop that runs if the previous condition is false and the "
                "current condition is true.",
        "else": "A loop that runs if none of the previous conditions are "
                "true.",
        "and": "A logic operator that checks if two conditions are true.",
        "or": "A logic operator that checks if at least one condition is "
              "true.",
        "print": "A function that tells Python to print the string or "
                 "variable inside the parentheses."
    }
    return glossary


def test_tiy_6_3():
    glossary = mock_6_3()

    assert type(glossary) == dict
    assert len(glossary.keys()) >= 5

    for key, value in glossary.items():
        assert type(key) == str
        assert type(value) == str


def mock_6_4():
    """Put the code for 6-4 in here."""
    glossary = {
        "if": "A loop that runs if a condition is true.",
        "elif": "A loop that runs if the previous condition is false and the "
                "current condition is true.",
        "else": "A loop that runs if none of the previous conditions are "
                "true.",
        "and": "A logic operator that checks if two conditions are true.",
        "or": "A logic operator that checks if at least one condition is "
              "true.",
        "print": "A function that tells Python to print the string or "
                 "variable inside the parentheses.",
        "sorted": "A function that temporarily sorts the items in a list.",
        "set": "A list with no duplicate items, defined using curly braces.",
        "tuple": "An immutable list, defined using parentheses.",
        "dictionary": "A list of values that are assigned to keys.",
        "key": "The string representing the location of a value in a "
               "dictionary.",
        "value": "The data stored at the location of a key in a dictionary."
    }
    return glossary


def test_tiy_6_4():
    glossary = mock_6_4()

    assert type(glossary) == dict
    assert len(glossary.keys()) >= 10

    for key, value in glossary.items():
        assert type(key) == str
        assert type(value) == str


def mock_6_5():
    """Put the code for 6-5 in here."""
    rivers = {
        "missouri": "united states",
        "amazon": "south america",
        "yangtze": "china",
    }
    return rivers


def test_tiy_6_5():
    rivers = mock_6_5()

    assert type(rivers) == dict
    assert len(rivers.keys()) >= 3

    for key, value in rivers.items():
        assert type(key) == str
        assert type(value) == str


def mock_6_6():
    """Put the code for 6-6 in here."""
    favorite_languages = {
        "ian": "c++",
        "brian": "c#",
        "adam": "basic",
        "charlie": "rust",
    }

    people_to_survey = [
        "ian",
        "john",
        "michael",
        "adam",
        "charlie",
        "bill"
    ]
    return favorite_languages, people_to_survey


def test_tiy_6_6():
    favorite_languages, people_to_survey = mock_6_6()

    assert type(favorite_languages) == dict

    for key, value in favorite_languages.items():
        assert type(key) == str
        assert type(value) == str

    assert type(people_to_survey) == list

    has_answered = False
    has_not_answered = False

    for key in favorite_languages.keys():
        if key in people_to_survey:
            has_answered = True
        else:
            has_not_answered = True

    assert has_answered and has_not_answered


def mock_6_7():
    """Put the code for 6-7 in here."""
    gerald = {
        "first_name": "Gerald",
        "last_name": "Smith",
        "city": "Leo",
    }

    melany = {
        "first_name": "Melany",
        "last_name": "France",
        "city": "Dallas",
    }

    tod = {
        "first_name": "Tod",
        "last_name": "Lander",
        "city": "Philadelphia",
    }

    people = [gerald, melany, tod]

    return people


def test_tiy_6_7():
    people = mock_6_7()

    assert type(people) == list
    assert len(people) >= 3

    for item in people:
        assert type(item) == dict


def mock_6_8():
    """Put the code for 6-8 in here."""
    pets = [
        {
            "type": "cat",
            "name": "bella",
            "owner": "maxine",
        },
        {
            "type": "dog",
            "name": "annie",
            "owner": "jordan",
        },
        {
            "type": "fish",
            "name": "bop",
            "owner": "sammy",
        },
    ]

    return pets


def test_tiy_6_8():
    pets = mock_6_8()

    assert type(pets) == list
    assert len(pets) >= 3

    for item in pets:
        assert type(item) == dict


def mock_6_9():
    """Put the code for 6-9 in here."""
    favorite_places = {
        "mary": ["finland", "norway", "germany"],
        "gerald": ["jamaica", "iceland"],
        "sarah": ["france", "italy"],
    }

    return favorite_places


def test_tiy_6_9():
    favorite_places = mock_6_9()

    assert type(favorite_places) == dict

    for key, value in favorite_places.items():
        assert type(key) == str
        assert type(value) == list
        assert len(value) >= 1
        assert type(value[0]) == str


def mock_6_10():
    """Put the code for 6-10 in here."""
    favorite_numbers = {
        "john": [17, 11, 35],
        "marianne": [2, 13],
        "jacob": [10, 9, 8, 12, 16, 21, 22, 32],
        "elizabeth": [7, 21],
        "samuel": [0],
    }
    return favorite_numbers


def test_tiy_6_10():
    favorite_numbers = mock_6_10()

    assert type(favorite_numbers) == dict
    assert len(favorite_numbers.keys()) >= 5

    for key, value in favorite_numbers.items():
        assert type(value) == list
        assert len(value) >= 1
        assert type(value[0]) == int or type(value[0]) == float


def mock_6_11():
    """Put the code for 6-11 in here."""
    cities = {
        "fort wayne": {
            "country": "United States",
            "population": 267927,
            "fact": "Fort Wayne is the 83rd largest city in the United States."
        },
        "stockholm": {
            "country": "Sweden",
            "population": 987661,
            "fact": "Stockholm contains over 50 bridges."
        },
        "chicago": {
            "country": "United States",
            "population": int(2.665e6),
            "fact": "Chicago is the 3rd largest city in the United States."
        }
    }
    return cities


def test_tiy_6_11():
    cities = mock_6_11()

    assert type(cities) == dict
    for key, value in cities.items():
        assert type(key) == str
        assert type(value) == dict
        assert len(value.keys()) >= 3


# Because TIY 6-12 is so open-ended, it cannot be tested (there's no way to
# know what the person added).
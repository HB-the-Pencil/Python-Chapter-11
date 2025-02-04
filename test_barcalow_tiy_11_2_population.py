from barcalow_tiy_11_2_population import format_city_country

def test_city_country():
    santiago = format_city_country("santiago", "chile")
    assert santiago == "Santiago, Chile - Population 0"


def test_city_country_population():
    santiago = format_city_country("santiago", "chile", 5_000_000)
    assert santiago == "Santiago, Chile - Population 5000000"
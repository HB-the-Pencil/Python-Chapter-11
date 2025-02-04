from barcalow_tiy_11_1_city_country import format_city_country

def test_city_country():
    santiago = format_city_country("santiago", "chile")
    assert santiago == "Santiago, Chile"
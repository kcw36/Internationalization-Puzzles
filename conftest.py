# pylint: skip-file

import pytest
from world_trip.world_trip import get_dicts_from_txt
from step_in.step_in import get_park_from_txt
from mojibake.mojibake import get_inputs_from_txt, degarble


@pytest.fixture
def test_message():
    return ["néztek bele az „ártatlan lapocskába“, mint ahogy belenézetlen mondták ki rá a halálos itéletet a sajtó csupa 20–30 éves birái s egyben hóhérai.",
            "livres, et la Columbiad Rodman ne dépense que cent soixante livres de poudre pour envoyer à six milles son boulet d'une demi-tonne.  Ces",
            "Люди должны были тамъ и сямъ жить въ палаткахъ, да и мы не были помѣщены въ посольскомъ дворѣ, который также сгорѣлъ, а въ двухъ деревянныхъ", "Han hade icke träffat Märta sedan Arvidsons middag, och det hade gått nära en vecka sedan dess. Han hade dagligen promenerat på de gator, där"]


@pytest.fixture
def test_recordings():
    return ["2019-06-05T08:15:00-04:00",
            "2019-06-05T14:15:00+02:00",
            "2019-06-05T17:45:00+05:30",
            "2019-06-05T05:15:00-07:00",
            "2011-02-01T09:15:00-03:00",
            "2011-02-01T09:15:00-05:00"]


@pytest.fixture
def test_input():
    return get_dicts_from_txt("test_input.txt")


@pytest.fixture
def test_park():
    return get_park_from_txt("test_input.txt")


@pytest.fixture
def test_mojibake():
    words, puzzle = get_inputs_from_txt("test_input.txt")
    return (degarble(words), puzzle)

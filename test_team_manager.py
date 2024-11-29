#  Copyright (c) 2024. William E. Kitson

from team_manager import TeamManager
import sqlite3

connection_string = "4kitsw10_COM519_database"

def test_add():
    team_manager = TeamManager(connection_string)

    for i in range(0, 5):
        team_manager.add_team(
            f"forename_{i}",
            f"surname_{i}",
            f"1998-01-0{i + 1}",
        )

    database = sqlite3.connect(connection_string)
    cursor = database.cursor()

    cursor.execute(
        "SELECT * "
        "FROM Staff"
    )

    for index, i in enumerate(cursor.fetchall()):
        comparison = (
            f"forename_{index}_surname_{index}",
            f"forename_{index}surname_{index}1998-01-0{index + 1}",
            f"forename_{index}",
            f"surname_{index}",
            f"1998-01-0{index + 1}",
        )

        result = (
            i[1],
            i[2],
            i[3],
            i[4],
            i[5]
        )

        assert(comparison == result)
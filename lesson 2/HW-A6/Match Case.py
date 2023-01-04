country = input("please insert a country: ")

match country.split():
    case["USA"]:
        print("Dollar")
    case["Israel"]:
        print("New Israel Shequel (NIS)")
    case["United Kingdom (UK)"]:
        print("pound")
    case ["Austria"] | ["Belgium"]|["Cyprus"] | ["Estonia"] | ["Finland"] | ["France"]\
            | ["Germany"] | ["Greece"] | ["Ireland"] | ["Italy"] | ["Latvia"]\
            | ["Lithuania"] | ["Luxembourg"] | ["Malta"] | ["Netherlands"] | ["Portugal"]\
            | ["Slovakia"] | ["Slovenia"] | ["Spain"]:
        print("Euro")
    case _:
        print("I don't know")

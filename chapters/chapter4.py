
data_base : list[tuple[str, str]] = [("saleem", "123"),
                                     ("saram", "345"),
                                     ("nadeem", "321")
                                     ]
for row in data_base:
    user, password = row
    print(user, password)

"""Print out all the melons in our inventory."""


from melons import melons 


def print_melons(melons):
    """Print each melon with corresponding attribute information."""

    for melon_type, params in melons.items():
        print(melon_type.upper())
        for param, value in params.items():
            print(f'{param}: {value}')
        print("")

print_melons(melons)
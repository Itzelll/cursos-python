def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late."""
    order = arrivals.index(name)
    return (order >= len(arrivals) / 2 and order != len(arrivals) - 1)


party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
print(fashionably_late(party_attendees, "Owen"))
print(fashionably_late(party_attendees, "Mona"))
def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa."""
    
    aux = racers[0]
    racers[0] = racers[-1]
    racers[-1] = aux
    return racers
    
    
r = ["Mario", "Bowser", "Luigi"] 
print(purple_shell(r))
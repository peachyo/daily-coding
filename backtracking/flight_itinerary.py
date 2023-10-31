def get_itinerary(flights, current_itinierary):
    if not flights:
        return current_itinierary
    last_stop = current_itinierary[-1]
    for i, (origin, destination) in enumerate(flights):
        flights_minus_current = flights[:i] + flights[i+1:]
        current_itinierary.append(destination)
        if origin == last_stop:
            return get_itinerary(flights_minus_current, current_itinierary)
        current_itinierary.pop()
    return None


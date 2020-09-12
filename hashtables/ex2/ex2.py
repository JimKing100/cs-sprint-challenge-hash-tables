#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hash = {}
    route = []
    for i in range(length):
        hash[tickets[i].source] = tickets[i].destination
    next = hash['NONE']
    route.append(next)
    for i in range(1, length):
        next = hash[next]
        route.append(next)

    return route

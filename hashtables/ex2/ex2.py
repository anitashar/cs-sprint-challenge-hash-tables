# #  Hint:  You may not need all of these.  Remove the unused functions.
# class Ticket:
#     def __init__(self, source, destination):
#         self.source = source
#         self.destination = destination


# def reconstruct_trip(tickets, length):
#     """
#     YOUR CODE HERE
#     """
#     

#     return route

#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Your code here
    
# starting location is the key and
# the destination is the value
# create a list of routes

    route = []
    dicty = {}
    #  going through all the tickets
    for i in tickets:
        dicty[i.source] = i.destination

    route.append(dicty["NONE"])
    final_destination = dicty["NONE"]
# if we have destination
    while final_destination != "NONE":
        if final_destination == "NONE":
            continue
        else:
            route.append(dicty[final_destination])
            final_destination = dicty[final_destination]
    return route
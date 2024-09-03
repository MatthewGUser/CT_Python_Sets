# [ Task 1 ]

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

shared_routes = our_routes.intersection(competitor_routes)
print("Destinations both airlines fly to:", shared_routes)

unique_to_our_airline = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", unique_to_our_airline)

all_routes = our_routes.union(competitor_routes)
neither_shared_routes = all_routes.difference(our_routes.intersection(competitor_routes))
print("Destinations that are not shared by both airlines:", neither_shared_routes)

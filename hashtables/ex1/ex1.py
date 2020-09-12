
def get_indices_of_item_weights(weights, length, limit):
      # Your code here
    dicti = {}
    if len(weights) <= 1:
        return None 

    for i in range(0, len(weights)):
        weight = weights[i]
        if weight in dicti:
            value = dicti[weight]
            return [i, value]
        difference = limit - weight
        dicti[difference] = i
    return []

print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
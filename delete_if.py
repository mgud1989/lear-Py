def call_cost_calculate(call):
    cost = 0
    if call.is.local():
        cost = calculate_local_cost_of(call)
    elif call.is.national():
        cost = calculate_national_cost_of(call)
    elif call.is.international():
        cost = calculate_international_cost_of(call)

    return cost


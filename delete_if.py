def call_cost_calculate(call):
    cost = 0
    if call.is.local():
        cost = calculate_local_cost_of(call)
    elif call.is.national():
        cost = calculate_national_cost_of(call)
    elif call.is.international():
        cost = calculate_international_cost_of(call)

    return cost

class CallCostCalculator(object):
    def m(self):
        raise NotImplementedError("Subclass Responsability")
class LocalCallCostCalculator(CallCostCalculator):
    def m(self):
        #codigo de calculate_local_cost_of
class NationalCallCostCalculator(CallCostCalculator):
    def m(self):
        #codigo de calculate_national_cost_of
class InternationalCallCostCalculator(CallCostCalculator):
    def m(self):
        #codigo de calculate_international_cost_of
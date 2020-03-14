
class CallCostCalculator(object):
    @classmethod
    def to_handle(klass, call):
        #codigo que busca el CallCostCalculator correspondiente

    def calculate(self):
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

cost_calculator = CallCostCalculator.to_handle(call)
cost_calculator.calculate()
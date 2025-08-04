class DemandModel:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_quantity(self, price):
        return max(self.a - self.b * price, 0)

    def calculate_revenue(self, price):
        return price * self.calculate_quantity(price)

    def calculate_elasticity_at_point(self, price):
        q = self.calculate_quantity(price)
        return (self.b * price) / q if q != 0 else 0

    def get_elasticity_classification(self, price):
        e = abs(self.calculate_elasticity_at_point(price))
        if e > 1:
            return "Elástico"
        elif e == 1:
            return "Unitário"
        return "Inelástico"

    def generate_demand_curve(self, price_range):
        prices = list(range(int(price_range[0]), int(price_range[1]) + 1))
        quantities = [self.calculate_quantity(p) for p in prices]
        return prices, quantities

    def generate_revenue_curve(self, price_range):
        prices = list(range(int(price_range[0]), int(price_range[1]) + 1))
        revenues = [self.calculate_revenue(p) for p in prices]
        return prices, revenues

    def find_revenue_maximizing_price(self, price_range):
        prices, revenues = self.generate_revenue_curve(price_range)
        return prices[revenues.index(max(revenues))]

def compare_segments(models, price):
    return {
        seg: {
            "quantity": m.calculate_quantity(price),
            "revenue": m.calculate_revenue(price),
            "elasticity": m.calculate_elasticity_at_point(price)
        }
        for seg, m in models.items()
    }

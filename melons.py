"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """A parent class for child classes to reference"""
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price."""

        base_price = 5
        christmas_melon_price = 1.5 * base_price

        total = (1 + self.tax) * self.qty * base_price

        if self.species == "Christmas":
            total = (1 + self.tax) * self.qty * christmas_melon_price

        if self.order_type == "international":
            if self.qty < 10:
                total += 3

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder,self).__init__(species, qty)
        self.order_type = "international"
        self.tax = 0.170
        self.country_code = country_code



    def get_country_code(self):
        """Return the country code."""

        return self.country_code

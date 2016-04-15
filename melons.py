"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    """AbstractMelon class."""

    def __init__(self, species, qty, country_code=None):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        # self.tax = None
        # self.order_type = None
        if country_code:
            self.country_code = country_code


    def get_total(self):
        """Calculate price."""

        base_price = 5

        if self.species == "Christmas melons":  # If Christmas melons is passed as an argument, then base price is 1.5 * base.
            base_price = base_price * 1.5

        if self.order_type == "international":  # Need to fix lines 25-27
            if self.qty < 10:
                total = (1 + self.tax) * self.qty * base_price + self.flat_fee
        

        total = (1 + self.tax) * self.qty * base_price

        
        # if self.country_code != "US":
        #     if self.qty < 10:
        #         flat_fee = 3
        #         total = total + flat_fee

        return total 

    def mark_shipped(self):
        """Set shipped to true."""

        self.mark_shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    tax = 0.08
    order_type = "domestic"

    # def __init__(self, species, qty):
    #     """Initialize melon order attributes."""
    #     super(DomesticMelonOrder, self).__init__(species, qty)  # From the superclass of DomesticMelonOrder, get the method name __init__ and pull the info from species, qty
    #     self.order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    
    tax = 0.17
    order_type = "international"
    flat_fee = 3


    # Below code works.

    # def __init__(self, species, qty, country_code):
    #     """Initialize melon order attributes."""
    #     super(InternationalMelonOrder, self).__init__(species, qty)
    #     self.order_type = "international"
    #     self.country_code = country_code
    #     self.tax = 0.17


    # Not sure if below code is needed.

    # def get_country_code(self):
    #     """Return the country code."""

    #     return self.country_code

# class DomesticMelonOrder(object):
#     """A domestic (in the US) melon order."""

#     def __init__(self, species, qty):
#         """Initialize melon order attributes"""

#         self.species = species
#         self.qty = qty
#         self.shipped = False
#         self.order_type = "domestic"
#         self.tax = 0.08

    # def get_total(self):
    #     """Calculate price."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price
    #     return total

    # def mark_shipped(self):
    #     """Set shipped to true."""

    #     self.shipped = True


# class InternationalMelonOrder(object):
#     """An international (non-US) melon order."""

#     def __init__(self, species, qty, country_code):
#         """Initialize melon order attributes"""

#         self.species = species
#         self.qty = qty
#         self.country_code = country_code
#         self.shipped = False
#         self.order_type = "international"

#         self.tax = 0.17

    # def get_total(self):
    #     """Calculate price."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price
    #     return total

    # def mark_shipped(self):
    #     """Set shipped to true."""

    #     self.shipped = True

    # def get_country_code(self):
    #     """Return the country code."""

    #     return self.country_code

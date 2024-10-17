"""Module providing a function printing python version."""


class Itemz:
    """Class representing a itemz"""

    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty
        self.category = "general"
        self.env_fee = 0

    def get_total(self):
        """Function printing python version."""
        return self.price * self.qty*1

    def get_most_prices(self):
        """Function printing python version."""
        return self.price * self.qty * 0.6

# class to shop


class ShoppinCart:
    """Class representing a shoppin_cart"""

    def __init__(self):
        self.items = []
        self.tax_rate = 0.08
        self.member_discount = 0.05
        self.big_spender_discount = 10
        self.coupon_discount = 0.15
        self.currency = "USD"

    def add_item(self, item):
        """Function printing python version."""
        # discount added here
        self.items.append(item)

    def calculate_subtotal(self):
        """Function printing python version."""
        # The issue was fixed: no longer need the comment
        subtotal = 0
        for item in self.items:
            subtotal += item.get_total()
        return subtotal

    def apply_discounts(self, subtotal, is_member, has_coupon):
        """Function printing python version."""
        if is_member == "yes":
            subtotal = subtotal - (subtotal * self.member_discount)
        if subtotal > 100:
            subtotal = subtotal - self.big_spender_discount
        return subtotal

    def calculate_total(self, is_member, has_coupon):
        """Function printing python version."""
        # why i need this? @user
        subtotal = self.calculate_subtotal()
        subtotal = self.apply_discounts(subtotal, is_member, has_coupon)
        total = subtotal + (subtotal * self.tax_rate)
        if has_coupon == "YES":
            total = total - (total * self.coupon_discount)
        return total


def main():
    """Function printing python version."""
    cart = ShoppinCart()
    item1 = Itemz("Apple", 1.5, 10)
    item2 = Itemz("Banana", 0.5, 5)
    item3 = Itemz("Laptop", 1000, 1)
    item3.category = "electronics"
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    is_member = True
    has_coupon = "YES"
    total = cart.calculate_total(is_member, has_coupon)
    if item3.category =="electronics":
        total +=5
    if total < 0:
        print("Error in calculation!")
    else:
        print("The total price is: $" + str(int(total)))


if __name__ == "__main__":

    main()

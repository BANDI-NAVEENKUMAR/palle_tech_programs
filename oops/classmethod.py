class cart:
    flat_discount = -150
    min_bill = 50
    @classmethod
    def update_flat_discount(cls,new_flat_discount):
        cls.flat_discount = new_flat_discount

    @classmethod
    def increase_flate_discount(cls,amount):
        new_flat_discount = cls.flat_discount + amount
        cls.update_flat_discount(new_flat_discount)
cart.increase_flate_discount(222)
print(cart.flat_discount)

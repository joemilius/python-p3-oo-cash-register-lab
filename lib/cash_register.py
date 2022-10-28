#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_price = 0
    self.quantity = 0
    pass

  def add_item(self, name, price, quantity = 1):
    for number in range(quantity):
      self.items.append(name)
      self.total += price
      self.last_price = price
      self.quantity = quantity
    
  def apply_discount(self):
    if self.discount == 0:
      print('There is no discount to apply.')
    else:
      discount = self.discount / 100
      self.total = self.total - (self.total * discount)
      print(f'After the discount, the total comes to ${int(self.total)}.')

  def void_last_transaction(self):
    total_void = self.quantity * self.last_price
    self.total -= total_void
    return self.total
  
  pass

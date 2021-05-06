class ShoppingCart:
    # write your code here
    def __init__(self, total=0, emp_discount=None, items=[], prices = []):
        self.total = sum([i['item_price']*i['quantity'] for i in items])
        self.employee_discount = emp_discount
        self.items = items
        self.prices = prices
    def add_item(self, name, price, quantity=1):
        self.items.append({'item_name': name, 'item_price':price, 'quantity': quantity})
        self.total += price*quantity
        return self.total
            
    def mean_item_price(self):
        num_items = sum(i['quantity'] for i in self.items)
        total = self.total
        mean = total/num_items
        return round(mean,2)

    def find_median(self):
        length = len(self.prices)
        if (length%2 == 0):
            mid_first = int(length/2)
            mid_second = mid_first - 1
            median = (self.prices[mid_first] + self.prices[mid_second])/2
            return round(median, 2)
        else: med = int(length/2)
        return round(self.prices[med],2)
    
    def median_item_price(self):
        for i in self.items:
            if i['quantity'] > 1:
                for q in range(i['quantity']):
                    self.prices.append(i['item_price'])
            else: self.prices.append(i['item_price'])
        self.prices.sort()
        return self.find_median()
        

    def apply_discount(self):
        if self.employee_discount:
            discount = self.employee_discount/100
            disc_total = self.total * (1 - discount)
            return disc_total
        else:
            return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
        else:
            return "There are no items in your cart!"
        self.total -= removed_item['item_price']
        
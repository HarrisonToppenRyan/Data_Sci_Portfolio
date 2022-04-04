import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])


visits_cart_merge = pd.merge(visits, cart, how='left')


num_nulls = len(visits_cart_merge[visits_cart_merge.cart_time.isnull()])
not_t_shirt_buyer = float(num_nulls / len(visits_cart_merge)) * 100 
print(visits_cart_merge)



checkout_cart_merge = pd.merge(cart, checkout, how='left')

print(checkout_cart_merge)

num_nulls2 = len(checkout_cart_merge[checkout_cart_merge.checkout_time.isnull()])


not_t_shirt_buyer2 = float(num_nulls2 / len(checkout_cart_merge)) * 100
print(not_t_shirt_buyer) 
print(not_t_shirt_buyer2)

all_data = visits\
  .merge(cart, how='left')\
  .merge(checkout, how='left')\
  .merge(purchase, how='left')



checkout_purchase = pd.merge(checkout, purchase, how='left')
checkout_purchase_rows = len(checkout_purchase)
not_purchased = len(checkout_purchase[checkout_purchase.purchase_time.isnull()])
print(not_t_shirt_buyer) 
print(not_t_shirt_buyer2)
print(float(not_purchased / checkout_purchase_rows) * 100)


all_data['time_to_purchase'] = (all_data.purchase_time - all_data.visit_time)

print(all_data.time_to_purchase.mean())

  

price = float(input('Enter price: '))
discount = float(input('Enter discount %: '))
reduction = price * discount/100
price_w_dsc = price - reduction
print(f'Price with discount is {price_w_dsc:.2f}')
print(f'reduction is {reduction:.2f}')
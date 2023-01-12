sf_books = int(input("insert amount of science fiction books: "))
com_books = int(input("insert amount of comics books: "))
his_books = int(input("insert amount of history books: "))

sf_books_price = sf_books * 58
com_books_price = com_books * 32
his_books_price = his_books * 24

tot_payment = sf_books_price + com_books_price + his_books_price

if sf_books >= 3:
    sf_books_price = 0.9 * sf_books * 58

if his_books // 3 != 0:
    his_books_price = (his_books // 3) * 48 + (his_books % 3) * 24

price_after_discount = sf_books_price + com_books_price + his_books_price

if tot_payment > 300:
    price_after_discount = price_after_discount - 20

print(f"total before discount is: {tot_payment}")
print(f"total discount is: {tot_payment - price_after_discount}")
print(f"the final price is: {price_after_discount}")

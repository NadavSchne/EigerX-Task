def priceCheck(products, productPrices, productSold, soldPrice):
    errors = 0
    product_prices = {}                                                          # creating a dict for products and prices

    for product, price in zip(products, productPrices):                          # using zip to iterate over tuples and set them into the dict

        product_prices[product] = price

    for i in range(len(productSold)):                                            # running on all sold products
        if product_prices[productSold[i]] != soldPrice[i]:                       # correct product price compare to sold product price
            errors += 1                                                          # comparing our 'Dict' against soldPrice list.
    return errors


def test_priceCheck():                                                           # writing 3 different cases in order to check our function
    products = ['eggs', 'milk', 'cheese']
    productPrices = [2.89, 3.29, 5.79]
    productSold = ['eggs', 'eggs', 'cheese', 'milk']
    soldPrice = [2.89, 2.99, 5.97, 3.29]
    assert priceCheck(products, productPrices, productSold, soldPrice) == 2      # in case there's a mistake,
                                                                                    # assert will exit the program
    products = ['apple', 'orange', 'banana']
    productPrices = [0.5, 0.6, 0.4]
    productSold = ['apple', 'banana', 'orange', 'orange']
    soldPrice = [0.5, 0.4, 0.6, 0.5]
    assert priceCheck(products, productPrices, productSold, soldPrice) == 1

    products = ['book', 'pen']
    productPrices = [20, 5]
    productSold = ['book', 'pen']
    soldPrice = [20, 5]
    assert priceCheck(products, productPrices, productSold, soldPrice) == 0

    print("All test cases pass")


test_priceCheck()                                                                # calling our test function

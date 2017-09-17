bookCost = 24.95
discount = 40
initialShippingCost = 3
recurringShippingCost = 0.75
numberOfCopies = 60
discountedBookCost = bookCost * ((100 - discount)/100)

totalCost = (discountedBookCost * numberOfCopies) + (initialShippingCost + ((numberOfCopies - 1) * recurringShippingCost))

print (totalCost)

#!/usr/bin/python
import sys
def reducer():
  maxSaleProduct = None
  maxSale = 0.0
  currentSale = 0.0
  currentSaleProduct = None
  oldKey=None

  for line in sys.stdin:
    data=line.strip().split("\t")
    if len(data)!=3:
      continue

    thisKey,thisItem,thisSale=data

    if oldKey and oldKey != thisKey:
      if currentSale > maxSale:
        maxSaleProduct = currentSaleProduct
        maxSale = currentSale
      print "{0}\t{1}\t{2}".format(oldKey,maxSaleProduct,maxSale) 
      maxSale=0.0
      maxSaleProduct = None
      currentSale = 0.0
      currentSaleProduct = None 
    oldKey=thisKey

    if (currentSaleProduct != thisItem):
      if currentSaleProduct:
        if currentSale > maxSale:
          maxSale = currentSale
          maxSaleProduct = currentSaleProduct
        currentSale = 0
    currentSale += float(thisSale)
    currentSaleProduct = thisItem
    
  if currentSale > maxSale:
    maxSaleProduct = currentSaleProduct
    maxSale = currentSale
  if oldKey != None:
    print "{0}\t{1}\t{2}".format(oldKey,maxSaleProduct,maxSale)
def main():
  reducer()
main()
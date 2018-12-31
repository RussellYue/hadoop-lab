#!/usr/bin/python
import sys
def reducer():
  maxSaleItem = None
  maxSale = None
  oldKey=None
  for line in sys.stdin:
    data=line.strip().split("\t")
    if len(data)!=3:
      continue
    thisKey,thisItem,thisSale=data
    if oldKey and oldKey != thisKey:
      print "{0}\t{1}\t{2}".format(oldKey,maxSaleItem,maxSale) 
      maxSale=None
      maxSaleItem = None
    oldKey=thisKey
    if (not maxSaleItem) or (float(maxSale) < float(thisSale)):
      maxSale = thisSale
      maxSaleItem = thisItem
  if oldKey != None:
    print "{0}\t{1}\t{2}".format(oldKey,maxSaleItem,maxSale)
def main():
  reducer()
main()
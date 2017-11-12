import pandas as pd
import numpy as np
import os
# import matplotlib.pyplot as plt

from grader import Grader


# load data
DATA_FOLDER = '../readonly/final_project_data/'

transactions = pd.read_csv(os.path.join(DATA_FOLDER, 'sales_train.csv'))
items = pd.read_csv(os.path.join(DATA_FOLDER, 'items.csv'))
item_categories = pd.read_csv(os.path.join(DATA_FOLDER, 'item_categories.csv'))
shops = pd.read_csv(os.path.join(DATA_FOLDER, 'shops.csv'))

grader = Grader()

print "shape of transactions: "
print transactions.shape
print "shape of items:"
print items.shape
print "shape of item categories: "
print item_categories.shape
print "shape of shops:"
print shops.shape

print "head of transactions:"
print transactions.head()
print "head of items:"
print items.head()
print "head of item categories:"
print item_categories.head()
print "head of shops:"
print shops.head()


# max_revenue =
# grader.submit_tag('max_revenue', max_revenue)
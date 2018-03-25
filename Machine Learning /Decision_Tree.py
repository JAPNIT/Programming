import csv, numpy, pandas, random, operator
from sklearn.preprocessing import Normalizer
from scipy import stats
from sklearn.model_selection import KFold

#importing data set into variable data as a numpy list
filename = 'glass_data_input.csv'
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')

random.shuffle(data)
train = data[:170]
test = data[170:]

#dicretize data


def entropy():
    pass

def info_gain():
    pass

def choose_attribute():
    pass # uses entropy and information gain

def create_decision_tree():
    pass # recursively creates a tree or subtreesusing the attribute chosen
    #if unable to classify -- returns a default value that is th highest frequency 
    #recurse for each sub tree except when a subset is pure

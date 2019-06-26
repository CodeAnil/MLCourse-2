#Market Basket Analyses

#Importing lib's
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


#Read the Pandas DataFrame

df = pd.read_excel('/Users/kszm146/git-codebases/mydevelopment/github/Machine-Learning/Subradeep-Code/Online_Retail.xlsx')
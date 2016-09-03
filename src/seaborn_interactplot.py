import seaborn as sns

import pandas as pd
from pyspark.context import SparkContext
from pyspark.sql.context import SQLContext
import seaborn as sns
from seaborn.matrix import ClusterGrid
import matplotlib.pyplot as plt
import scipy

sns.set(style="white",palette="pastel")

import sys

if len(sys.argv) > 1 and sys.argv[1] == "-test":
    import os
    df = pd.read_csv("Datasets/DRUG1N.csv")
    x1_field = "Na"
    x2_field = "K"
    y_field = "Age"
    output_option = 'output_to_screen'
    output_path = '/tmp/foo.html'
    title_font_size = 24
    title = "Test Test Test Test Test Test"
    filled = True

else:
    import spss.pyspark.runtime
    ascontext = spss.pyspark.runtime.getContext()
    sc = ascontext.getSparkContext()
    sqlCtx = ascontext.getSparkSQLContext()
    df = ascontext.getSparkInputData().toPandas()
    x1_field = '%%x1_field%%'
    x2_field = '%%x2_field%%'
    y_field = '%%y_field%%'
    output_option = '%%output_option%%'
    output_path = '%%output_path%%'
    title_font_size = int('%%title_font_size%%')
    title = '%%title%%'
    filled = ('%%filled%%' == 'Y')

g = sns.interactplot(x1_field,x2_field,y_field,df,levels=50,filled=filled)

if output_option == 'output_to_file':
    if not output_path:
        raise Exception("No output path specified")
else:
    from os import tempnam
    output_path = tempnam()+".svg"

sns.plt.title(title,fontsize=title_font_size)

sns.plt.savefig(output_path)

if output_option == 'output_to_screen':
    import webbrowser
    webbrowser.open(output_path)
    print("Output should open in a browser window")
else:
    print("Output should be saved on the server to path: "+output_path)
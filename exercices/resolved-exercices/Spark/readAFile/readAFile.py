#!/usr/bin/python


import os
import sys

import findspark

findspark.init()


from pyspark import SparkConf, SparkContext

if __name__ == "__main__":
 
  # create Spark context with Spark configuration
  conf = SparkConf().setAppName("Read Text to RDD - Python")
  sc = SparkContext(conf=conf)
 
  # read input text file to RDD
  lines = sc.textFile("/home/developer/work/da-academy/exercices/resolved-exercices/hadoop/readAFile/sampleText.txt")
 
  # collect the RDD to a list
  llist = lines.collect()
 
  # print the list
  for line in llist:
    print(line)

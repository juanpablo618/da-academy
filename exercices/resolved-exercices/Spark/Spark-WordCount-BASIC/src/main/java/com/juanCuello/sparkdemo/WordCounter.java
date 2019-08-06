package com.juanCuello.sparkdemo;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import scala.Tuple2;

import java.util.Arrays;


//Apache Spark Example: Word Count Program in Java
public class WordCounter {

    private static void wordCount(String fileName) {

        //The object this class is used to set various Spark parameters as key-value pairs for the program
        //The master specifies local which means that this program should connect to Spark thread running on the localhost.
        //App name is just a way to provide Spark with the application metadata.
        SparkConf sparkConf = new SparkConf().setMaster("local").setAppName("JD Word Counter");

        //after that we can create a sparkContext
        //Use SparkContext to work with RDD and sparkSession to work with dataSets and dataFrames
        JavaSparkContext sparkContext = new JavaSparkContext(sparkConf);

        /*
        * Spark considers every resource it gets to process as an RDD (Resilient Distributed Datasets) which helps it
         * to organise the data in a find data structure which is much more efficient to be analysed. We will now
         * convert the input file to a JavaRDD object itself
        * */

        JavaRDD<String> inputFile = sparkContext.textFile(fileName);



        //Start working with JavaRDD
        // Always a map is a transformation that passes each dataset element through a function and returns a new RDD
        // representing the results
        JavaRDD<String> wordsFromFile = inputFile.flatMap(content -> Arrays.asList(content.split(" ")));

        // provide a word, number pair which can be presented as an output
        JavaPairRDD countData = wordsFromFile.mapToPair(t -> new Tuple2(t, 1)).reduceByKey((x, y) -> (int) x + (int) y);

        //save the output file as a text file
        countData.saveAsTextFile("CountData");




    }

    public static void main(String[] args) {

        if (args.length == 0) {
            System.out.println("No files provided.");
            System.exit(0);
        }

        wordCount(args[0]);
    }
}

package com.juanCuello.sparkdemo;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.Function;
import org.apache.spark.sql.SparkSession;

public class Main {

    public static void main(String[] args) {

        SparkConf conf= new SparkConf().setAppName("Java Spark").setMaster("local[*]");

        SparkSession spark = SparkSession
                .builder()
                .config(conf)
                .getOrCreate();

        JavaSparkContext sc = new JavaSparkContext();
        JavaRDD<String> lines=sc.textFile("/home/developer/Downloads/weblog.csv");
        JavaRDD<String> filteredLines = lines.filter(new Function<String, Boolean>() {

            private static final long serialVersionUID = -7797014772600159088L;

            @Override
            public Boolean call(String arg0) throws Exception {
                // TODO Auto-generated method stub
                return null;
            }
        });





    }

}

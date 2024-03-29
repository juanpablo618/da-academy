package com.mkyong.core;

import java.net.UnknownHostException;
import com.mongodb.BasicDBObject;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.MongoClient;
import com.mongodb.MongoException;

/**
 * Java + MongoDB Hello world Example
 *
 *  to delete db
 *  use testdb
 *  db.dropDatabase()
 * 
 */
public class App {
	public static void main(String[] args) {

		try {
			long startTime = System.nanoTime();

			/**** Connect to MongoDB ****/
			// Since 2.10.0, uses MongoClient
			MongoClient mongo = new MongoClient("localhost", 27017);

			/**** Get database ****/
			// if database doesn't exists, MongoDB will create it for you
			DB db = mongo.getDB("testdb");

			/**** Get collection / table from 'testdb' ****/
			// if collection doesn't exists, MongoDB will create it for you
			DBCollection table = db.getCollection("user");

			/**** Insert ****/
			// create a document to store key and value

			for (int i =0 ; i<=1000;i++){
			BasicDBObject document = new BasicDBObject();
			document.put("name"+i, "mkyong"+i);
			document.put("age"+i, 30+i);
			table.insert(document);
			}
			/**** Find and display ****/
			//BasicDBObject searchQuery = new BasicDBObject();
			//searchQuery.put("name", "mkyong");

			//DBCursor cursor = table.find(searchQuery);

			//while (cursor.hasNext()) {
			//	System.out.println(cursor.next());
			//}

			/**** Update ****/
			// search document where name="mkyong" and update it with new values
			//BasicDBObject query = new BasicDBObject();
			//query.put("name", "mkyong");

			//BasicDBObject newDocument = new BasicDBObject();
			//newDocument.put("name", "mkyong-updated");

			//BasicDBObject updateObj = new BasicDBObject();
			//updateObj.put("$set", newDocument);

			//table.update(query, updateObj);

			/**** Find and display ****/
			//BasicDBObject searchQuery2
			//	= new BasicDBObject().append("name", "mkyong-updated");

			//DBCursor cursor2 = table.find(searchQuery2);

			//while (cursor2.hasNext()) {
			//	System.out.println(cursor2.next());
			//}

			/**** Done ****/
			long endTime = System.nanoTime();
			long totalTime = endTime-startTime;
			System.out.println("TOTAL TIME:" +  totalTime);

			System.out.println("Done");

		} catch (UnknownHostException e) {
			e.printStackTrace();
		} catch (MongoException e) {
			e.printStackTrace();
		}

	}
}

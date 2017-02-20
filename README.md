
# Stockafolio
Insight Data Engineering Fellowship, New York City
### Your Portfolio at a glance!
> 
- Project Website: http://insightdata.karthikchaganti.com/
- Project Presentation: https://goo.gl/DJHBbe

### What is Stock-a-folio?
- A highly scalable, low-latent and always available stock portfolio managmeent application.
- It can handle 10 million users and a throughput of 20,000 trades per second from different users! Yet your portfolio is updated in the blink of an eye.
- The website hosting the application contains two dashboards, one for the Users and one for the Trading firm to look at the overall trading patterns of all the traders in a day and get some insights to serve them better. 
- Built using all distributed open-source technologies.

## The Data Pipeline
![Alt text](/Images/Data-Pipeline.png)

### Motivation
- Back in the early 2000s, the stock portfolio updation was very slow. But today, instantaneous updation is vital
as quick decisions make a faster and profiting trade. That is what I tried to replicate in this project.


### The Stack
 - Built on Amazon Webservices EC2


| Tecnology     | Purpose       |
| ------------- | ------------- |
| Python  | Data Generator  |
| Apache Kafka  | Ingestion  |
| Apache Spark  | Batch Processing Engine  |
| Apache Spark Streaming | Stream Processing Engine |
| Apache Cassandra  | Data Storage  |
| Python Flask  | Server-side Web App  |
| Hadoop HDFS | Batch File System  |

### Data Schema
- Data is engineered using original S&P 500 stocks and then gaussian distribution is applied to it to simulate change in every second. The script is written in python.
- In order to simulate high scalability, a total of 10 million users are generated who keep trading on 1-500+ of these stocks randomly.
![Alt text](/Images/Trades.png)

- The throughput is set around 20,000 trades/sec i.e. those many messages are generated by the script every second and pushed into both Kafka and S3. 

### Stream Pipeline
- Kafka serves as the beginning of the pipeline which ingests the trades and then outputs them to the Spark Streaming engine. For higher throughput, 4 partitions are used.
- The Spark Stream engine collects the messages from Kafka in 1 second window batches and then processes them based on the queries selected to be displayed on the website.
- The processed data is stored on cassandra. Flask is python api that serves as server-end technology to fetch the queries and show them on the website. 
- Inorder to improve the latencies on the database end, SS Tables count was reduced by allocating more I/O bandwidth by increasing the nodes in the cluster. Memtables (JVM Heap) was increased in order to retain more data before writing to the disks to improve the reads and reduce the disk seeks.
- The latency of read/write from ingestion into Kafka and writing to database is calculated to be 0.27ms/0.015ms.

### Batch Pipeline
- The trades saved on the S3 are read into HDFS are processed by spark and pushed onto Cassandra. The batch serves as source for the Firm Dashboard which updates once in a day at 4 PM. 
- Batch can also be served as a fault-tolerant system to the stream pipeline.

### Website
- The website displays two dashboards, one for the user and the other for the trading firm. The following are displayed:
![Alt text](/Images/user.png)
![Alt text](/Images/firm.png)







[![Analytics](https://ga-beacon.appspot.com/UA-92170532-1/https://github.com/karthikchaganti/Stockafolio-Insight-Project)](https://github.com/igrigorik/ga-beacon)

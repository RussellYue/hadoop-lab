# Hadoop HDP Mapreduce tutorial

## exercise 1
- Create a folder called `/user/hadoop` in `hdfs` file system 
```bash
$ hdfs dfs -mkdir /user/hadoop/
```

- put files to `hdfs`
```bash
$ hdfs dfs -put pg20417.txt purchases.txt /user/hadoop/
```

- run mapreduce
  - you need to specify where the file is on the sandbox- hdp using the -files option
  
- exercise 1
```bash
$ hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -files mapper1.py,reducer1.py  -mapper "mapper1.py"  -reducer "reducer1.py" -input /user/hadoop/pg20417.txt -output e_1_output
```

- exercise 2
```bash
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -files mapper_q_a.py,reducer_q_a.py  -mapper "mapper_q_a.py"  -reducer "reducer_q_a.py" -input /user/hadoop/purchases.txt -output q_a_ouput
```

- question a 
```bash
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -files mapper_q_a.py,reducer_q_a.py  -mapper "mapper_q_a.py"  -reducer "reducer_q_a.py" -input /user/hadoop/purchases.txt -output q_a_ouput
```
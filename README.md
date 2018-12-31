# Hadoop HDP Mapreduce tutorial

## Steps
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
  
```bash
$ hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -files mapper1.py,reducer1.py  -mapper "mapper1.py"  -reducer "reducer1.py" -input /user/hadoop/pg20417.txt -output e_1_output
```

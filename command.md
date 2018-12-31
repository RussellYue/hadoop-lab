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

- question b

```bash
tail purchases.txt | ./mapper_q_b.py | sort | ./reducer_q_b.py
```

```
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -files mapper_q_b.py,reducer_q_b.py  -mapper "mapper_q_b.py"  -reducer "reducer_q_b.py" -input /user/hadoop/purchases.txt -output q_b_ouput
```

- question c

```
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -files mapper_q_c.py,reducer_q_c.py  -mapper "mapper_q_c.py"  -reducer "reducer_q_c.py" -input /user/hadoop/purchases.txt -output q_c_output
```
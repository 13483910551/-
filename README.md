# spark 和 mapreduce有哪些区别，请用具体的例子说明？
MapReduce的缺陷
操作复杂
开发起来：因为MapReduce只有map、reduce两种算子。
1. low-level 低级别的。
2. constrained	有很多限制 （虽然可以使用一些类似Hive之类的框架来弥补）
并且单元测试也很麻烦计算效率低
MapReduce是属于进程级别:MapTask ReduceTask虽然有JVM复用，但还是效率不高
频繁的IO: 因为MapReduce的作业一般都是串起来的作业，chain，一个作业的输出作为下一个作业的输入…并且作业的数据一般都会存储在HDFS上，这样会有频繁的磁盘和网络的IO。数据落地的话，是需要三个副本的。
MapReduce的所有任务都需要序列化
排序：MapReduce每个场景都需要排序的，但是很多时候都是没有必要的
面试题：key类型是实现什么接口？
writable 要执行序列化的 read方法和wirte方法
writablecomparable 排序比较的
Memory:MapReduce基于内存做处理，但是是有限的
所以说MapReduce性能是很低的，迭代次数比较多的话，性能会不好
不适合迭代处理
数据挖掘，机器学习，图计算之类的，都需要很多迭代操作，所以不适合用 MapReduce 去做不适合实时流式处理，只能离线处理
很多框架都各自为战，浪费了很多资源，开发也慢，运维也不方便

Spark的特点

综述：Spark is a fast and general engine for large-scale data processing（数据处理）
fast + general engine
fast体现在：
write code fast :Java/Scala/Python/R并支持interactive shell；
run fast : memory / DAG / Thread Model /sort可以设置成无。

计算速度快
memory	RDD cash
thread	基于线程
sort	可以设置的
pipeline（流水线）	rdd.map.fliter…collect
如果是MapReduce，maptask reducetask 遇到就执行，是立刻执行的
而 spark 是将很多操作串起来，就是一张DAG图（有向无环图）
rdd.map.fliter…这些操作再多是不会执行的，需要触发action操作才可以来执行。
例如：rdd.map.fliter…collect
遇见就执行，先执行map，读取写入操作完了，执行fliter，读取写入…
而对于Spark来说，是基于rdd来计算的
rdd里有分区，每一个操作都是载依赖，有action了，直接在这个分区（partition）中kaka就执行，就减少很多中间数据落地的操作（写入读取）
易于使用
使用Java，Scala，Python，R开发代码块+测试块
80+ high-level operator：80多种高级别的算子
nteractively 交互式命令行（测试快）
通用性
一站式处理（但是也不是万能的，只能解决一定场景的）


# rdd 是弹性分布式数据集（Resilient Distributed Dataset）的简称，是分布式内存的一个抽象概念，提供了一种高度受限的共享内存模型；
一、RDD是什么？
RDD是一个逻辑概念，一个RDD中有多个分区，一个分区在Executor节点上执行时，他就是一个迭代器。
一个RDD有多个分区，一个分区肯定在一台机器上，但是一台机器可以有多个分区，我们要操作的是分布在多台机器上的数据，而RDD相当于是一个代理，对RDD进行操作其实就是对分区进行操作，就是对每一台机器上的迭代器进行操作，因为迭代器引用着我们要操作的数据！

二、RDD的五大特性
1.RDD是由多个分区组成的集合
2.每个分区上会有一个函数作用在上面，实现分区的转换
3.RDD与RDD之间存在依赖关系，实现高容错性
4.如果RDD里面装的是（K-V）类型的，有分区器
5.如果从HDFS这种文件系统中创建RDD，会有最佳位置，是为了数据本地化


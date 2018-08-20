### candytray 生产者消费者模型之糖果生产
模拟一个简化的糖果机。这个特制的机器只有5 个可用的槽来
保持库存（糖果）。如果所有的槽都满了，糖果就不能再加到这个机器中了；相似地，如果每
个槽都空了，想要购买的消费者就无法买到糖果了。我们可以使用信号量来跟踪这些有限的
资源（糖果槽）。

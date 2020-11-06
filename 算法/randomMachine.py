class randomMachine(object):
    import random as rd

    def setWeight(self, weight):
        # 字典结构（k,v），数据为： {"一等奖": 1, "二等奖": 1, "三等奖": 1, "安慰奖": 6}
        self.weight = weight

        WEIGHT = {}

        weightLength = len(self.weight)  # 权重个数   4

        valueCount = 0  # 权重合计

        for v in self.weight.values():        #   1,1,1,6
            valueCount += v                   #  valueCount = 9
        # 析构，如：   k="一等奖" , v=1  ---->  "一等奖": 1,
        for k, v in self.weight.items():
            WEIGHT[k] = 1000000 * v / valueCount  # 一百万乘以权重所占百分比
            print("weight.items()  k:%s,v:%s" % (k, v))

        # 构建一个字典，设置初始为： "FIRST_PART": 0
        self.compare = {"FIRST_PART": 0}

        tmp = 0

        for k, v in WEIGHT.items():
            tmp += v
            print("WEIGHT.items() k:%s,v:%s" % (k,v))
            self.compare[k] = tmp

    def drawing(self):

        r = self.rd.randrange(1, 1000001)  # 随机数

        # print("随机数 : ", r)

        tmp = 0         # v暂存值  权重

        name = ''

        for k, v in self.compare.items():

            #print('k : ', k, "v :", v)    #先判断随机数是否小于等于范围
            if r <= v:

                if tmp == 0:  # 第一次判断

                    tmp = v

                    name = k

                if v < tmp:
                    tmp = v

                    name = k

        print(name)

        self.weight[k] -= 1  # 每次执行少一次奖励

    def graphicsUI(self):

        pass

    def start(self):

        pass


if __name__ == "__main__":

    # 实例化抽奖对象
    test = randomMachine()

    # 调抽奖对象test的setWeight()方法
    test.setWeight({"一等奖": 1, "二等奖": 1, "三等奖": 1, "安慰奖": 6})

    for i in range(9):
        # 调抽奖对象test的drawing()方法
        test.drawing()
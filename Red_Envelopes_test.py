
'''
计算微信红包的运气王概率
'''



import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   #显示中文
plt.rcParams['axes.unicode_minus']=False       #显示负号

def get_Fortune_King_Probability(n,m,k):
    '''

    :param n: 红包分成 n 个小红包
    :param m: 大红包中的总额
    :param k: 发 k 个大红包
    :return:  每个小红包能开出运气王的概率
    '''

    rets = np.zeros(n+1)
    # print("重复",k,"次")
    for k_index in range(0,k):
        max_index = 0 # 运气王是的索引
        max_value = 0 # 运气王的数值
        surplus_value = m
        surplus_index = n
        # print("抢红包....")
        for index_n in range(1,n+1):

            if surplus_index > 1:
                # 大于一个红包才会拆分
                t = np.random.uniform(0.01, 2*surplus_value/surplus_index)
            else:
                t = surplus_value
            if t > max_value:
                max_index = index_n
                max_value = t
            surplus_value = surplus_value - t
            surplus_index = surplus_index - 1

        rets[max_index] += 1

    return rets/k


if __name__ == '__main__':
    n = 20
    m = 100
    k = 10000
    y = get_Fortune_King_Probability(n=n, m=m, k=k)
    x = np.arange(len(y))

    plt.figure()
    plt.title(str(n)+" 个人参与微信抢红包，重复 "+str(k)+" 次运气王统计图")
    plt.bar(x[1:len(x)],y[1:len(y)],width=0.5)
    plt.ylabel("运气王的概率")
    plt.xlabel("红包被抢的顺序")
    plt.show()

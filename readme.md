# 代码文件说明

包括文件名称、功能、输入的参数及格式、输出文件名称及格式

## greedy-knapsack.cpp
- 功能：贪心算法求解0/1背包问题，按价值/重量比排序后依次选取
- 输入的参数及格式：命令行参数为数据文件路径，文件格式为第一行物品数量n，接下来n行每行为"编号 价值 重量"，最后一行背包容量
- 输出文件名称及格式：控制台输出，包括总价值、总重量、运行时间

## dp-knapsack.cpp
- 功能：动态规划算法（一维优化）求解0/1背包问题
- 输入的参数及格式：同上
- 输出文件名称及格式：控制台输出，包括最优价值、运行时间

## backtrack-knapsack.cpp
- 功能：回溯法（带剪枝）求解0/1背包问题
- 输入的参数及格式：同上
- 输出文件名称及格式：控制台输出，包括最优价值、运行时间

# 数据文件说明

包括文件名称、来源、格式及主要规模参数

## knapsack-github-01.in
- 来源：https://github.com/JorikJooken/knapsackProblemInstances
- 格式：第一行n=400，接下来400行每行"物品编号 价值 重量"，最后一行容量=1,000,000
- 主要规模参数：物品数量400，背包容量1,000,000

## knapsack-github-02.in
- 来源：同上
- 格式：第一行n=800，接下来800行每行"物品编号 价值 重量"，最后一行容量=1,000,000
- 主要规模参数：物品数量800，背包容量1,000,000

## knapsack-github-03.in
- 来源：同上
- 格式：第一行n=1000，接下来1000行每行"物品编号 价值 重量"，最后一行容量=1,000,000
- 主要规模参数：物品数量1000，背包容量1,000,000

## knapsack-github-04.in
- 来源：同上
- 格式：第一行n=400，接下来400行每行"物品编号 价值 重量"，最后一行容量=1,000,000
- 主要规模参数：物品数量400，背包容量1,000,000

## knapsack-github-05.in
- 来源：同上
- 格式：第一行n=400，接下来400行每行"物品编号 价值 重量"，最后一行容量=100,000,000
- 主要规模参数：物品数量400，背包容量100,000,000

## knapsack-github-06.in
- 来源：同上
- 格式：第一行n=400，接下来400行每行"物品编号 价值 重量"，最后一行容量=10,000,000,000
- 主要规模参数：物品数量400，背包容量10,000,000,000

# 结果文件说明

包括输出的文件名称、使用的应用程序名称、调用的函数名称、参数设置及文件格式等

## 结果文件命名格式

所有结果文件均按以下格式命名：
`{算法}-knapsack-github-{序号}-n_{物品数量}-c_{容量}.txt`

示例：`greedy-knapsack-github-06-n_400-c_10000000000.txt`
- 算法：greedy
- 数据源：knapsack-github
- 序号：06
- 物品数量 n：400
- 容量 c：10,000,000,000

## 结果文件通用说明

- 使用的应用程序名称：对应算法的cpp文件（greedy-knapsack.cpp / dp-knapsack.cpp / backtrack-knapsack.cpp）
- 调用的函数名称：main（回溯算法额外调用 backtrack, bound）
- 参数设置：数据集为对应的 knapsack-github-XX.in，物品数量n和容量c见文件名
- 文件格式：文本文件，记录算法运行结果，包括最优价值/总价值、运行时间

## 所有结果文件列表

| 文件名 | 算法 | 数据集 | n | 容量 |
|--------|------|--------|---|------|
| greedy-knapsack-github-01-n_400-c_1000000.txt | greedy | github-01 | 400 | 1,000,000 |
| greedy-knapsack-github-02-n_800-c_1000000.txt | greedy | github-02 | 800 | 1,000,000 |
| greedy-knapsack-github-03-n_1000-c_1000000.txt | greedy | github-03 | 1000 | 1,000,000 |
| greedy-knapsack-github-04-n_400-c_1000000.txt | greedy | github-04 | 400 | 1,000,000 |
| greedy-knapsack-github-05-n_400-c_100000000.txt | greedy | github-05 | 400 | 100,000,000 |
| greedy-knapsack-github-06-n_400-c_10000000000.txt | greedy | github-06 | 400 | 10,000,000,000 |
| dp-knapsack-github-01-n_400-c_1000000.txt | dp | github-01 | 400 | 1,000,000 |
| dp-knapsack-github-02-n_800-c_1000000.txt | dp | github-02 | 800 | 1,000,000 |
| dp-knapsack-github-03-n_1000-c_1000000.txt | dp | github-03 | 1000 | 1,000,000 |
| dp-knapsack-github-04-n_400-c_1000000.txt | dp | github-04 | 400 | 1,000,000 |
| dp-knapsack-github-05-n_400-c_100000000.txt | dp | github-05 | 400 | 100,000,000 |
| dp-knapsack-github-06-n_400-c_10000000000.txt | dp | github-06 | 400 | 10,000,000,000 |
| backtrack-knapsack-github-01-n_400-c_1000000.txt | backtrack | github-01 | 400 | 1,000,000 |
| backtrack-knapsack-github-02-n_800-c_1000000.txt | backtrack | github-02 | 800 | 1,000,000 |
| backtrack-knapsack-github-03-n_1000-c_1000000.txt | backtrack | github-03 | 1000 | 1,000,000 |
| backtrack-knapsack-github-04-n_400-c_1000000.txt | backtrack | github-04 | 400 | 1,000,000 |
| backtrack-knapsack-github-05-n_400-c_100000000.txt | backtrack | github-05 | 400 | 100,000,000 |
| backtrack-knapsack-github-06-n_400-c_10000000000.txt | backtrack | github-06 | 400 | 10,000,000,000 |

## 汇总结果文件

### exp1_fixed_capacity.csv
- 使用的应用程序名称：greedy-knapsack.cpp, dp-knapsack.cpp, backtrack-knapsack.cpp
- 调用的函数名称：main; main; main, backtrack, bound
- 参数设置：固定容量1000000，物品数量分别为400、800、1000
- 文件格式：CSV，实验1汇总数据

### exp2_fixed_n.csv
- 使用的应用程序名称：greedy-knapsack.cpp, dp-knapsack.cpp, backtrack-knapsack.cpp
- 调用的函数名称：main; main; main, backtrack, bound
- 参数设置：固定物品数量400，容量分别为1000000、100000000、10000000000
- 文件格式：CSV，实验2汇总数据

### summary_all_results.csv
- 使用的应用程序名称：greedy-knapsack.cpp, dp-knapsack.cpp, backtrack-knapsack.cpp
- 调用的函数名称：main; main; main, backtrack, bound
- 参数设置：所有6个数据集
- 文件格式：CSV，全部实验结果汇总

## 实验图表

### fig1_time_vs_n.png
- 使用的应用程序名称：plot_results.py
- 调用的函数名称：matplotlib.pyplot
- 参数设置：固定容量1000000，横轴为物品数量n，纵轴为运行时间(ms)，对数坐标
- 文件格式：PNG图片，图1：运行时间 vs 物品数量

### fig2_time_vs_capacity.png
- 使用的应用程序名称：plot_results.py
- 调用的函数名称：matplotlib.pyplot
- 参数设置：固定物品数量400，横轴为容量(对数坐标)，纵轴为运行时间(ms)
- 文件格式：PNG图片，图2：运行时间 vs 容量

### fig3_greedy_accuracy.png
- 使用的应用程序名称：plot_results.py
- 调用的函数名称：matplotlib.pyplot
- 参数设置：贪心解与最优解的价值差值
- 文件格式：PNG图片，图3：贪心算法最优性差距

### fig4_heatmap.png
- 使用的应用程序名称：plot_results.py
- 调用的函数名称：matplotlib.pyplot
- 参数设置：所有算法性能热力图，统一归一化尺度
- 文件格式：PNG图片，图4：算法性能热力图

# 辅助脚本说明

包括文件名称、功能、输入的参数及格式、输出文件名称及格式

## plot_results.py
- 位置：tools/ 目录下
- 功能：读取 experiments/ 目录下的 CSV 文件，生成四张实验分析图
- 输入的参数及格式：无命令行参数，直接运行即可
- 输出文件名称及格式：
  - ../experiments/fig1_time_vs_n.png（PNG图片，运行时间 vs 物品数量）
  - ../experiments/fig2_time_vs_capacity.png（PNG图片，运行时间 vs 容量）
  - ../experiments/fig3_greedy_accuracy.png（PNG图片，贪心算法最优性差距）
  - ../experiments/fig4_heatmap.png（PNG图片，算法性能热力图）
- 依赖：Python 3，需要安装 pandas, matplotlib, numpy
- 运行方式：进入 tool/ 目录后执行 `python plot_results.py`
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
exp1 = pd.read_csv('../experiments/exp1_fixed_capacity.csv')
exp2 = pd.read_csv('../experiments/exp2_fixed_n.csv')
summary = pd.read_csv('../experiments/summary_all_results.csv')

# 对于极小的greedy时间，保留4位小数
exp1['avg_ms'] = exp1['avg_ms'].apply(lambda x: round(x, 4) if isinstance(x, (int, float)) else x)
exp2['avg_ms'] = exp2['avg_ms'].apply(lambda x: round(x, 4) if isinstance(x, (int, float)) else x)

# ============================================
# 图1：运行时间 vs 物品数量（统一单位ms）
# ============================================
fig1, ax1 = plt.subplots(figsize=(11, 7))

algorithms = ['greedy', 'dp', 'backtrack']
colors = {'greedy': 'green', 'dp': 'blue', 'backtrack': 'red'}
markers = {'greedy': 'o', 'dp': 's', 'backtrack': '^'}

for algo in algorithms:
    data = exp1[exp1['algorithm'] == algo].copy()
    if len(data) > 0:
        data['avg_ms'] = pd.to_numeric(data['avg_ms'], errors='coerce')
        data = data.dropna(subset=['avg_ms'])
        if len(data) > 0:
            ax1.plot(data['n'], data['avg_ms'], 
                    marker=markers[algo], linewidth=2, markersize=8,
                    color=colors[algo], label=f"{algo.upper()}")
            for _, row in data.iterrows():
                value = row['avg_ms']
                if value < 0.001:
                    ax1.annotate(f'<0.001', xy=(row['n'], value),
                                xytext=(5, 5), textcoords='offset points',
                                fontsize=8, color=colors[algo])
                else:
                    ax1.annotate(f'{value:.3f}', xy=(row['n'], value),
                                xytext=(5, 5), textcoords='offset points',
                                fontsize=8, color=colors[algo])

ax1.set_xlabel('Number of Items (n)', fontsize=12)
ax1.set_ylabel('Running Time (ms)', fontsize=12)
ax1.set_title('Figure 1: Running Time vs Number of Items (Fixed Capacity = 1,000,000)', fontsize=12)
ax1.set_yscale('log')
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.legend(loc='upper left')
ax1.set_xlim(350, 1050)

plt.tight_layout()
plt.savefig('../experiments/fig1_time_vs_n.png', dpi=150)
plt.close()
print("Figure 1 saved")

# ============================================
# 图2：运行时间 vs 容量（10G的DP用虚线）
# ============================================
fig2, ax2 = plt.subplots(figsize=(11, 7))

# 贪心
greedy_data = exp2[exp2['algorithm'] == 'greedy'].copy()
greedy_data['avg_ms'] = pd.to_numeric(greedy_data['avg_ms'], errors='coerce')
greedy_data = greedy_data.dropna(subset=['avg_ms'])
ax2.plot(greedy_data['capacity'], greedy_data['avg_ms'], 
        marker='o', linewidth=2, markersize=8, color='green', label='GREEDY')
for _, row in greedy_data.iterrows():
    ax2.annotate(f'{row["avg_ms"]:.4f}', xy=(row['capacity'], row['avg_ms']),
                xytext=(5, 5), textcoords='offset points', fontsize=8, color='green')

# DP：10G用虚线表示
dp_data = exp2[exp2['algorithm'] == 'dp'].copy()
dp_data['avg_ms'] = pd.to_numeric(dp_data['avg_ms'], errors='coerce')
dp_valid = dp_data.dropna(subset=['avg_ms'])
dp_invalid = dp_data[dp_data['avg_ms'].isna()]

if len(dp_valid) > 0:
    # 有效数据：实线
    ax2.plot(dp_valid['capacity'], dp_valid['avg_ms'], 
            marker='s', linewidth=2, markersize=8, color='blue',
            label='DP', linestyle='-')
    for _, row in dp_valid.iterrows():
        ax2.annotate(f'{row["avg_ms"]:.0f}', xy=(row['capacity'], row['avg_ms']),
                    xytext=(5, 5), textcoords='offset points', fontsize=8, color='blue')

# 10G的DP：从最后一个有效点画虚线到10G位置
if len(dp_invalid) > 0 and len(dp_valid) > 0:
    last_valid = dp_valid.iloc[-1]
    # 虚线连接到10G位置，y值设为极大（表示时间极长）
    ax2.plot([last_valid['capacity'], 1e10], 
            [last_valid['avg_ms'], 1e6],  # 1e6 ms ≈ 16.7分钟
            color='blue', linestyle='--', linewidth=2, alpha=0.8)
    ax2.annotate('Extremely long /\nMemory overflow', 
                xy=(1e10, 1e6),
                xytext=(-30, 10), textcoords='offset points',
                fontsize=8, color='blue', ha='right')

# 回溯
backtrack_data = exp2[exp2['algorithm'] == 'backtrack'].copy()
backtrack_data['avg_ms'] = pd.to_numeric(backtrack_data['avg_ms'], errors='coerce')
backtrack_data = backtrack_data.dropna(subset=['avg_ms'])
ax2.plot(backtrack_data['capacity'], backtrack_data['avg_ms'], 
        marker='^', linewidth=2, markersize=8, color='red', label='BACKTRACK')
for _, row in backtrack_data.iterrows():
    ax2.annotate(f'{row["avg_ms"]:.0f}', xy=(row['capacity'], row['avg_ms']),
                xytext=(5, 5), textcoords='offset points', fontsize=8, color='red')

ax2.set_xlabel('Capacity', fontsize=12)
ax2.set_ylabel('Running Time (ms)', fontsize=12)
ax2.set_title('Figure 2: Running Time vs Capacity (Fixed n = 400)', fontsize=12)
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.legend(loc='upper left')

# 设置x轴刻度标签
ax2.set_xticks([1e6, 1e8, 1e10])
ax2.set_xticklabels(['1M', '100M', '10G'])

plt.tight_layout()
plt.savefig('../experiments/fig2_time_vs_capacity.png', dpi=150)
plt.close()
print("Figure 2 saved")

# ============================================
# 图3：差值图
# ============================================
fig3, ax3 = plt.subplots(figsize=(12, 5))

greedy_dict = {}
optimal_dict = {}

for _, row in summary[summary['algorithm'] == 'greedy'].iterrows():
    if row['value'] != 'N/A' and pd.notna(row['value']):
        try:
            greedy_dict[row['dataset']] = float(row['value'])
        except:
            pass

for _, row in summary[summary['algorithm'].isin(['dp', 'backtrack'])].iterrows():
    if row['value'] != 'N/A' and pd.notna(row['value']):
        try:
            if row['dataset'] not in optimal_dict:
                optimal_dict[row['dataset']] = float(row['value'])
        except:
            pass

common_ds = []
gaps = []
greedy_vals = []
optimal_vals = []

for ds in greedy_dict:
    if ds in optimal_dict:
        g = greedy_dict[ds]
        o = optimal_dict[ds]
        if not np.isnan(g) and not np.isnan(o):
            common_ds.append(ds)
            greedy_vals.append(g)
            optimal_vals.append(o)
            gaps.append(o - g)

x = np.arange(len(common_ds))
width = 0.6

colors_gap = ['red' if gap > 0 else 'green' for gap in gaps]
bars = ax3.bar(x, gaps, width, color=colors_gap, alpha=0.7, edgecolor='black')

ax3.set_xlabel('Dataset', fontsize=12)
ax3.set_ylabel('Gap (Optimal - Greedy)', fontsize=12)
ax3.set_title('Figure 3: Greedy Algorithm Optimality Gap', fontsize=12)
ax3.set_xticks(x)
ax3.set_xticklabels(common_ds)
ax3.axhline(y=0, color='black', linestyle='-', linewidth=1)
ax3.grid(True, alpha=0.3, axis='y')

for i, (gap, g, o) in enumerate(zip(gaps, greedy_vals, optimal_vals)):
    ax3.annotate(f'{int(gap)}', xy=(i, gap), xytext=(0, 5 if gap >= 0 else -15),
                textcoords='offset points', ha='center', fontsize=10, fontweight='bold')
    ax3.annotate(f'G:{int(g):,}', xy=(i, -max(gaps)/20 if max(gaps) > 0 else -0.5),
                ha='center', fontsize=8, color='green')
    ax3.annotate(f'O:{int(o):,}', xy=(i, -max(gaps)/10 if max(gaps) > 0 else -1),
                ha='center', fontsize=8, color='blue')

plt.tight_layout()
plt.savefig('../experiments/fig3_greedy_accuracy.png', dpi=150)
plt.close()
print("Figure 3 saved")

# ============================================
# 图4：热力图（统一尺度，NaN显示为灰色）
# ============================================
fig4, (ax4a, ax4b) = plt.subplots(1, 2, figsize=(14, 6))

import matplotlib.colors as mcolors
from matplotlib.cm import ScalarMappable

# 创建自定义colormap，将NaN显示为浅灰色
cmap = plt.cm.RdYlGn_r
cmap.set_bad(color='lightgray')

# 收集所有时间数据用于统一归一化
all_times = []
for df in [exp1, exp2]:
    times = pd.to_numeric(df['avg_ms'], errors='coerce').dropna()
    all_times.extend(times.tolist())
global_max = max(all_times) if all_times else 1
global_min = min([t for t in all_times if t > 0]) if all_times else 0.001

print(f"Global time range: {global_min:.4f} ms to {global_max:.0f} ms")

# 图4a：固定容量
pivot_n = exp1.pivot_table(index='n', columns='algorithm', values='avg_ms', aggfunc='first')
for col in pivot_n.columns:
    pivot_n[col] = pd.to_numeric(pivot_n[col], errors='coerce')

# 使用全局最大值归一化
pivot_n_norm = pivot_n / global_max

# 将NaN标记为无效（后续会被imshow显示为灰色）
pivot_n_norm = pivot_n_norm.astype(float)
pivot_n_norm_masked = np.ma.masked_invalid(pivot_n_norm.T.values)

im1 = ax4a.imshow(pivot_n_norm_masked, cmap=cmap, aspect='auto', 
                  vmin=0, vmax=1)
ax4a.set_xticks(range(len(pivot_n.index)))
ax4a.set_xticklabels(pivot_n.index)
ax4a.set_yticks(range(len(pivot_n.columns)))
ax4a.set_yticklabels([c.upper() for c in pivot_n.columns])
ax4a.set_xlabel('Number of Items (n)', fontsize=11)
ax4a.set_title('Figure 4a: Performance Heatmap\n(Fixed Capacity=1M, Green=Fast, Red=Slow)', fontsize=10)

for i in range(len(pivot_n.columns)):
    for j in range(len(pivot_n.index)):
        val = pivot_n.iloc[j, i]
        if not pd.isna(val):
            if val < 0.001:
                ax4a.text(j, i, '<0.001', ha='center', va='center', fontsize=7)
            else:
                ax4a.text(j, i, f'{val:.3f}', ha='center', va='center', fontsize=7)
        else:
            # 在NaN位置标注"N/A"
            ax4a.text(j, i, 'N/A', ha='center', va='center', fontsize=7, color='black')

cbar = plt.colorbar(im1, ax=ax4a)
cbar.set_label('Normalized Time (0=fast, 1=slow)', fontsize=9)

# 图4b：固定n
pivot_cap = exp2.pivot_table(index='capacity', columns='algorithm', values='avg_ms', aggfunc='first')
for col in pivot_cap.columns:
    pivot_cap[col] = pd.to_numeric(pivot_cap[col], errors='coerce')

# 使用全局最大值归一化
pivot_cap_norm = pivot_cap / global_max

# 过滤全NaN列和行
pivot_cap = pivot_cap.dropna(axis=1, how='all').dropna(axis=0, how='all')
pivot_cap_norm = pivot_cap_norm.loc[pivot_cap.index, pivot_cap.columns]
pivot_cap_norm_masked = np.ma.masked_invalid(pivot_cap_norm.T.values)

if len(pivot_cap) > 0 and len(pivot_cap.columns) > 0:
    im2 = ax4b.imshow(pivot_cap_norm_masked, cmap=cmap, aspect='auto',
                      vmin=0, vmax=1)
    ax4b.set_xticks(range(len(pivot_cap.index)))
    cap_labels = []
    for c in pivot_cap.index:
        if c >= 1e9:
            cap_labels.append(f'{int(c/1e9)}G')
        elif c >= 1e6:
            cap_labels.append(f'{int(c/1e6)}M')
        else:
            cap_labels.append(str(c))
    ax4b.set_xticklabels(cap_labels)
    ax4b.set_yticks(range(len(pivot_cap.columns)))
    ax4b.set_yticklabels([c.upper() for c in pivot_cap.columns])
    ax4b.set_xlabel('Capacity', fontsize=11)
    ax4b.set_title('Figure 4b: Performance Heatmap\n(Fixed n=400, Green=Fast, Red=Slow)', fontsize=10)
    
    for i in range(len(pivot_cap.columns)):
        for j in range(len(pivot_cap.index)):
            val = pivot_cap.iloc[j, i]
            if not pd.isna(val):
                if val < 0.001:
                    ax4b.text(j, i, '<0.001', ha='center', va='center', fontsize=7)
                elif val < 1:
                    ax4b.text(j, i, f'{val:.4f}', ha='center', va='center', fontsize=7)
                else:
                    ax4b.text(j, i, f'{val:.0f}', ha='center', va='center', fontsize=7)
            else:
                # 在NaN位置标注"N/A"
                ax4b.text(j, i, 'N/A', ha='center', va='center', fontsize=7, color='black')
    
    cbar2 = plt.colorbar(im2, ax=ax4b)
    cbar2.set_label('Normalized Time (0=fast, 1=slow)', fontsize=9)

plt.tight_layout()
plt.savefig('../experiments/fig4_heatmap.png', dpi=150)
plt.close()
print("Figure 4 saved")

print("\n" + "="*50)
print("All figures generated with unified scale!")
print("="*50)
print("Output files:")
print("  - fig1_time_vs_n.png")
print("  - fig2_time_vs_capacity.png (DP at 10G shown as dashed line)")
print("  - fig3_greedy_accuracy.png")
print("  - fig4_heatmap.png (unified color scale across all algorithms)")
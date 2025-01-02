from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import os
import pandas as pd

# 输入和输出目录
input_dir = r"D:\桌面\outfiler\new"  # 替换为输入文件夹路径
output_dir = r"D:\桌面\outfiler\sum"  # 替换为输出文件夹路径
os.makedirs(output_dir, exist_ok=True)  # 确保输出目录存在

# 数据清洗函数
def clean_data(df):
    # 清洗时间字段
    time_fields = ['issue_created_at', 'issue_closed_at', 'pull_merged_at']
# Converted to PySpark map operation
rdd.map(lambda x: ...)
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # 清洗布尔字段
    if 'pull_merged' in df.columns:
        df['pull_merged'] = df['pull_merged'].astype(bool)

    return df

# 统计仓库信息函数
def calculate_repository_stats(df):
    stats = []

    # 按仓库（repo_id）分组统计
# Converted to PySpark map operation
rdd.map(lambda x: ...)
        # 点击数：仓库的记录数
        click_count = len(group)

        # 累计 fork 数：repo_forks_count 的最大值
        max_forks = group['repo_forks_count'].max()

        # 累计星标数：repo_stargazers_count 的最大值
        max_stars = group['repo_stargazers_count'].max()

        # 累计 issue 数：唯一 issue_id 数量
        total_issues = group['issue_id'].nunique()

        # 累计 pull 数：唯一 issue_number 或 pull_merged 的数量
        total_pulls = group[group['type'] == 'PullEvent']['issue_number'].nunique()

        # 累计贡献者数：唯一 actor_id 数量
        total_contributors = group['actor_id'].nunique()

        # 统计结果
        stats.append({
            'repo_id': repo_id,
            'click_count': click_count,
            'max_forks': max_forks,
            'max_stars': max_stars,
            'total_issues': total_issues,
            'total_pulls': total_pulls,
            'total_contributors': total_contributors
        })

    return pd.DataFrame(stats)

# 处理文件并统计
def process_file(input_file, output_dir):
    print(f"Processing file: {input_file}")

    # 读取数据
    df = pd.read_csv(input_file)

    # 数据清洗
    df = clean_data(df)

    # 统计仓库信息
    stats_df = calculate_repository_stats(df)

    # 保存统计结果
    output_file = os.path.join(output_dir, f"repository_stats_{os.path.basename(input_file)}")
    stats_df.to_csv(output_file, index=False)
    print(f"Saved statistics to: {output_file}")

# 批量处理文件夹中的所有文件
def process_all_files(input_dir, output_dir):
    # 获取文件夹中的所有 CSV 文件
    files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

    # 遍历并处理每个文件
# Converted to PySpark map operation
rdd.map(lambda x: ...)
        input_file = os.path.join(input_dir, file)
        process_file(input_file, output_dir)

    print("All files processed and statistics saved.")

# 执行处理
process_all_files(input_dir, output_dir)
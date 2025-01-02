from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import os
import pandas as pd

# 输入和输出目录
input_dir = r'D:\桌面\outfiler\new'  # 替换为输入文件夹路径
output_dir = r'D:\桌面\outfiler\PULL'  # 替换为输出文件夹路径
os.makedirs(output_dir, exist_ok=True)  # 确保输出目录存在

def calculate_pr_stats(input_dir, output_dir, time_freq='2Q'):
    """
    按时间统计仓库中的新增 PR 和已合并 PR 数量，以及 PR 的处理效率和处理时间。
    """
# Converted to PySpark map operation
rdd.map(lambda x: ...)
        if file_name.endswith('.csv'):  # 仅处理 CSV 文件
            file_path = os.path.join(input_dir, file_name)
            print(f"Processing file: {file_path}")

            # 读取数据
            df = pd.read_csv(file_path)

            # 检查所需字段是否存在
            required_columns = {'repo_id', 'pull_merged', 'issue_created_at', 'pull_merged_at', 'type'}
            if required_columns.issubset(df.columns):
                # 筛选 type 为 PullEvent 的记录
                df = df[df['type'] == 'PullEvent']

                # 转换时间字段为日期时间类型
                df['issue_created_at'] = pd.to_datetime(df['issue_created_at'], errors='coerce')
                df['pull_merged_at'] = pd.to_datetime(df['pull_merged_at'], errors='coerce')

                # 创建结果存储列表
                results = []

                # 按仓库分组处理
# Converted to PySpark map operation
rdd.map(lambda x: ...)
                    # 1. 统计新增 PR 按时间分组
                    created_prs = (
                        group.dropna(subset=['issue_created_at'])  # 过滤无创建时间的记录
                        .groupby(pd.Grouper(key='issue_created_at', freq=time_freq))
                        .size()
                        .reset_index(name='pulls_created')
                    )
                    created_prs['repo_id'] = repo_id

                    # 2. 统计已合并 PR 按时间分组
                    merged_prs = (
                        group[group['pull_merged'] == True].dropna(subset=['pull_merged_at'])  # 筛选已合并的记录
                        .groupby(pd.Grouper(key='pull_merged_at', freq=time_freq))
                        .size()
                        .reset_index(name='pulls_merged')
                    )
                    merged_prs['repo_id'] = repo_id

                    # 3. 计算 PR 平均处理时间（已合并 PR 的合并时间减创建时间）
                    group['processing_time'] = (
                        (group['pull_merged_at'] - group['issue_created_at']).dt.total_seconds() / 3600  # 转为小时
                    )
                    avg_processing_time = (
                        group[group['pull_merged'] == True]
                        .groupby(pd.Grouper(key='pull_merged_at', freq=time_freq))
                        ['processing_time']
                        .mean()
                        .reset_index(name='avg_processing_time_hours')
                    )
                    avg_processing_time['repo_id'] = repo_id

                    # 合并三个结果表
                    combined = pd.merge(
                        created_prs.rename(columns={'issue_created_at': 'time'}),
                        merged_prs.rename(columns={'pull_merged_at': 'time'}),
                        on=['repo_id', 'time'],
                        how='outer'
                    )
                    combined = pd.merge(
                        combined,
                        avg_processing_time.rename(columns={'pull_merged_at': 'time'}),
                        on=['repo_id', 'time'],
                        how='outer'
                    ).fillna(0)

                    # 4. 计算处理效率（已合并 PR 占新增 PR 的百分比）
                    combined['processing_efficiency'] = (
                        combined['pulls_merged'] / combined['pulls_created']
                    ).fillna(0) * 100  # 转为百分比

                    results.append(combined)

                # 合并所有仓库结果
                if results:
                    final_df = pd.concat(results, ignore_index=True)

                    # 保存到输出文件夹
                    output_file = os.path.join(output_dir, f"pr_stats_{file_name}")
                    final_df.to_csv(output_file, index=False)
                    print(f"Saved results to: {output_file}")
                else:
                    print(f"No valid data for {file_name}.")
            else:
                print(f"Skipping file {file_name}: Required columns are missing.")

# 调用函数，按半年统计
calculate_pr_stats(input_dir, output_dir, time_freq='2Q')  # 按半年统计

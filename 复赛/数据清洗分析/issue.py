from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import os
import pandas as pd

# 输入和输出目录
input_dir = r'D:\桌面\outfiler\new'  # 替换为输入文件夹路径
output_dir = r'D:\桌面\outfiler\issue'  # 替换为输出文件夹路径
os.makedirs(output_dir, exist_ok=True)  # 确保输出目录存在

def process_issues_by_time(input_dir, output_dir, time_freq='2Q'):
    """
    按时间统计仓库中 issue 的新增和关闭数量，限定 type 为 IssueEvent。
    """
# Converted to PySpark map operation
rdd.map(lambda x: ...)
        if file_name.endswith('.csv'):  # 确保处理 CSV 文件
            file_path = os.path.join(input_dir, file_name)
            print(f"Processing file: {file_path}")

            # 读取数据
            df = pd.read_csv(file_path)

            # 确保所需字段存在
            required_columns = {'repo_id', 'issue_created_at', 'issue_closed_at', 'type'}
            if required_columns.issubset(df.columns):
                # 筛选 type 为 IssueEvent 的数据
                df = df[df['type'] == 'IssueEvent']

                # 转换时间字段为日期时间类型
                df['issue_created_at'] = pd.to_datetime(df['issue_created_at'], errors='coerce')
                df['issue_closed_at'] = pd.to_datetime(df['issue_closed_at'], errors='coerce')

                # 创建新的数据框，用于存储结果
                results = []

                # 按仓库分组处理
# Converted to PySpark map operation
rdd.map(lambda x: ...)
                    # 新增 issue 按时间统计
                    created_issues = (
                        group.dropna(subset=['issue_created_at'])  # 过滤无创建时间的记录
                        .groupby(pd.Grouper(key='issue_created_at', freq=time_freq))
                        .size()
                        .reset_index(name='issues_created')
                    )
                    created_issues['repo_id'] = repo_id
                    created_issues['event'] = 'created'

                    # 关闭 issue 按时间统计
                    closed_issues = (
                        group.dropna(subset=['issue_closed_at'])  # 过滤无关闭时间的记录
                        .groupby(pd.Grouper(key='issue_closed_at', freq=time_freq))
                        .size()
                        .reset_index(name='issues_closed')
                    )
                    closed_issues['repo_id'] = repo_id
                    closed_issues['event'] = 'closed'

                    # 合并新增和关闭统计
                    merged_stats = pd.merge(
                        created_issues.rename(columns={'issue_created_at': 'time'}),
                        closed_issues.rename(columns={'issue_closed_at': 'time'}),
                        on=['repo_id', 'time'],
                        how='outer'
                    ).fillna(0)

                    results.append(merged_stats)

                # 合并所有仓库结果
                if results:
                    final_df = pd.concat(results, ignore_index=True)

                    # 保存到输出文件夹
                    output_file = os.path.join(output_dir, f"issues_by_time_{file_name}")
                    final_df.to_csv(output_file, index=False)
                    print(f"Saved results to: {output_file}")
                else:
                    print(f"No valid data for {file_name}.")
            else:
                print(f"Skipping file {file_name}: Required columns are missing.")

# 调用函数，按半年统计
process_issues_by_time(input_dir, output_dir, time_freq='2Q')
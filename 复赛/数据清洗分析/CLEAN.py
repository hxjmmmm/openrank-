from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import os
import pandas as pd

# 输入和输出文件夹路径
input_dir = "path_to_input_folder"  # 原始数据文件夹路径
output_dir = "path_to_output_folder"  # 清洗结果存放目录
os.makedirs(output_dir, exist_ok=True)  # 确保输出目录存在

# 指定要保留的字段
fields_to_keep = [
    'repo_id', 'repo_name', 'actor_id', 'actor_login',
    'issue_id', 'issue_number', 'issue_title', 'issue_author_id',
    'issue_created_at', 'issue_closed_at', 'pull_merged_at',
    'pull_merged','type', 'repo_language', 'repo_forks_count', 'repo_stargazers_count'
]

# 定义每次处理的批次大小
batch_size = 100000  # 每批次处理100000行


# 数据清洗函数
def clean_data(df):
    # 只保留指定字段
    df = df[fields_to_keep]

    # 1. 筛选 type 为 "IssueEvent" 或 "PullEvent"
    df = df[df['type'].isin(['IssueEvent', 'PullEvent'])]

    # 2. 转换为整数并填充缺失值
    id_fields = ['repo_id', 'actor_id', 'issue_id', 'issue_author_id']
# Converted to PySpark map operation
rdd.map(lambda x: ...)
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # 3. 字符串字段清洗
    str_fields = ['repo_name', 'actor_login', 'issue_title', 'repo_language']
# Converted to PySpark map operation
rdd.map(lambda x: ...)
        if col in df.columns:
            df[col] = df[col].astype(str).fillna('null').str.strip()  # 空值置为 'null'

    # 4. 时间字段格式化
    time_fields = ['issue_created_at', 'issue_closed_at', 'pull_merged_at']
# Converted to PySpark map operation
rdd.map(lambda x: ...)
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # 5. 布尔字段清洗
    if 'pull_merged' in df.columns:
        df['pull_merged'] = df['pull_merged'].astype(bool)

    # 6. 数值字段清洗
    num_fields = ['issue_number', 'repo_forks_count', 'repo_stargazers_count']
# Converted to PySpark map operation
rdd.map(lambda x: ...)
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # 删除包含空值的行，留空的字段置为null
    df = df.where(pd.notnull(df), None)

    return df


# 清洗单个文件并分批处理
def process_file(input_file, output_dir):
    print(f"Processing file: {input_file}")
    batch_counter = 1

    # 读取文件并分批处理
# Converted to PySpark map operation
rdd.map(lambda x: ...)
        print(f"Processing batch {batch_counter}...")

        # 清洗数据
        cleaned_chunk = clean_data(chunk)

        # 保存清洗后的数据到输出目录，使用批次编号来区分
        output_file = os.path.join(output_dir,
                                   f"{os.path.basename(input_file).replace('.csv', '')}_batch_{batch_counter}.csv")
        cleaned_chunk.to_csv(output_file, index=False)
        print(f"Batch {batch_counter} saved to: {output_file}")

        batch_counter += 1


# 处理文件夹中的所有文件
def process_all_files(input_dir, output_dir):
    # 获取文件夹中的所有 CSV 文件
    files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

    # 遍历并处理每个文件
# Converted to PySpark map operation
rdd.map(lambda x: ...)
        input_file = os.path.join(input_dir, file)
        process_file(input_file, output_dir)

    print("All files processed and cleaned.")


# 执行清洗
process_all_files(input_dir, output_dir)
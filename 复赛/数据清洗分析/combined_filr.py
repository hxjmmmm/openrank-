from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import pandas as pd
import os

# 定义文件夹路径
file1_folder = r"D:\桌面\xxxx"  # 替换为文件夹路径
file2_path = r"D:\桌面\modified_data.csv"  # 第二个文件路径

# 定义处理大型文件时只读取必要的列
cols_file1 = ['repo_id', 'repo_name', 'actor_id', 'actor_login', 'issue_id', 'issue_title']
cols_file2 = ['id', 'name', 'value', 'category']

# 读取 file2 数据并创建索引
try:
    file2 = pd.read_csv(file2_path, usecols=cols_file2, encoding='utf-8')
except UnicodeDecodeError:
    file2 = pd.read_csv(file2_path, usecols=cols_file2, encoding='latin1')

# 创建索引字典以加速查找
category_1_2 = file2[file2['category'].isin([1, 2])].set_index(['name', 'value'])
category_3 = file2[file2['category'] == 3].set_index(['name', 'value'])

# 初始化新表的数据列表和主键 id
record_id = 1  # 用于生成主键 id

# 遍历文件夹中的每个 CSV 文件
# Converted to PySpark map operation
rdd.map(lambda x: ...)
    file1_path = os.path.join(file1_folder, file_name)
    if not file_name.endswith('.csv'):
        continue  # 跳过非 CSV 文件

    # 初始化当前仓库的新数据列表
    new_data = []

    # 逐块加载第一个文件
    try:
        chunks = pd.read_csv(file1_path, usecols=cols_file1, chunksize=5000, encoding='utf-8')
    except UnicodeDecodeError:
        chunks = pd.read_csv(file1_path, usecols=cols_file1, chunksize=5000, encoding='latin1')

# Converted to PySpark map operation
rdd.map(lambda x: ...)
        # **第一种情况：处理问题（category 为 1 或 2）**
        merged_1_2 = chunk.merge(
            category_1_2.reset_index(),
            left_on=['issue_title', 'issue_id'],
            right_on=['name', 'value'],
            how='inner'
        )
        if not merged_1_2.empty:
            merged_1_2 = merged_1_2.merge(
                file2[['id', 'name', 'value']],
                left_on=['repo_id', 'repo_name'],
                right_on=['value', 'name'],
                how='inner',
                suffixes=('', '_source')
            )
# Converted to PySpark map operation
rdd.map(lambda x: ...)
                new_data.append({
                    'id': record_id,
                    'repo_name': row['repo_name'],
                    'source': row['id_source'],
                    'target': row['id']
                })
                record_id += 1

        # **第二种情况：处理用户（category 为 3）**
        merged_3 = chunk.merge(
            category_3.reset_index(),
            left_on=['actor_login', 'actor_id'],
            right_on=['name', 'value'],
            how='inner'
        )
        if not merged_3.empty:
            merged_3 = merged_3.merge(
                file2[['id', 'name', 'value']],
                left_on=['issue_id', 'issue_title'],
                right_on=['value', 'name'],
                how='inner',
                suffixes=('', '_source')
            )
# Converted to PySpark map operation
rdd.map(lambda x: ...)
                new_data.append({
                    'id': record_id,
                    'repo_name': row['repo_name'],
                    'source': row['id_source'],
                    'target': row['id']
                })
                record_id += 1

    # 输出当前仓库的匹配结果
    if new_data:
        output_file = f"new_table_{file_name.replace('.csv', '')}.csv"
        output_path = os.path.join(file1_folder, output_file)
        pd.DataFrame(new_data).to_csv(output_path, index=False)
        print(f"匹配结果已保存: {output_path}")
    else:
        print(f"仓库 {file_name} 无匹配结果")
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import os
import pandas as pd
import numpy as np

# 输入和输出文件夹路径
input_dir = r"D:\桌面\end_data1\end_data1"  # 清洗后的文件夹路径
output_dir = r"D:\桌面\outfiler\pull"  # 修改后的结果存放目录
os.makedirs(output_dir, exist_ok=True)  # 确保输出目录存在

def randomize_type_field(input_dir, output_dir):
    """
    随机修改 type 字段的值为 issuevent 和 pullevent。
    """
    # 获取所有清洗后的 CSV 文件
    files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

# Converted to PySpark map operation
rdd.map(lambda x: ...)
        input_file = os.path.join(input_dir, file)
        print(f"Processing file: {input_file}")

        # 读取数据
        df = pd.read_csv(input_file)

        # 检查 type 字段是否存在
        if 'type' in df.columns:
            # 随机分配 type 字段的值为 issuevent 或 pullevent
            df['type'] = np.random.choice(['IssueEvent', 'PullEvent'], size=len(df))

            # 保存修改后的文件到输出目录
            output_file = os.path.join(output_dir, file)
            df.to_csv(output_file, index=False)
            print(f"Saved modified file to: {output_file}")
        else:
            print(f"Skipping file {file}: 'type' column not found.")

# 执行修改
randomize_type_field(input_dir, output_dir)
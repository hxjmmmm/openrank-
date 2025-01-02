from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import os
import pandas as pd

# 配置文件夹路径
input_folder = r"D:\桌面\outfiler\new"  # 替换为您的文件夹路径
output_folder = r"D:\桌面\outfiler\repo+pull"  # 替换为保存结果的文件夹路径

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 遍历文件夹中的所有 CSV 文件
# Converted to PySpark map operation
rdd.map(lambda x: ...)
    if file_name.endswith('.csv'):
        file_path = os.path.join(input_folder, file_name)

        try:
            # 读取 CSV 文件
            df = pd.read_csv(file_path)

            # 清洗 `PullEvent` 类型的数据
            pull_df = df[df['type'] == 'PullEvent'][
                ['repo_id', 'repo_name', 'actor_id', 'actor_login', 'issue_id', 'issue_title']]

            # 重命名字段
            pull_df = pull_df.rename(columns={'issue_id': 'pull_id', 'issue_title': 'pull_title'})

            # 保存清洗后的文件
            output_file_path = os.path.join(output_folder, f"cleaned_pulltype_{file_name}")
            pull_df.to_csv(output_file_path, index=False)
            print(f"Processed and saved PullEvent: {output_file_path}")

        except Exception as e:
            print(f"Error processing {file_name}: {e}")

print("PullEvent data cleaning completed.")
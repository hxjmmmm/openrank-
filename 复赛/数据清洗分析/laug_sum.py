from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import pandas as pd

# 读取 CSV 文件
input_path = "combined_file.csv"  # 替换为你的文件路径
output_path = "your_output_file.csv"  # 替换为保存的文件路径

# 加载数据
df = pd.read_csv(input_path)

# 合并重复项，按 repo_id 和 language_name 分组，汇总 language_percentage
df_merged = df.groupby(["repo_id", "language_name"], as_index=False).agg({"language_percentage": "sum"})

# 在每个 repo_id 内计算 language_percentage 的占比
df_merged["language_percentage"] = df_merged.groupby("repo_id")["language_percentage"].transform(lambda x: 100 * x / x.sum())

# 保存结果到新的 CSV 文件
df_merged.to_csv(output_path, index=False)

print(f"处理后的数据已保存到: {output_path}")
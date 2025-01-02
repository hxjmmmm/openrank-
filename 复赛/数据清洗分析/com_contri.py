from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import pandas as pd

# 读取 CSV 文件
input_path = "D:\pythonProject\openrank\combined_file.csv"  # 替换为你的文件路径
output_path = "your_output_file.csv"  # 替换为保存的文件路径

# 加载数据
df = pd.read_csv(input_path)

# 合并重复项，按 repo_id, actor_id, actor_login 分组，汇总 activity_count
df_merged = df.groupby(["repo_id", "actor_id", "actor_login"], as_index=False).agg({"activity_count": "sum"})

# 在每个 repo_id 内部，根据 activity_count 降序排序并设置 rank
df_merged["rank"] = df_merged.groupby("repo_id")["activity_count"].rank(ascending=False, method="min").astype(int)

# 保存结果到新的 CSV 文件
df_merged.to_csv(output_path, index=False)

print(f"处理后的数据已保存到: {output_path}")
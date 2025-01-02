from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import pandas as pd

# 读取 CSV 文件
input_path = "combined_file.csv"  # 替换为你的文件路径
output_path = "your_output_file.csv"  # 替换为保存的文件路径

# 加载数据
df = pd.read_csv(input_path)

# 合并重复项，按 time 和 repo_id 分组，汇总 pulls_created 和 pulls_merged
df_merged = df.groupby(["time", "repo_id"], as_index=False).agg({
    "pulls_created": "sum",
    "pulls_merged": "sum"
})

# 计算 processing_efficiency
df_merged["processing_efficiency"] = (df_merged["pulls_merged"] / df_merged["pulls_created"] * 100).fillna(0)

# 保存结果到新的 CSV 文件
df_merged.to_csv(output_path, index=False)

print(f"处理后的数据已保存到: {output_path}")
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import pandas as pd

# 配置文件路径
input_file = r"D:\pythonProject\openrank\combined_file.csv"  # 替换为您的数据文件路径
output_file = r"D:\桌面\outfiler\pull_file.csv"  # 替换为保存结果的路径

# 读取数据
df = pd.read_csv(input_file)

# 消除完全重复的行
df_cleaned = df.drop_duplicates()

# 保存结果
df_cleaned.to_csv(output_file, index=False)

print(f"去重完成，结果已保存到 {output_file}")
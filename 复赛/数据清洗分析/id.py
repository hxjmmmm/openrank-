from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import pandas as pd

# 读取原始 CSV 文件
input_file = r"D:\桌面\outfiler\xin\pull.csv"  # 替换为你的文件路径
output_file = "output_file.csv"  # 替换为输出文件路径

# 读取 CSV 文件
df = pd.read_csv(input_file)

# 添加主键列
df.insert(0, 'id', range(0, len(df)))

# 保存到新的 CSV 文件
df.to_csv(output_file, index=False)

print(f"已成功将主键列添加到 {output_file}")
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import pandas as pd
import numpy as np

# 加载 Excel 文件
data_file = r"D:\桌面\repo.xlsx"  # 替换为您的文件名
sheet_name = "Sheet1"  # 替换为您的工作表名
df = pd.read_excel(data_file, sheet_name=sheet_name)

# 统计 pull_id 出现次数
pull_counts = df["actor_id"].value_counts().reset_index()
pull_counts.columns = ["actor_id", "symbolsize"]

# 合并以获取 pull_title 和 symbolsize
df_cleaned = df.drop_duplicates(subset="actor_id").merge(pull_counts, on="actor_id")

# 添加 id，从 1 开始生成
df_cleaned["id"] = range(1, len(df_cleaned) + 1)

# 随机生成 x, y 坐标，范围为 -10 到 10
df_cleaned["x"] = np.random.uniform(-10, 10, len(df_cleaned))
df_cleaned["y"] = np.random.uniform(-10, 10, len(df_cleaned))

# 固定 category = 2
df_cleaned["category"] = 3

# 重命名字段
final_df = df_cleaned[["id", "actor_login", "symbolsize", "x", "y", "actor_id", "category"]]
final_df.columns = ["id", "name", "symbolsize", "x", "y", "value", "category"]

# 查看结果
print(final_df)

# 保存清洗后的数据到新的 Excel 文件
output_file = "cleaned_data.xlsx"  # 替换为您的输出文件名
final_df.to_excel(output_file, index=False)
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import pandas as pd

# 输入文件和输出文件路径
input_file = 'D:\pythonProject\openrank\combined_file.csv'  # 替换为您的输入文件路径
output_file = 'D:\pythonProject\openrank\path_to_your_output_file.csv'  # 替换为您的输出文件路径

# 读取 CSV 文件
df = pd.read_csv(input_file)

# 将时间字段转换为日期格式
df['time'] = pd.to_datetime(df['time'])

# 按 repo_id 和 time 合并数据
merged_df = df.groupby(['repo_id', 'time'], as_index=False).agg({
    'issues_created': 'sum',  # 合并时对 issues_created 列求和
    'issues_closed': 'sum',   # 合并时对 issues_closed 列求和
    'event_x': 'last',        # 保留分组内最后一个 event_x
    'event_y': 'last'         # 保留分组内最后一个 event_y
})

# 保存合并后的数据到新的 CSV 文件
merged_df.to_csv(output_file, index=False)

# 输出保存结果的消息
print(f"Results saved to: {output_file}")
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import pandas as pd
import os

# 输入和输出文件路径
input_file = "path_to_your_cleaned_data.csv"  # 第一遍清洗后的数据文件路径
output_file = "path_to_output.csv"  # 输出文件路径

# 加载数据
data = pd.read_csv(input_file)

# 检查type类型是否为PullRequestEvent
pull_request_mask = data['type'] == 'PullRequestEvent'

# 对符合条件的字段进行重命名
data.loc[pull_request_mask, 'pull_id'] = data.loc[pull_request_mask, 'issue_id']
data.loc[pull_request_mask, 'pull_number'] = data.loc[pull_request_mask, 'issue_number']
data.loc[pull_request_mask, 'pull_title'] = data.loc[pull_request_mask, 'issue_title']
data.loc[pull_request_mask, 'pull_author_id'] = data.loc[pull_request_mask, 'issue_author_id']
data.loc[pull_request_mask, 'pull_created_at'] = data.loc[pull_request_mask, 'issue_created_at']

# 删除旧字段以避免混淆（可选）
data.drop(columns=['issue_id', 'issue_number', 'issue_title', 'issue_author_id', 'issue_created_at'], inplace=True)

# 保存结果
data.to_csv(output_file, index=False)
print(f"Processed data saved to: {output_file}")




# 对于符合条件的记录，将字段 issue_id, issue_number, issue_title, issue_author_id,
# 和 issue_created_at 分别重命名为 pull_id, pull_number, pull_title, pull_author_id, 和 pull_created_at。
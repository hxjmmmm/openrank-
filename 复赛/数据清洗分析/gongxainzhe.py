from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import os
import pandas as pd










# repo_id: 仓库 ID
# actor_id: 贡献者 ID
# actor_login: 贡献者用户名
# type: 活动类型 ,PushEvent, PullRequestEvent, IssueCommentEvent 等




# 输入和输出文件夹路径
input_dir = r'D:\桌面\outfiler\new'  # 替换为你的输入文件夹路径
output_dir = r'D:\桌面\outfiler\contributer'  # 替换为你的输出文件夹路径
os.makedirs(output_dir, exist_ok=True)  # 确保输出文件夹存在

def calculate_contributor_rank(input_dir, output_dir):
    """
    计算仓库中的贡献者排名并保存到指定输出文件夹。
    """
# Converted to PySpark map operation
rdd.map(lambda x: ...)
        if file_name.endswith('.csv'):  # 确保处理的是 CSV 文件
            file_path = os.path.join(input_dir, file_name)
            print(f"Processing file: {file_path}")

            # 读取 CSV 文件
            df = pd.read_csv(file_path)

            # 确保必要的列存在
            if {'repo_id', 'actor_id', 'actor_login', 'type'}.issubset(df.columns):
                # 按仓库和贡献者分组，统计贡献活动数量
                contributor_stats = (
                    df.groupby(['repo_id', 'actor_id', 'actor_login'])
                    .size()  # 统计每个贡献者的活动次数
                    .reset_index(name='activity_count')
                )

                # 按仓库排序贡献者，按活动次数降序排列
                contributor_stats['rank'] = (
                    contributor_stats.groupby('repo_id')['activity_count']
                    .rank(ascending=False, method='dense')
                    .astype(int)
                )

                # 构造输出文件路径
                output_file = os.path.join(output_dir, f"contributor_rank_{file_name}")

                # 保存结果到输出文件夹
                contributor_stats.to_csv(output_file, index=False)
                print(f"Contributor rank saved to: {output_file}")
            else:
                print(f"Skipping file {file_name}: Required columns are missing.")

# 执行清洗过程
calculate_contributor_rank(input_dir, output_dir)
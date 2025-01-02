from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import pandas as pd
import os

# 设置文件夹路径
folder_path = "D:\桌面\outfiler\sum"  # 替换为你的文件夹路径
output_path = "merged_output.csv"  # 替换为保存的文件路径

# 获取文件夹中所有的 CSV 文件
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# 初始化一个空的 DataFrame 用于存储合并后的数据
all_data = pd.DataFrame()

# 循环读取每个 CSV 文件，并将其数据合并
# Converted to PySpark map operation
rdd.map(lambda x: ...)
    file_path = os.path.join(folder_path, file)
    try:
        # 读取文件，跳过空文件或没有有效数据的文件
        df = pd.read_csv(file_path)
        if df.empty:
            print(f"文件 {file} 为空，跳过处理。")
            continue
        all_data = pd.concat([all_data, df], ignore_index=True)
    except pd.errors.EmptyDataError:
        print(f"文件 {file} 为空或无效，跳过。")
    except Exception as e:
        print(f"处理文件 {file} 时发生错误: {e}")

# 检查合并后的数据是否为空
if all_data.empty:
    print("没有有效数据进行合并，请检查源文件。")
else:
    # 合并重复的 repo_id 并进行汇总
    df_merged = all_data.groupby("repo_id", as_index=False).agg({
        "click_count": "sum",            # click_count 相加
        "max_forks": "max",              # max_forks 保留最大值
        "max_stars": "max",              # max_stars 保留最大值
        "total_issues": "sum",           # total_issues 相加
        "total_pulls": "sum",            # total_pulls 相加
        "total_contributors": "sum"      # total_contributors 相加
    })

    # 保存合并后的结果到新的 CSV 文件
    df_merged.to_csv(output_path, index=False)
    print(f"所有 CSV 文件已合并并保存到: {output_path}")
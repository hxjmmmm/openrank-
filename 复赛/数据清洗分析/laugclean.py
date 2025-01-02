from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import os
import pandas as pd

# 输入和输出文件夹路径
input_dir = r'D:\桌面\outfiler\new'  # 替换为你的输入文件夹路径
output_dir = r'D:\桌面\outfiler\laug'  # 替换为你的输出文件夹路径
os.makedirs(output_dir, exist_ok=True)  # 确保输出文件夹存在

def clean_language_data(input_dir, output_dir):
    """
    清洗文件夹中所有 CSV 文件的语言占比数据并保存到指定输出文件夹。
    """
    # 遍历输入文件夹中的所有 CSV 文件
# Converted to PySpark map operation
rdd.map(lambda x: ...)
        if file_name.endswith('.csv'):  # 确保处理的是 CSV 文件
            file_path = os.path.join(input_dir, file_name)
            print(f"Processing file: {file_path}")

            # 读取 CSV 文件
            df = pd.read_csv(file_path)

            # 确保 'repo_language' 列存在且处理缺失值
            if 'repo_id' in df.columns and 'repo_language' in df.columns:
                df['repo_language'] = df['repo_language'].fillna('Unknown').astype(str).str.strip()

                # 按仓库分组并计算语言占比
                repo_language_percentage = (
                    df.groupby('repo_id')['repo_language']
                    .value_counts(normalize=True)  # 计算占比
                    .mul(100)  # 转换为百分比
                    .reset_index(name='language_percentage')  # 转换为 DataFrame 并命名占比列
                )

                # 重命名列以便更清晰
                repo_language_percentage.rename(columns={'repo_language': 'language_name'}, inplace=True)

                # 构造输出文件路径
                output_file = os.path.join(output_dir, f"cleaned_{file_name}")

                # 保存清洗后的结果到输出文件夹
                repo_language_percentage.to_csv(output_file, index=False)
                print(f"Cleaned data saved to: {output_file}")
            else:
                print(f"Skipping file {file_name}: Required columns are missing.")

# 执行清洗过程
clean_language_data(input_dir, output_dir)
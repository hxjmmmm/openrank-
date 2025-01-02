from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Conversion').getOrCreate()
sc = spark.sparkContext
import pandas as pd
from datetime import datetime

# 配置文件路径
input_file = r"D:\桌面\outfiler\xin\pull.csv"  # 替换为您的数据文件路径
output_file = "D:\桌面\outfiler\sss.csv"  # 替换为保存结果的路径

# 读取数据
df = pd.read_csv(input_file)

# 确保 time 字段为日期类型
df['time'] = pd.to_datetime(df['time'])

# 定义截止时间
cutoff_date = datetime(2020, 3, 31)

# 处理每个仓库
result = []
# Converted to PySpark map operation
rdd.map(lambda x: ...)
    # 分为早于2020/3/31和等于2020/3/31及之后的两部分
    before_cutoff = group[group['time'] < cutoff_date]
    on_or_after_cutoff = group[group['time'] >= cutoff_date]

    if not before_cutoff.empty:
        # 计算累计值
        total_created = before_cutoff['pulls_created'].sum()
        total_merged = before_cutoff['pulls_merged'].sum()

        # 检查是否存在 `2020/3/31` 的记录
        march_31_record = on_or_after_cutoff[on_or_after_cutoff['time'] == cutoff_date]
        if not march_31_record.empty:
            # 更新 `2020/3/31` 的记录
            idx = march_31_record.index[0]
            df.loc[idx, 'pulls_created'] += total_created
            df.loc[idx, 'pulls_merged'] += total_merged
        else:
            # 添加一条新记录
            new_row = {
                'id': None,  # 占位，稍后重新生成
                'repo_id': repo_id,
                'time': cutoff_date,
                'pulls_created': total_created,
                'pulls_merged': total_merged,
                'processing_efficiency': total_merged / total_created if total_created > 0 else 0
            }
            result.append(new_row)

    # 处理 `2020/3/31` 及之后的记录，重新计算 processing_efficiency
    on_or_after_cutoff['processing_efficiency'] = on_or_after_cutoff.apply(
        lambda row: row['pulls_merged'] / row['pulls_created'] if row['pulls_created'] > 0 else 0, axis=1
    )

    # 将 `2020/3/31` 及之后的记录添加到结果中
    result.extend(on_or_after_cutoff.to_dict('records'))

# 创建结果 DataFrame
result_df = pd.DataFrame(result)

# 按时间和 repo_id 排序
result_df.sort_values(by=['repo_id', 'time'], inplace=True)

# 重新生成 id
result_df['id'] = range(1, len(result_df) + 1)

# 保存结果
result_df.to_csv(output_file, index=False)

print(f"Data processing completed. Results saved to {output_file}.")
from pathlib import Path

# 定义文件路径
file_path = Path(r"F:\SLBAF-Net-20.04\modules\yolov5-dual\data\ImageSets\Main\val2.txt")
temp_file_path = file_path.with_name("train_temp.txt")  # 临时文件路径

# 逐行读取并修改，写入临时文件
with open(file_path, "r") as input_file, open(temp_file_path, "w") as output_file:
    for line in input_file:
        modified_line = line.strip() + ".png\n"  # 在每行末尾加上 .png
        output_file.write(modified_line)

# 用临时文件替换原文件
temp_file_path.replace(file_path)

print(f"文件已高效修改并覆盖: {file_path}")
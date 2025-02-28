import os
from PyPDF2 import PdfMerger

# 需要合并的文件所在的文件夹
target_path = 'D:/test/pdf_merge'

# 获取需要合并的文件名
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]

# 将文件名改为绝对路径
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

# 合并pdf文件
file_merger = PdfMerger()
for pdf in pdf_lst:
    file_merger.append(pdf)

# 合并后保存文件
file_merger.write("D:/test/pdf_merge/merge.pdf")
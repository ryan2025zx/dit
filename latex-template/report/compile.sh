#!/bin/bash

# 设置文件名变量
filename="report"

# 编译 LaTeX 文件
# 编译两次是为了让tableofcontents出现
for arg in "$@"; do
    if [[ "$arg" == "toc" ]]; then
        echo "Argument 'toc' found, executing the command."
        # 在这里执行你想运行的命令
        pdflatex "${filename}.tex"
        break  # 找到后就跳出循环，不再检查其他参数
    fi
done
xelatex "${filename}.tex"

# 检查编译是否成功
if [ $? -eq 0 ]; then
    echo "Compilation successful."
else
    echo "Compilation failed."
    exit 1
fi

# 删除生成的中间文件
rm -f "${filename}.aux" "${filename}.log" "${filename}.out" "${filename}.toc" "${filename}.lof" "${filename}.lot"

echo "Clean up complete."
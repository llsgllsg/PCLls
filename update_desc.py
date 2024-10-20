import requests
import os

# API接口地址
url = "https://api.leafone.cn/api/lishi?type=rand"

try:
    # 发送GET请求
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析返回的JSON数据
        data = response.json()

        # 获取desc内容
        desc_text = data.get("data", {}).get("desc", "无描述信息")

        # 生成或修改main.xaml文件
        file_path = "main.xaml"
        if not os.path.exists(file_path):
            # 如果文件不存在，创建文件并写入基本结构
            with open(file_path, "w", encoding='utf-8') as f:
                f.write('<local:MyCard Title="纯文本" Margin="0,0,0,15" CanSwap="True" IsSwaped="True">\n')
                f.write('\t<StackPanel Margin="25,40,23,15">\n')
                f.write(f'\t\t<TextBlock TextWrapping="Wrap" Margin="0,0,0,4" Text="{desc_text}" />\n')
                f.write('\t</StackPanel>\n')
                f.write('</local:MyCard>\n')
            print("文件 main.xaml 已创建并保存内容")

        else:
            # 如果文件存在，读取文件内容
            with open(file_path, "r", encoding='utf-8') as f:
                content = f.read()

            # 使用正则表达式替换Text属性内的内容
            import re
            new_content = re.sub(
                r'(<TextBlock TextWrapping="Wrap" Margin="0,0,0,4" Text=")(.*?)(" />)',
                r'\1' + desc_text + r'\3',
                content
            )

            # 写入新的内容
            with open(file_path, "w", encoding='utf-8') as f:
                f.write(new_content)

            print("main.xaml 文件已更新")

    else:
        print("请求失败，状态码：", response.status_code)

except requests.exceptions.RequestException as e:
    print("请求出错：", e)

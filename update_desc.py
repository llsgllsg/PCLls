import requests
import os
import re

# API 接口地址
url = "https://api.leafone.cn/api/lishi?type=rand"

try:
    # 发送 GET 请求
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析返回的 JSON 数据
        data = response.json()
        print("API返回的数据:", data)  # 打印 API 返回的数据

        # 获取必要的信息
        title = data.get("data", {}).get("title", "无标题信息")
        type_event = data.get("data", {}).get("type", "无类型信息")
        desc_text = data.get("data", {}).get("desc", "无描述信息")

        # 生成或修改 main.xaml 文件的路径
        file_path = "main.xaml"
        
        if not os.path.exists(file_path):
            # 如果文件不存在，创建文件并写入基本结构
            with open(file_path, "w", encoding='utf-8') as f:
                f.write(f'<local:MyCard Title="事件：{title}，类型：{type_event}" Margin="0,0,0,15" CanSwap="True" IsSwaped="True">\n')
                f.write('\t<StackPanel Margin="25,40,23,15">\n')
                f.write(f'\t\t<TextBlock TextWrapping="Wrap" Margin="0,0,0,4" Text="{desc_text}" />\n')
                f.write('\t</StackPanel>\n')
                f.write('</local:MyCard>\n')
            print("文件 main.xaml 已创建并保存内容")
        else:
            # 如果文件存在，读取文件内容
            with open(file_path, "r", encoding='utf-8') as f:
                content = f.read()

            print("旧内容:\n", content)  # 打印旧内容
            
            # 使用正则表达式替换第一个匹配的内容
            pattern = r'(<local:MyCard Title="事件：)(.*?)(，类型：.*?" Margin=.*?>\n\s+<StackPanel.*?>\n\s+<TextBlock TextWrapping="Wrap" Margin="0,0,0,4" Text=")(.*?)("\s*/>\n\s+</StackPanel>\n\s+</local:MyCard>'
            new_content = f'\\1{title}，类型：{type_event}\\3{desc_text}\\5'
            
            updated_content = re.sub(pattern, new_content, content, count=1, flags=re.DOTALL)

            # 仅当内容不同的时候才写入新的内容
            if content != updated_content:
                with open(file_path, "w", encoding='utf-8') as f:
                    f.write(updated_content)
                print("main.xaml 文件已更新")
            else:
                print("内容没有变化，不进行更新。")

    else:
        print("请求失败，状态码：", response.status_code)

except requests.exceptions.RequestException as e:
    print("请求出错：", e)

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
        print("API返回的数据:", data)  # 打印API返回的数据

        # 获取必要的信息
        title = data.get("data", {}).get("title", "无标题信息")
        type_event = data.get("data", {}).get("type", "无类型信息")
        desc_text = data.get("data", {}).get("desc", "无描述信息")

        # 生成或修改main.xaml文件的路径
        file_path = "main.xaml"
        
        # 新增的前缀内容
        header_content = '<local:MyCard Title="欢迎使用历史上的今天" Margin="10,0,250,15" CanSwap="False" IsSwaped="True">\n    <StackPanel Margin="25,75,23,15">\n        <local:MyImage Height="200" HorizontalAlignment="Center" Source="https://cn-sy1.rains3.com/123456/tp.png" />\n    </StackPanel>\n</local:MyCard>\n'  
        if not os.path.exists(file_path):
            # 如果文件不存在，创建文件并写入基本结构
            with open(file_path, "w", encoding='utf-8') as f:
                f.write(header_content)
                f.write(f'<local:MyCard Title="事件：{title}，类型：{type_event}" Margin="300,-300,0,15" CanSwap="False" IsSwaped="True">\n')
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
            
            # 建立 expected 新内容字符串
            new_content = f'<local:MyCard Title="事件：{title}，类型：{type_event}" Margin="300,-315,0,15" CanSwap="False" IsSwaped="True">\n' \
                          f'\t<StackPanel Margin="25,40,23,15">\n' \
                          f'\t\t<TextBlock TextWrapping="Wrap" Margin="0,0,0,4" Text="{desc_text}" />\n' \
                          f'\t</StackPanel>\n' \
                          f'</local:MyCard>\n'

            print("构建的新内容:\n", new_content)  # 打印新内容
            
            # 仅当内容不同的时候才写入新的内容
            if content != new_content:
                with open(file_path, "w", encoding='utf-8') as f:
                    f.write(header_content)
                    f.write(new_content)
                print("main.xaml 文件已更新")
            else:
                print("内容没有变化，不进行更新。")

        # 添加内容
        with open(file_path, "a", encoding='utf-8') as f:  # 以追加模式打开文件
            f.write('\n<local:MyCard Margin="0,-6,0,12" Title="欢迎"> <!--下面不是卡片，所以不用0,0,0,12-->\n')
            f.write('     <StackPanel Margin="24,35,24,15">\n')
            f.write('          <TextBlock HorizontalAlignment="Center" Margin="0,0,0,0"\n')
            f.write('               Foreground="{DynamicResource ColorBrush2}" FontSize="20"\n')
            f.write('               Text="  " />\n')
            f.write('          <Calendar HorizontalAlignment="Center" Margin="0,12,0,10" />\n')
            f.write('          <TextBlock Margin="5,0,5,12" TextWrapping="Wrap" HorizontalAlignment="Center"\n')
            f.write('               Foreground="{DynamicResource ColorBrush1}" Text="{cave}" />\n')
            f.write('     </StackPanel>\n')
            f.write('</local:MyCard> \n\n')  # 添加结束标记和换行

        print("附加内容已成功添加到 main.xaml 文件中。")

    else:
        print("请求失败，状态码：", response.status_code)

except requests.exceptions.RequestException as e:
    print("请求出错：", e)

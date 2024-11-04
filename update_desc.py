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
        header_content = '<StackPanel.Resources>\n    <Style TargetType="TextBlock" x:Key="AlertText">\n        <Setter Property="FontWeight" Value="ExtraBold" />\n        <Setter Property="FontSize" Value="12" />\n        <Setter Property="HorizontalAlignment" Value="Left" />\n        <Setter Property="Margin" Value="50,13,0,0" />\n    </Style>\n\n    <Style TargetType="Path" x:Key="AnimatedPathStyle">\n        <Setter Property="Fill" Value="{DynamicResource ColorBrush4}" />\n        <Style.Triggers>\n            <Trigger Property="IsMouseOver" Value="True">\n                <Setter Property="Fill" Value="{DynamicResource ColorBrush2}" />\n            </Trigger>\n        </Style.Triggers>\n    </Style>\n\n    <Style x:Key="RoundedGroupBoxStyle" TargetType="{x:Type GroupBox}">\n        <Setter Property="Template">\n            <Setter.Value>\n                <ControlTemplate TargetType="{x:Type GroupBox}">\n                    <Border CornerRadius="10" BorderBrush="{TemplateBinding BorderBrush}"\n                        BorderThickness="{TemplateBinding BorderThickness}"\n                        Background="{TemplateBinding Background}">\n                        <Grid>\n                            <Grid.RowDefinitions>\n                                <RowDefinition Height="Auto" />\n                                <RowDefinition Height="*" />\n                            </Grid.RowDefinitions>\n                            <!-- 标题栏 -->\n                            <Border Grid.Row="0" BorderThickness="1,1,1,0"\n                                Background="{TemplateBinding BorderBrush}" CornerRadius="10,10,0,0"\n                                Height="30">\n                                <!-- 设置标题栏的字体 -->\n                                <Label Content="{TemplateBinding Header}" Padding="3"\n                                    HorizontalAlignment="Center" VerticalAlignment="Center"\n                                    Foreground="White"\n                                    FontFamily="YouYuan" FontSize="14" />\n                            </Border>\n                            <!-- 内容 -->\n                            <ContentPresenter Grid.Row="1" Margin="{TemplateBinding Padding}" />\n                        </Grid>\n                    </Border>\n                </ControlTemplate>\n            </Setter.Value>\n        </Setter>\n    </Style>\n\n    <ControlTemplate TargetType="ContentControl" x:Key="Separator">\n        <Grid Margin="0,0,0,15">\n            <Grid.ColumnDefinitions>\n                <ColumnDefinition Width="1*" />\n                <ColumnDefinition Width="100" />\n                <ColumnDefinition Width="1*" />\n            </Grid.ColumnDefinitions>\n            <Line X1="0" X2="100" Stroke="{DynamicResource ColorBrush5}" StrokeThickness="1.5"\n                HorizontalAlignment="Center" Stretch="Fill" Grid.Column="0" />\n            <TextBlock Text="{TemplateBinding Content}" HorizontalAlignment="Center" FontSize="14"\n                Foreground="{DynamicResource ColorBrush5}" Grid.Column="1"\n                VerticalAlignment="Center" />\n            <Line X1="0" X2="100" Stroke="{DynamicResource ColorBrush5}" StrokeThickness="1.5"\n                HorizontalAlignment="Center" Stretch="Fill" Grid.Column="2" />\n        </Grid>\n    </ControlTemplate>\n</StackPanel.Resources>\n<StackPanel.Triggers>\n    <EventTrigger RoutedEvent="StackPanel.Loaded">\n        <BeginStoryboard>\n            <Storyboard x:Name="animation" RepeatBehavior="Forever">\n                <ColorAnimation BeginTime="0:0:2"\n                    Storyboard.TargetName="AlertText1"\n                    Storyboard.TargetProperty="(TextBlock.Foreground).(SolidColorBrush.Color)"\n                    From="#954024" To="#00000000" Duration="0:0:3" />\n                <ColorAnimation BeginTime="0:0:14"\n                    Storyboard.TargetName="AlertText1"\n                    Storyboard.TargetProperty="(TextBlock.Foreground).(SolidColorBrush.Color)"\n                    From="#00000000" To="#954024" Duration="0:0:3" />\n                <ColorAnimation BeginTime="0:0:4"\n                    Storyboard.TargetName="AlertText2"\n                    Storyboard.TargetProperty="(TextBlock.Foreground).(SolidColorBrush.Color)"\n                    From="#00000000" To="#954024" Duration="0:0:3" />\n                <ColorAnimation BeginTime="0:0:7"\n                    Storyboard.TargetName="AlertText2"\n                    Storyboard.TargetProperty="(TextBlock.Foreground).(SolidColorBrush.Color)"\n                    From="#954024" To="#00000000" Duration="0:0:3" />\n                <ColorAnimation BeginTime="0:0:9"\n                    Storyboard.TargetName="AlertText3"\n                    Storyboard.TargetProperty="(TextBlock.Foreground).(SolidColorBrush.Color)"\n                    From="#00000000" To="#954024" Duration="0:0:3" />\n                <ColorAnimation BeginTime="0:0:12"\n                    Storyboard.TargetName="AlertText3"\n                    Storyboard.TargetProperty="(TextBlock.Foreground).(SolidColorBrush.Color)"\n                    From="#954024" To="#00000000" Duration="0:0:3" />\n            </Storyboard>\n        </BeginStoryboard>\n    </EventTrigger>\n</StackPanel.Triggers>\n\n<local:MyCard Title="欢迎" Margin="-28,-26,-28,20" Height="40">\n    <TextBlock x:Name="AlertText1" Style="{StaticResource AlertText}" Foreground="#954024">\n        历史上的今天主页~\n    </TextBlock>\n    <TextBlock x:Name="AlertText2" Style="{StaticResource AlertText}" Foreground="#00000000">\n        简约~~~\n    </TextBlock>\n    <TextBlock x:Name="AlertText3" Style="{StaticResource AlertText}" Foreground="#00000000">\n        历史上的今天！\n    </TextBlock>\n    <TextBlock Margin="0,13,80,0" Foreground="{DynamicResource ColorBrush5}"\n        HorizontalAlignment="Right"\n        Text="llsgllsg " FontWeight="ExtraBold" FontStyle="Italic" />\n    <local:MyIconTextButton Margin="0,5,5,6" Height="35" HorizontalAlignment="Right"\n        Text="刷新" EventType="刷新主页" Grid.Column="1"\n        LogoScale="0.8" ColorType="Highlight"\n        Logo="M256.455,8C322.724,8.119,382.892,34.233,427.314,76.685L463.029,40.97C478.149,25.851,504,36.559,504,57.941L504,192C504,205.255,493.255,216,480,216L345.941,216C324.559,216,313.851,190.149,328.97,175.029L370.72,133.279C339.856,104.38 299.919,88.372 257.49,88.006 165.092,87.208 87.207,161.983 88.0059999999999,257.448 88.764,348.009 162.184,424 256,424 297.127,424 335.997,409.322 366.629,382.444 371.372,378.283 378.535,378.536 382.997,382.997L422.659,422.659C427.531,427.531 427.29,435.474 422.177,440.092 378.202,479.813 319.926,504 256,504 119.034,504 8.001,392.967 8,256.002 7.999,119.193 119.646,7.755 256.455,8z" />\n</local:MyCard>'

        if not os.path.exists(file_path):
            # 如果文件不存在，创建文件并写入基本结构
            with open(file_path, "w", encoding='utf-8') as f:
                f.write(header_content)
                f.write(f'<local:MyCard Title="事件：{title}，类型：{type_event}" Margin="0,0,0,15" CanSwap="False" IsSwaped="True">\n')
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
            new_content = f'<local:MyCard Title="事件：{title}，类型：{type_event}" Margin="0,0,0,15" CanSwap="False" IsSwaped="True">\n' \
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

            # 继续追加其他内容
            f.write('<local:MyCard Margin="0,0,0,8">\n')
            f.write('     <StackPanel Margin="24,6,24,12">\n')
            f.write('          <Grid>\n')
            f.write('               <Grid.ColumnDefinitions>\n')
            f.write('                    <ColumnDefinition Width="1*" />\n')
            f.write('                    <ColumnDefinition Width="1*" />\n')
            f.write('               </Grid.ColumnDefinitions>\n')
            f.write('               <local:MyIconTextButton Margin="0,5,0,6" Height="35" HorizontalAlignment="Center"\n')
            f.write('                    Text="作者网站" EventType="打开网页" Grid.Column="0"\n')
            f.write('                    EventData="https://llsgllsg.rth1.xyz"\n')
            f.write('                    LogoScale="0.8" ColorType="Highlight"\n')
            f.write('                    Logo="M13.5,4A1.5,1.5 0 0,0 12,5.5A1.5,1.5 0 0,0 13.5,7A1.5,1.5 0 0,0 15,5.5A1.5,1.5 0 0,0 13.5,4M13.14,8.77C11.95,8.87 8.7,11.46 8.7,11.46C8.5,11.61 8.56,11.6 8.72,11.88C8.88,12.15 8.86,12.17 9.05,12.04C9.25,11.91 9.58,11.7 10.13,11.36C12.25,10 10.47,13.14 9.56,18.43C9.2,21.05 11.56,19.7 12.17,19.3C12.77,18.91 14.38,17.8 14.54,17.69C14.76,17.54 14.6,17.42 14.43,17.17C14.31,17 14.19,17.12 14.19,17.12C13.54,17.55 12.35,18.45 12.19,17.88C12,17.31 13.22,13.4 13.89,10.71C14,10.07 14.3,8.67 13.14,8.77Z" />\n')
            f.write('               
            f.write('          <local:MyListItem Margin="-2,0,0,0"\n')
            f.write('               Logo="pack://application:,,,/images/blocks/GoldBlock.png" Title="今日人品"\n')
            f.write('               Info="试试手气！" EventType="今日人品" Type="Clickable" />\n')
            f.write('          <local:MyListItem Margin="-2,0,0,0"\n')
            f.write('               Logo="pack://application:,,,/images/blocks/Grass.png" Title="启动基岩版"\n')
            f.write('               Info="以 URL Scheme 的方式启动电脑上的 MC 基岩版。" EventType="打开网页" EventData="minecraft://"\n')
            f.write('               Type="Clickable" />\n')
            f.write('          <local:MyListItem Margin="-2,0,0,0"\n')
            f.write('               Logo="pack://application:,,,/images/blocks/CommandBlock.png" Title="网页捷径"\n')
            f.write('               Type="Clickable"\n')
            f.write('               Info="打开网页捷径页面" EventType="打开帮助"\n')
            f.write('               EventData="https://cn-sy1.rains3.com/123456/jj.json" />\n')
            f.write('<!--十分感谢MFn233的简单主页的部分代码此主页使用了MFn233简单主页后来——也就是11月3号更新又使用了信标的代码啊啊啊啊啊啊啊啊的代码更新历史事件使用了一个不知名API和github actions自动部署-->\n')
            f.write('<local:MyListItem Margin="-2,0,0,0" Info="llsgllsg"\n')
            f.write(' Logo="pack://application:,,,/images/Blocks/Fabric.png" Title="关于项目"\n')
            f.write('EventType="弹出窗口"\n')
            f.write(' EventData="关于项目|我是llsgllsg，该主页部分使用了MFn233的代码，后来在11月3号更新上部分使用了信标的代码，并在GitHub上开源。欢迎你前往仓库为我的项目提issue\n©llsgllsg 2024"\n')
            f.write(' Type="Clickable" />\n')
            f.write('</StackPanel>\n')
            f.write('</local:MyCard>\n')
            f.write('<StackPanel>\n')
            f.write('  <Border Background="#A0FFFFFF" Height="200" Margin="-25,10,-25,-20"\n')
            f.write('    BorderThickness="0,2,0,0" BorderBrush="#954024">\n')
            f.write('    <StackPanel Margin="40,15,0,20">\n')
            f.write('      <TextBlock Text="PCL2历史上的今天主页 Next" Foreground="#954024" FontSize="16" Margin="0,5,5,5" />\n')
            f.write('      <TextBlock> Originally By: llsgllsg<LineBreak />\n')
            f.write('          GitHub仓库: <Underline>\n')
            f.write('            <local:MyTextButton Margin="0,0,0,-3" EventType="打开网页"\n')
            f.write('              Text="https://github.com/llsgllsg/PCLls"\n')
            f.write('              EventData="https://github.com/llsgllsg/PCLls"\n')
            f.write('              ToolTip="点击打开GitHub" />\n')
            f.write('          </Underline> <LineBreak />\n')
            f.write('          Gitee仓库！不是最新: <Underline>\n')
            f.write('            <local:MyTextButton Margin="0,0,0,-3" EventType="打开网页"\n')
            f.write('              Text="https://gitee.com/llsgllsg/PCLls"\n')
            f.write('              EventData="https://gitee.com/llsgllsg/PCLls"\n')
            f.write('              ToolTip="点击打开Gitee" />\n')
            f.write('          </Underline> <LineBreak />\n')
            f.write('          <LineBreak />\n')
            f.write('          无特殊声明本主页采用 <Underline>\n')
            f.write('            <local:MyTextButton Margin="0,0,0,-2" Text="CC BY-NC-SA 4.0" EventType="打开网页"\n')
            f.write('              EventData="https://creativecommons.org/licenses/by-nc-sa/4.0/ " />\n')
            f.write('          </Underline>\n')
            f.write('          授权。 <LineBreak />\n')
            f.write('         </TextBlock>\n')
            f.write('     </StackPanel>\n')
            f.write('   </Border>\n')
            f.write('</StackPanel>\n')

        print("附加内容已成功添加到 main.xaml 文件中。")

    else:
        print("请求失败，状态码：", response.status_code)

except requests.exceptions.RequestException as e:
    print("请求出错：", e)

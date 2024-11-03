import os

# 定义要添加的内容
content_to_add = """<StackPanel.Resources>
    <Style TargetType="TextBlock" x:Key="AlertText">
        <Setter Property="FontWeight" Value="ExtraBold" />
        <Setter Property="FontSize" Value="12" />
        <Setter Property="HorizontalAlignment" Value="Left" />
        <Setter Property="Margin" Value="50,13,0,0" />
    </Style>
    <Style TargetType="Path" x:Key="AnimatedPathStyle">
        <Setter Property="Fill" Value="{DynamicResource ColorBrush4}" />
        <Style.Triggers>
            <Trigger Property="IsMouseOver" Value="True">
                <Setter Property="Fill" Value="{DynamicResource ColorBrush2}" />
            </Trigger>
        </Style.Triggers>
    </Style>
    <Style x:Key="RoundedGroupBoxStyle" TargetType="{x:Type GroupBox}">
        <Setter Property="Template">
            <Setter.Value>
                <ControlTemplate TargetType="{x:Type GroupBox}">
                    <Border CornerRadius="10" BorderBrush="{TemplateBinding BorderBrush}"
                        BorderThickness="{TemplateBinding BorderThickness}"
                        Background="{TemplateBinding Background}">
                        <Grid>
                            <Grid.RowDefinitions>
                                <RowDefinition Height="Auto" />
                                <RowDefinition Height="*" />
                            </Grid.RowDefinitions>
                            <Border Grid.Row="0" BorderThickness="1,1,1,0"
                                Background="{TemplateBinding BorderBrush}" CornerRadius="10,10,0,0"
                                Height="30">
                                <Label Content="{TemplateBinding Header}" Padding="3"
                                    HorizontalAlignment="Center" VerticalAlignment="Center"
                                    Foreground="White"
                                    FontFamily="YouYuan" FontSize="14" />
                            </Border>
                            <ContentPresenter Grid.Row="1" Margin="{TemplateBinding Padding}" />
                        </Grid>
                    </Border>
                </ControlTemplate>
            </Setter.Value>
        </Setter>
    </Style>
    <ControlTemplate TargetType="ContentControl" x:Key="Separator">
        <Grid Margin="0,0,0,15">
            <Grid.ColumnDefinitions>
                <ColumnDefinition Width="1*" />
                <ColumnDefinition Width="100" />
                <ColumnDefinition Width="1*" />
            </Grid.ColumnDefinitions>
            <Line X1="0" X2="100" Stroke="{DynamicResource ColorBrush5}" StrokeThickness="1.5"
                HorizontalAlignment="Center" Stretch="Fill" Grid.Column="0" />
            <TextBlock Text="{TemplateBinding Content}" HorizontalAlignment="Center" FontSize="14"
                Foreground="{DynamicResource ColorBrush5}" Grid.Column="1"
                VerticalAlignment="Center" />
            <Line X1="0" X2="100" Stroke="{DynamicResource ColorBrush5}" StrokeThickness="1.5"
                HorizontalAlignment="Center" Stretch="Fill" Grid.Column="2" />
        </Grid>
    </ControlTemplate>
</StackPanel.Resources>
"""

# 查找当前目录下的main.xaml文件
current_directory = os.getcwd()
xaml_file_path = os.path.join(current_directory, 'main.xaml')

# 如果文件存在，添加内容
if os.path.exists(xaml_file_path):
    with open(xaml_file_path, 'r', encoding='utf-8') as file:
        original_content = file.read()

    # 将新内容添加到开头
    new_content = content_to_add + original_content

    # 写回文件
    with open(xaml_file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

    print(f"已在 {xaml_file_path} 文件开头添加内容。")
else:
    print("未找到 main.xaml 文件。")

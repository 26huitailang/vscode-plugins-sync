# vscode-plugins-sync

同步 VSCode/Cursor 插件到离线环境

## 环境准备

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows

# 安装依赖
pip install -r requirements.txt
```

## 使用方法

1. 运行脚本下载插件

```bash
python3 main.py
# 根据提示选择编辑器类型：
# 1: VSCode（默认）
# 2: Cursor
```

2. 打包文件

```bash
# Linux/macOS
zip -r vscode-plugins.zip extensions install.ps1

# Windows (PowerShell)
Compress-Archive -Path extensions, install.ps1 -DestinationPath vscode-plugins.zip
```

3. 在目标机器上

- 解压 vscode-plugins.zip
- 运行 install.ps1 安装插件

## 注意事项

- 确保目标机器已安装对应的编辑器（VSCode 或 Cursor）
- 目标机器需要有 PowerShell 环境
- 如果遇到权限问题，可能需要以管理员身份运行 PowerShell

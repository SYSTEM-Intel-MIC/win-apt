# WinApt

> apt for Windows -- 在 Windows 上用熟悉的方式管理软件包

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)

## Features

- 100% apt 语法兼容: `install`, `remove`, `update`, `upgrade`, `search`, `show` ...
- 双后端: 自动检测 [winget](https://github.com/microsoft/winget-cli) 和/或 [Chocolatey](https://chocolatey.org/)
- 同时提供 `apt` 和 `apt-get` 命令
- 80+ 个彩蛋 (`apt moo`, `apt-get moo -vvvvv`)
- 零外部依赖, 纯 Python 标准库
- 可配置: `~/.winapt/config.json`

## Install

### 方式一: 双击安装 (推荐)

1. 下载本仓库 ZIP 并解压
2. 双击 `install.bat`
3. 重启终端, 输入 `apt --version` 验证

### 方式二: pip 手动安装

```powershell
git clone https://github.com/YOUR_USERNAME/winapt.git
cd winapt
pip install .
```

### 方式三: 直接运行 (无需安装)

```powershell
python apt.py --version
```

## Usage

```powershell
apt update                          # 更新软件包索引
apt install firefox                 # 安装软件
apt install firefox notepadplusplus # 批量安装
apt remove firefox                  # 移除软件
apt purge firefox                   # 彻底删除 (含配置)
apt upgrade                         # 升级所有软件
apt full-upgrade                    # 完整系统升级
apt search browser                  # 搜索软件
apt show firefox                    # 查看详情
apt list --installed                # 列出已安装
apt list --upgradable               # 列出可升级
apt autoremove                      # 清理无用依赖
apt cache clean                     # 清理缓存
apt moo                             # 经典彩蛋
apt-get moo -vvvvv                  # 超级牛力
```

## Commands

| Command | Description |
|---------|-------------|
| `apt update` | 更新软件包索引 |
| `apt upgrade [pkg...]` | 升级软件包 |
| `apt full-upgrade` | 完整系统升级 |
| `apt install <pkg...>` | 安装软件包 |
| `apt remove <pkg...>` | 移除软件包 |
| `apt purge <pkg...>` | 彻底删除 (含配置) |
| `apt autoremove` | 自动清理无用包 |
| `apt search <keyword>` | 搜索软件包 |
| `apt show <pkg>` | 显示软件包详情 |
| `apt list [pattern]` | 列出软件包 |
| `apt list --installed` | 列出已安装 |
| `apt list --upgradable` | 列出可升级 |
| `apt depends <pkg>` | 显示依赖 |
| `apt rdepends <pkg>` | 显示反向依赖 |
| `apt policy [pkg]` | 显示策略 |
| `apt download <pkg>` | 下载软件包 |
| `apt cache {clean\|stats\|dump}` | 缓存管理 |
| `apt edit-sources` | 编辑源列表 |
| `apt moo` | 彩蛋 |
| `apt --version` | 显示版本 |

### Global Options

```
-y, --yes          自动确认 (不提示)
-s, --simulate     模拟执行 (不实际操作)
-q, --quiet        静默模式
-v, --verbose      详细输出 (可叠加)
--no-color         禁用彩色输出
```

## Easter Eggs

```powershell
# 基础彩蛋
apt moo
         (__)
         (oo)
   /------\/
  / |    ||
 *  /\---/\
    ~~   ~~
...."Have you mooed today?"...

# 超级牛力
apt-get moo -vvvvv

# 随机彩蛋 (每次不同)
apt moo -v
```

## Config

配置文件: `%USERPROFILE%\.winapt\config.json`

```json
{
  "sources": ["winget", "choco"],
  "priority": "winget",
  "cache_ttl": 3600,
  "color_output": true,
  "confirm_install": true,
  "simulate": false
}
```

| Key | Description |
|-----|-------------|
| `sources` | 启用的后端列表 |
| `priority` | 优先使用的后端 |
| `cache_ttl` | 缓存过期时间 (秒) |
| `color_output` | 启用彩色输出 |
| `confirm_install` | 安装前确认 |
| `simulate` | 默认模拟模式 |

## Build

```powershell
pip install pyinstaller
.\build.bat
```

产物位于 `dist\`: `apt.exe`, `apt-get.exe`, `winapt.zip`

## Project Structure

```
winapt/
├── .github/workflows/build.yml  # CI/CD
├── core/
│   ├── config.py                # 配置管理
│   ├── parser.py                # 参数解析
│   ├── executor.py              # 命令执行器
│   └── package.py               # 数据模型
├── backends/
│   ├── base.py                  # 后端抽象基类
│   ├── winget.py                # winget 后端
│   └── choco.py                 # Chocolatey 后端
├── apt.py                       # apt 入口
├── apt_get.py                   # apt-get 入口
├── easter_eggs.py               # 彩蛋集合
├── install.bat                  # 一键安装
├── build.bat                    # 编译脚本
├── setup.py                     # 包配置
└── README.md
```

## Requirements

- Windows 10/11
- Python 3.8+
- [winget](https://aka.ms/getwinget) 和/或 [Chocolatey](https://chocolatey.org/install)

## Contributing

1. Fork
2. Create branch (`git checkout -b feature/amazing-feature`)
3. Commit (`git commit -m 'Add some amazing feature'`)
4. Push (`git push origin feature/amazing-feature`)
5. Create Pull Request

## License

[MIT](LICENSE)

## Credits

- [Microsoft winget](https://github.com/microsoft/winget-cli)
- [Chocolatey](https://chocolatey.org/)
- [Debian apt](https://salsa.debian.org/apt-team/apt)

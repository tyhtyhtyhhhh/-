# github学习笔记

## 1. 什么是GitHub？

GitHub是一个面向开源及私有软件项目的托管平台，因为只支持Git作为唯一的版本库格式，故名GitHub。

GitHub提供了各种功能，包括：

- 代码托管：GitHub可以托管各种Git和SVN代码仓库，让你和他人协作开发。
- 项目管理：GitHub提供项目管理工具，包括看板、任务管理、wikis等。
- 代码 review：GitHub提供代码 review 功能，让你和他人一起审查代码。
- 第三方插件：GitHub提供第三方插件，可以与其他服务集成。
- 社交网络：GitHub拥有强大的社交网络功能，你可以跟别人分享你的想法、帮助他人、提出建议。
- 文档分享：GitHub可以分享你的文档，让他人帮助你更好的使用你的项目。


## 2. GitHub的优势

GitHub的优势主要有以下几点：

- 免费：GitHub是完全免费的，不收取任何费用。
- 社区支持：GitHub拥有强大的社区支持，你可以在上面找到志同道合的伙伴，提出你的想法、帮助他人。
- 版本控制：GitHub支持Git版本控制系统，这使得它成为开源项目的理想选择。
- 易用性：GitHub提供友好的图形界面，让你轻松上手。
- 安全性：GitHub提供安全措施，包括两步验证、代码审查、第三方应用的审核等。
- 协作性：GitHub支持团队协作，让你和他人一起开发项目。
- 透明度：GitHub提供详尽的日志，让你掌握项目进展。
- 免费私有仓库：GitHub提供免费的私有仓库，让你把自己的项目放到云端。


## 3. GitHub的使用方法

GitHub的使用方法主要有以下几点：

- 注册：首先你需要注册一个GitHub账号，注册地址为：https://github.com/join。
- 创建仓库：登录GitHub后，你可以创建自己的仓库，仓库的创建方法为：点击右上角的加号，选择New repository。
- 上传代码：你可以通过GitHub的Web界面或客户端上传你的代码，上传代码的方法有两种：
  1. 通过Web界面：点击仓库的Code按钮，然后点击Upload files按钮，选择你要上传的文件，并添加描述信息。
  2. 通过客户端：你可以安装GitHub客户端，然后在客户端上传你的代码。
- 克隆代码：你可以通过Git命令克隆别人的代码，克隆代码的方法为：点击仓库的Clone or download按钮，复制SSH或HTTPS地址，然后在命令行中输入git clone命令。
- 提交代码：你可以通过GitHub的Web界面或客户端提交你的代码，提交代码的方法有两种：
  1. 通过Web界面：点击仓库的Pull requests按钮，然后点击New pull request按钮，选择你要合并的分支，并添加描述信息。
  2. 通过客户端：你可以安装GitHub客户端，然后在客户端提交你的代码。
- 代码审查：你可以通过GitHub的Web界面或客户端发起代码审查，代码审查的方法有两种：
  1. 通过Web界面：点击仓库的Pull requests按钮，然后点击New pull request按钮，选择你要审查的分支，并添加描述信息。
  2. 通过客户端：你可以安装GitHub客户端，然后在客户端发起代码审查。
- 管理仓库：你可以管理仓库的权限、设置保护规则、管理Webhooks等，管理仓库的方法为：点击仓库的Settings按钮，然后选择对应的选项。
- 第三方应用：你可以通过GitHub的API、OAuth等方式与其他服务集成，与其他服务集成的方法为：点击仓库的Settings按钮，然后选择Integrations选项。
- 社交网络：你可以通过GitHub的社交网络功能与他人分享你的想法、帮助他人、提出建议，社交网络的方法为：点击右上角的加号，选择Your profile，然后选择Social选项。
- 文档分享：你可以通过GitHub的Web界面或客户端分享你的文档，文档分享的方法有两种：
  1. 通过Web界面：点击仓库的Wiki按钮，然后点击Create a new page按钮，添加文档内容。
  2. 通过客户端：你可以安装GitHub客户端，然后在客户端分享你的文档。

## 4、github的一些常用命令

- git clone：克隆远程仓库到本地
- git add：添加文件到暂存区
- git commit：提交暂存区到本地仓库
- git push：推送本地仓库到远程仓库
- git pull：拉取远程仓库到本地仓库
- git branch：创建分支
- git checkout：切换分支
- git merge：合并分支
- git log：查看提交历史
- git status：查看仓库状态

## 5、git文件状态

- 未跟踪文件：在工作区中，但不在版本库中的文件。
- 已跟踪文件：在版本库中有记录的文件。
- 已修改文件：在工作区中被修改过的文件，但没有提交到暂存区。
- 已暂存文件：在暂存区中被修改过的文件，但没有提交到本地仓库。
- 未提交文件：在本地仓库中，但没有推送到远程仓库的文件。


## 6、git基本命令

- git init：初始化一个Git仓库
- git add：添加文件到暂存区
- git commit：提交暂存区到本地仓库
- git push：推送本地仓库到远程仓库
- git pull：拉取远程仓库到本地仓库
- git branch：创建分支
- git checkout：切换分支
- git merge：合并分支
- git log：查看提交历史
- git status：查看仓库状态
- git reset：重置当前分支指向的HEAD
- git rm：删除文件
- git mv：移动或重命名文件
- git clone：克隆远程仓库到本地
- git config：配置Git的用户信息
- git help：查看Git命令的帮助信息





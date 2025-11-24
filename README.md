# Django Gallery - 图片相册管理系统

一个基于Django开发的图片相册管理系统，允许用户上传、分类和展示图片。系统使用Bootstrap 5实现现代化界面设计。

## 功能特性

- **图片上传**：用户可以上传图片并添加描述
- **分类管理**：支持为图片创建和选择分类
- **相册浏览**：以网格形式展示所有图片
- **图片详情**：查看单个图片的详细信息，包含前后导航功能
- **响应式设计**：使用Bootstrap 5实现现代化界面
- **图片下载**：支持图片下载功能
- **前后导航**：图片详情页支持前后切换功能

## 技术栈

- **后端**：Django 5.2.8
- **前端**：HTML, CSS, JavaScript, Bootstrap 5, Bootstrap Icons
- **数据库**：SQLite3
- **图片处理**：Django ImageField

## 项目结构

```
django_Gallery/
├── django_Gallery/           # Django项目配置
│   ├── settings.py          # 项目设置
│   ├── urls.py              # 主路由配置
│   └── ...
├── photos/                  # 图片应用
│   ├── models.py            # 数据模型 (图片、分类)
│   ├── views.py             # 视图逻辑 (包含前后导航功能)
│   ├── urls.py              # 应用路由
│   ├── forms.py             # 表单定义
│   └── templates/           # 模板文件
│       └── photos/
│           ├── Gallery.html # 相册主页 (Bootstrap 5网格布局)
│           ├── Photos.html  # 图片详情页 (包含前后导航、下载功能)
│           └── AddPhotos.html # 图片上传页 (包含实时预览)
├── media/                   # 媒体文件存储目录
├── static/                  # 静态文件目录
├── .gitignore              # Git忽略配置
├── db.sqlite3              # 数据库文件
└── manage.py               # Django管理脚本
```

## 模型设计

### Category (分类模型)
- `photos_name`: 分类名称

### Photo (图片模型)
- `category`: 与分类的外键关系
- `image`: 图片文件
- `description`: 图片描述
- `date_time`: 上传时间

## 页面功能

1. **相册主页** (`/home`)
   - 以响应式网格形式展示所有图片
   - 左侧分类导航栏
   - 支持按分类筛选
   - "添加图片"按钮

2. **图片详情页** (`/photos/<id>`)
   - 使用Bootstrap 5卡片设计展示单个图片
   - 图片描述和上传时间
   - 分类信息显示
   - 前后图片导航功能
   - 图片下载功能
   - 返回相册按钮

3. **图片上传页** (`/addphotos`)
   - 图片上传表单
   - 分类选择/创建功能
   - 描述输入框
   - 实时图片预览
   - 表单验证

## 主要改进

1. **UI/UX 改进**：
   - 使用Bootstrap 5完全重构了界面
   - 图片详情页添加了现代化的卡片式布局
   - 添加了前后图片导航功能
   - 添加了响应式设计

2. **功能增强**：
   - 在PhotosView中添加了获取前后图片的逻辑
   - 实现了前后导航功能
   - 添加了图片下载功能
   - 改进了图片信息展示

3. **代码优化**：
   - 使用Bootstrap Icons增强界面元素
   - 添加了阴影和圆角等现代设计元素
   - 优化了CSS样式

## 安装和运行

1. **克隆项目**
   ```bash
   git clone https://github.com/HDANface/Django-Gallery.git
   cd Django-Gallery
   ```

2. **创建虚拟环境并安装依赖**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或
   venv\Scripts\activate     # Windows
   
   pip install django
   pip install Pillow        # 用于图片处理
   ```

3. **数据库迁移**
   ```bash
   python manage.py migrate
   ```

4. **运行开发服务器**
   ```bash
   python manage.py runserver
   ```

5. **访问应用**
   - 应用主页: http://127.0.0.1:8000/home
   - 管理后台: http://127.0.0.1:8000/admin

## 使用说明

1. 访问 `/` 进入相册主页
2. 点击"Add Photos"按钮上传新图片
3. 在上传页面选择图片、添加描述、选择或创建分类
4. 在相册主页可以通过左侧分类导航筛选图片
5. 点击任意图片进入详情页查看大图和信息，使用左右按钮切换前后图片

## 环境要求

- Python 3.8+
- Django 5.2+
- Pillow (用于图片处理)

## 版权信息

此项目仅供学习参考使用。

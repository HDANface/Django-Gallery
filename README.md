# Django Gallery - 图片相册管理系统

一个基于Django开发的图片相册管理系统，允许用户上传、分类和展示图片。

## 功能特性

- **图片上传**：用户可以上传图片并添加描述
- **分类管理**：支持为图片创建和选择分类
- **相册浏览**：以网格形式展示所有图片
- **图片详情**：查看单个图片的详细信息
- **响应式设计**：使用Bootstrap 5实现现代化界面

## 技术栈

- **后端**：Django 5.2.8
- **前端**：HTML, CSS, JavaScript, Bootstrap 5
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
│   ├── views.py             # 视图逻辑
│   ├── urls.py              # 应用路由
│   ├── forms.py             # 表单定义
│   └── templates/           # 模板文件
│       └── photos/
│           ├── Gallery.html # 相册主页
│           ├── Photos.html  # 图片详情页
│           └── AddPhotos.html # 图片上传页
├── media/                   # 媒体文件存储目录
├── static/                  # 静态文件目录
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
   - 以卡片形式展示所有图片
   - 左侧分类导航栏
   - 支持按分类筛选
   - "添加图片"按钮

2. **图片详情页** (`/photos/<id>`)
   - 显示单个图片
   - 图片描述和上传时间
   - 分类信息
   - 前后图片导航
   - 下载功能

3. **图片上传页** (`/addphotos`)
   - 图片上传表单
   - 分类选择/创建
   - 描述输入
   - 实时图片预览

## 安装和运行

1. **克隆项目**
   ```bash
   git clone <your-repo-url>
   cd django_Gallery
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

4. **创建超级用户（可选）**
   ```bash
   python manage.py createsuperuser
   ```

5. **运行开发服务器**
   ```bash
   python manage.py runserver
   ```

6. **访问应用**
   - 应用主页: http://127.0.0.1:8000/home
   - 管理后台: http://127.0.0.1:8000/admin

## 使用说明

1. 访问 `/home` 进入相册主页
2. 点击"Add Photos"按钮上传新图片
3. 在上传页面选择图片、添加描述、选择或创建分类
4. 在相册主页可以通过左侧分类导航筛选图片
5. 点击任意图片进入详情页查看大图和信息

## 环境要求

- Python 3.8+
- Django 5.2+
- Pillow (用于图片处理)

## 版权信息

此项目仅供学习参考使用。
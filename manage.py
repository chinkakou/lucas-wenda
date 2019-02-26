from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app import app
from exts import db
from models import User,Question,Answer
#导入模型之后，在终端中进入项目文件夹，运行python manage.py db init初始化当前项目的迁移环境
#再运行python manage.py db migrate做一个迁移文件
#然后通过python manage.py db upgrade将模型映射到数据库当中

manager = Manager(app)

#使用Migrate绑定app和db
migrate = Migrate(app,db)

#添加迁移脚本的命令到manager中
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
from flask import Flask
app = Flask(__name__)

db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app

print("test over")
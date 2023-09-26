# 使用官方的Python镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到镜像中
COPY . /app

# 安装项目依赖项
RUN pip install -r requirements.txt

# 设置环境变量
ENV FLASK_APP=app.py

# 暴露端口
EXPOSE 5000

# 启动Flask应用
CMD ["flask", "run", "--host=0.0.0.0"]
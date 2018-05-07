

##nginx+uwsgi 部署服务器

购买服务器    Linux ubuntu16.04          

升级环境    apt update    

安装pip3    apt-get  install python3-pip

安装nginx   apt install nginx         

测试nginx   nginx -t     |||   /etc/init.d/nginx start(stop)          

移动到相关的环境  cd /var/www

安装环境    pip3 install virtualenv          

升级环境    pip3 install --upgrade pip            

创建环境    virtualenv  -p python3 envpro  

入虚拟环境    source envpro/bin/activate          

安装Django    pip3 install django==1.11.6          

安装相应的模块 django-bootstrap4   django-simple-captcha  pymysql

安装 Mysql  apt-get install mysql-server

安装mysql   apt install libmysqlclient-dev



``` python
安装成功后可以通过下面的命令测试是否安装成功：netstat -tap | grep mysql

现在设置mysql允许远程访问，首先编辑文件/etc/mysql/mysql.conf.d/mysqld.cnf：

sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf

注释掉bind-address = 127.0.0.1：

保存退出，然后进入mysql服务，执行授权命令：

创建普通用户

  CREATE USER 'username'@'%' IDENTIFIED BY 'password';
    
给普通用户赋权

grant all on *.* to username@'%' identified by 'password' with grant option;

flush privileges;

然后执行quit命令退出mysql服务，执行如下命令重启mysql：

service mysql restart
```

安装需要依赖的包  apt-get install python3-dev  ####   apt-get install gcc

安装uwsgi    pip3 install uwsgi       还是在虚拟环境里面



```python
第一种
1. 安装Mezzanine    pip install mezzanine
2. 创建mezzanine    mezzanine-project librepath          
3. 移动目录    cd librepath          
4. 创建数据库    python manage.py  createdb          
5. 收集资源    python manage.py  collectstatic          
6. 修改设置    Vim librepath/settings.py          ALLOWDE_HOSTS    =[“服务器ip”]         
7. 测试    python manage.py runserver   
```

```python
第二种
1.安装git  apt-get install git
2.克隆自己的项目  git clone https://github.com/pizil-li/tanzhou
```

安装需要依赖的包  apt-get install python3-dev  ####   apt-get install gcc

安装uwsgi    pip3 install uwsgi        

```
查看端口号  lsof -i   

关闭端口  kill 端口号   

移动目录    cd  /var/www/tanzhou   

```







测试uwsgi    uwsgi --http :8000 --module tanzhou.wsgi          

在上一层环境中上传三个文件，nginx.conf  uwsgi.ini  uwsgi_params             

配置 socke  配置conf和ini             真实环境中安装uwsgi

测试    uwsgi --ini uwsgi.ini     测试   

把nginx文件配置    cd  /etc/nginx/sites-enabled          

删除默认文件    rm default          

创建软链接    ln -s /var/www/nginx.conf default  

重启 nginx     /etc/init.d/nginx start  

​            cd /var/www

启动uwsgi    uwsgi --ini uwsgi.ini          

设置自动启动    vim  /ect/rc.local          /usr/local/bin/uwsgi --ini  /var/www/uwsgi.ini                

reboot                   

参考 bilibili上讲接nginx的视频豆瓣源

<https://pypi.doubanio.com/simple/pip> 

install xxx -i [http://pypi.douban.com/simple/](https://www.douban.com/link2/?url=http%3A%2F%2Fpypi.douban.com%2Fsimple%2F)   
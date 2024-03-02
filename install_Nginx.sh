echo "它仅在CentoOS Stream 9 上运行测试成功，其它版本未进行测试 "
echo "它使用了YUM命令，因此仅支持 CentOS"
echo "它使用了自建节点，维护状态未知"
echo -e "你确定安装 Nginx 1.24.0 吗?[y/n]: \c"
read _INSTALL_FROM_YUM
if [[ "y" == "${_INSTALL_FROM_YUM}" ]]; then
	#安装编译工具及库文件
	yum -y install make zlib zlib-devel gcc-c++ libtool openssl openssl-devel
	#安装PCRE
	cd /usr/local/src/
	wget http://iwyz.love/pcre-8.45.tar.gz
	tar zxvf pcre-8.45.tar.gz
	rm -rf ./pcre-8.45.tar.gz
	cd ./pcre-8.45
	./configure
	make && make install
	#安装Nginx
	cd /usr/local/src/
	wget https://nginx.org/download/nginx-1.24.0.tar.gz
	tar zxvf nginx-1.24.0.tar.gz
	rm -rf ./nginx-1.24.0.tar.gz
	cd ./nginx-1.24.0
	./configure --prefix=/usr/local/webserver/nginx --with-http_stub_status_module --with-http_ssl_module --with-pcre=/usr/local/src/pcre-8.45
	make && make install
	#为 Nginx 创建用户 www
	/usr/sbin/groupadd www 
	/usr/sbin/useradd -g www www
	#创建目录，清空 nginx.conf 的配置
	rm -rf /usr/local/webserver/nginx/conf/nginx.conf
	mkdir /home/nginx_host
	mkdir /home/website_log
	mkdir /home/website_log/access
	mkdir /home/website_log/error
	echo '已经完成了 access/error/nginx_host 目录的创建'
	echo 'Nginx安装完毕，后续配置清前往 https://www.runoob.com/linux/nginx-install-setup.html 查看，紧接 Nginx 配置篇章中的配置nginx.conf'
	echo '注意：当 nginx_host 文件内有配置文件时才允许启动 Nginx'
fi
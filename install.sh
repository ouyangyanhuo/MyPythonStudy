echo "Only test in CentOS Stream 9"
echo -e "Do you want install hugo?[y/n]: \c"
read _INSTALL_FROM_YUM

if [[ "y" == "${_INSTALL_FROM_YUM}" ]]; then

	#安装依赖
	yum -y install git
	yum -y golang
	cd /
	cd /home
	mkdir hugo_install
	cd ./hugo_install
	wget https://github.com/gohugoio/hugo/releases/download/v0.123.6/hugo_0.123.6_Linux-64bit.tar.gz
	echo 'Install version is v0.123.6,it published in 2024/02/28'
	tar -zxvf hugo_0.123.6_Linux-64bit.tar.gz
	cp ./hugo /usr/bin
	cd /home
	rm -rf ./hugo_install
	mkdir ./hugo
	hugo new site /home/hugo --format yaml
	cd ./hugo 
	echo 'Fine'
fi
	
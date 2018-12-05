# docker

- Helloworld.df
	- 对应 DockerHub 上的仓库：houdongdong/hello-dockerfile

- eureka_server_dockerfile
	- 对应 DockerHub 上的仓库：houdongdong/eureka-server
	
	- [给 springboot项目制作Dockerfile镜像](https://blog.csdn.net/hnmpf/article/details/80092586)
	- [将SpringCloud Eureka 服务注册与发现部署到docker详解](https://blog.csdn.net/Michael_HM/article/details/79280720)
	- [Docker Swarm运行Spring Cloud应用（二）：Eureka高可用](https://yq.aliyun.com/articles/73493)

- git_dockerfile
	- Dockerfile 自动化构建脚本
	
- nginx_dockerfile
	- Dockerfile 自动化构建脚本

- mailer_dockerfile
	
- engine-install-url.bash 
	- 下载方法： curl -fsSL https://get.docker.com -o get-docker.sh
	- 可以通过这个 bash 脚本安装 docker
	- docker-machine create 就是用这个脚本 安装docker的
	- 被发布在 Apache web服务器上， URL是：http://<ip-address>/engine-install-url.bash
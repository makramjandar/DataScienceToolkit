[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)


## Dockerfile for the Fast AI course v3
This Dockerfile uses a pre-build and GPU-enabled pytorch image from nvidia to create an isolated environment for the 2018 fast.ai course. Those images are very convenient, because they come batteries included: All CUDA libraries, dependencies and pytorch is pre-installed and ready to go. Only the fast.ai library has to be installed.

### Who should use this Dockerfile?
If you are using your own PC with a CUDA enabled device I would highly recommend docker. While isolation with `venv` or `conda` isolates your python environment, it does not isolate the complex CUDA toolchain. Also sometimes if you want to use different stacks like keras/TensorFlow and pytorch they can have different dependencies. And it works great!

### Prerequisites
     - Your host runs Linux (I would always recommend that for deep learning!)
     - You have a CUDA enabled device and the drivers installed

#### Install docker-ce and the nvidia runtime
The first thing is to install docker and the nvidia runtime to pass a GPU into a container:
```shell
     # Install docker via get.docker script
     $ curl -fsSL get.docker.com -o get-docker.sh
     
     # Add the package repositories for nvidia docker
     $ curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | apt-key add -
     $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
     $ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
     tee /etc/apt/sources.list.d/nvidia-docker.list
     $ apt-get update
     
     # Install nvidia-docker2 and reload the Docker daemon configuration
     $ apt-get install -y nvidia-docker2
     $ pkill -SIGHUP dockerd
     
     
     # To test if everything is installed correctly you can run. 
     # This executes nvidia-smi` inside a container which should display your GPU.
     $ docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi
```
## Get a pre-build pytorch image with GPU support from nvidia
The nvidia GPU cloud is not a cloud service provider but an image registry similar to docker hub where you can download pre build images for free. The cool thing is: The developer at nvidia took care of all the necessary libraries and tools you need to have. It’s free and you can use the images for your own or commercial purposes, but you are not allowed to redistribute them.
Now to download the pytorch image use the command: `$ docker pull nvcr.io/nvidia/pytorch:18.05-py3`.

## What's inside and how to build
As you can see this is a pretty short Dockerfile and that's because of the pytorch image. All the nitty-gritty stuff is already done by nvidia. We only have to install the fast.ai library and download the data. I'm going to install the fast.ai library into the container but I'm going to mount the `fast.ai/data` folder from the host. That means, that the folder `fast.ai/data` is going to be the place where you have to store all persistent data: notebooks or code files you worked on or data you downloaded to play around. Everything else is going to be deleted when a container is deleted. Note, that you can also commit changes to a container and start and stop it (like a virtual machine). I'm not doing that, because I want to keep track of the changes I make. Also I'm disabling token and password protection, because this is for local use. So when you want to remote log on your workstation please use a ssh tunnel! To build the image download the Dockerfile to a local folder (with no other content than the Dockerfile), open a terminal in this folder and use the command:
```shell
  $ docker build -t makramjandar/fastai .
```
This should take quite a while.
## How to use it? 
Now you should create a data folder on your **host** where you download the cats and dogs data. For example in your home directory:
```shell
  $ cd ~
  $ mkdir data
  $ cd data
  $ wget http://files.fast.ai/data/dogscats.zip
  $ unzip -q dogscats.zipls
```
Now you can use the following command to start a container from the image. It's mounting the data folder into the container and also exposes the port 8888 for your browser. Use `localhost:8888` or the IP of your workstation. Keep in mind that only the data in `fast.ai/data` will be persistent when you start a new container!
```shell
$ docker run --runtime=nvidia -it --rm -v ~/data/fastai_course-v3:/fastai_course-v3/data -p 8888:8888 makramjandar/fastai_course-v3
```
Now let's create a `Notebooks` folder in our `data` folder to save Notebooks we create ourselves. Also we have to link the fast.ai library so that we can easily import things:
```shell
$ cd ~
$ mkdir data/Notebooks
$ ln -s /fastai/fastai/ fastai/data/Notebooks/fastai
```

#### Get updates
To get updates watch this repo or follow me on ...

Forked from KaiLicht https://github.com/KaiLicht

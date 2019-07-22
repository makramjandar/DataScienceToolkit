[![License](https://img.shields.io/badge/license-Do%20What%20The%20Fuck%20You%20Want-red.svg)](http://badges.mit-license.org)
[![](https://images.microbadger.com/badges/image/makramjandar/pytorch-fastai.svg)](https://microbadger.com/images/makramjandar/pytorch-fastai "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/makramjandar/pytorch-fastai.svg)](https://microbadger.com/images/makramjandar/pytorch-fastai "Get your own version badge on microbadger.com")
[Dockerfile](https://raw.githubusercontent.com/makramjandar/DataScienceToolkit/master/dockerfiles/pytorch/fastai/Dockerfile)


## Dockerfile for the Fast AI courses (v1-v3)
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
     
     # Install nvidia-docker2 via install-nvidia-docker2.sh script
     $ wget -O - -q 'https://raw.githubusercontent.com/makramjandar/Fast-Data-on-GCP/master/utils/install-nvidia-docker2.sh' | bash
     # To test if everything is installed correctly you can run. 
     # This executes nvidia-smi` inside a container which should display your GPU.
     $ docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi
```
## Get a pre-build pytorch image with GPU support from nvidia
The nvidia GPU cloud is not a cloud service provider but an image registry similar to docker hub where you can download pre build images for free. The cool thing is: The developer at nvidia took care of all the necessary libraries and tools you need to have. It’s free and you can use the images for your own or commercial purposes, but you are not allowed to redistribute them.
Now to download the pytorch image use the command: `$ docker pull nvcr.io/nvidia/pytorch:19.05-py3`.

## What's inside and how to build
As you can see this is a pretty short Dockerfile and that's because of the pytorch image. All the nitty-gritty stuff is already done by nvidia. We only have to install the fast.ai library and download the data. I'm going to install the fast.ai library into the container but I'm going to mount the `$HOME` folder from the host. That means, that the folder `$HOME` is going to be the place where you have to store all persistent data: notebooks or code files you worked on or data you downloaded to play around. Everything else is going to be deleted when a container is deleted. Note, that you can also commit changes to a container and start and stop it (like a virtual machine). I'm not doing that, because I want to keep track of the changes I make. Also I'm disabling token and password protection, because this is for local use. So when you want to remote log on your workstation please use a ssh tunnel! To build the image download the Dockerfile to a local folder (with no other content than the Dockerfile), open a terminal in this folder and use the command:
```shell
  $ docker build -t makramjandar/pytorch-fastai .
```
This should take quite a while.

## How to use it? 
Now we can use the following command to start a container from the image. It's mounting the $HOME folder into the container and also exposes the port 9999 for your browser. Use `localhost:9999` or the IP of your workstation. Keep in mind that only the data in `fastai/_home` will be persistent when you start a new container!
```shell
$ docker run -d -p 9999:9999 -v $HOME:/fastai/_home --runtime=nvidia --restart always makramjandar/pytorch-fastai:latest
```

#### Get updates
To get updates watch this repo or follow me ...

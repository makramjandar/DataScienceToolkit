[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)


This Dockerfile builds GPU images (via Nvidia-docker) for training purpose specifically for fastai course v3

Credit: this Dockerfile was originally published by https://github.com/ThatAIGeek/course-v3

* Installs software, which is used and/or mentioned in notebooks
* Install jupyterlab and some handy extensions for better experience. Jupyter notebook should also work but I never tried
* Set’s a jupyter password, so you can acces jupyterlab without token. Changes to jupyter_notebook_config.py should be made in order to enable this. The default password has been set as "jupyter". Here is the explanation, what to do https://jupyter-notebook.readthedocs.io/en/latest/public_server.html#preparing-a-hashed-password. 
* Changes default shell to bash
* Creates another user, this way inside of docker will look more like regular setup
* Sets up conda
* Uses conda to install pytorch, fastai and other usefull packages
* runs jupyterlab by default

Prerequisite: 
* The docker images requires cuda10.1 You need to have Nvidia driver version 410 installed on your machine first.
* Please following the instruction at https://github.com/NVIDIA/nvidia-docker to install nvidia-docker2.

Build command: `sudo docker image build -t fastai_v1:v3 .`

I’m running this to spin up my container `sudo docker run -p 8889:8888/tcp  -v /home/mj/Documents/git:/home/user/git -v /home/mj/Documents/git/data:/home/user/git/data --runtime=nvidia --ipc=host fastai_v1:v3`

- Note: simlink won't work in container, so you might need to attach multiple volumes to your container.

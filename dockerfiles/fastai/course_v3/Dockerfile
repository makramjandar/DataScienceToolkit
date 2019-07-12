FROM nvidia/cuda:10.1-base-ubuntu18.04

LABEL maintainer="Makram Jandar <makramjandar@gmail.com>"

# Install some basic utilities
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    sudo \
    git \
    bzip2 \
    unzip \
    libx11-6 \
    software-properties-common \
    ffmpeg \
    frei0r-plugins \
    vim \
    p7zip-full \
    wget \
    default-jdk \
    tmux \
    htop \
 && rm -rf /var/lib/apt/lists/*

# Create a working directory

RUN mkdir /app
WORKDIR /app
RUN chsh -s /bin/bash

# Create a non-root user and switch to it

RUN adduser --disabled-password --gecos '' --shell /bin/bash user \
 && chown -R user:user /app \
 && adduser user sudo

RUN echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-user
USER user

# All users can use /home/user as their home directory

ENV HOME=/home/user
ENV SHELL=/bin/bash
SHELL ["/bin/bash", "--login", "-c"]

RUN chmod 777 /home/user

# Install Miniconda
RUN curl -so ~/miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-4.5.11-Linux-x86_64.sh \
 && chmod +x ~/miniconda.sh \
 && ~/miniconda.sh -b -p ~/miniconda \
 && rm ~/miniconda.sh

ENV PATH=/home/user/miniconda/bin:$PATH
ENV CONDA_AUTO_UPDATE_CONDA=false

RUN conda install -y -c pytorch -c fastai fastai \
 && conda install -y flask \
 && conda install -y seaborn \
 && conda install -y scikit-learn \
 && conda clean -ya

# CUDA 9.2-specific steps
#RUN conda install -y -c pytorch \
#    cuda92 \
#    magma-cuda92 \
#    pytorch \
# && conda clean -ya

#RUN conda install -y -c fastai torchvision && conda clean -ya
#RUN conda install -y -c fastai fastai && conda clean -ya

# configure Jupyter Lab
RUN conda install -y -c conda-forge jupyterlab
RUN conda install -y -c conda-forge nodejs
RUN jupyter labextension install @jupyterlab/toc
RUN conda install -y -c conda-forge ipywidgets
RUN pip install jupyterlab_latex
RUN jupyter labextension install @jupyterlab/latex
RUN jupyter labextension install jupyterlab-drawio
RUN jupyter labextension install jupyterlab_bokeh

# Variable inspector for jupyter lab
RUN git clone https://github.com/lckr/jupyterlab-variableInspector \
 && cd jupyterlab-variableInspector \
 && npm install \
 && npm run build \
 && jupyter labextension install . \
 && jupyter labextension list \
 && cd .. && rm -rf jupyterlab-variableInspector \
 && mkdir java-kernel && cd java-kernel \
 && wget https://github.com/SpencerPark/IJava/releases/download/v1.2.0/ijava-1.2.0.zip \
 && unzip ijava-1.2.0.zip \
 && python3 install.py --sys-prefix \
 && cd ..  && rm -rf java-kernel

# Install HDF5 Python bindings

#RUN conda install -y h5py \
# && conda clean -ya
#RUN conda install -y -c haasad eidl7zip \
# && conda clean -ya
#RUN pip install h5py-cache


#RUN pip install kaggle --upgrade \
# && mkdir -p ~/.kaggle/

#COPY kaggle.json /home/user/.kaggle/kaggle.json

COPY .tmux.conf /home/user/

WORKDIR /home/user/
RUN mkdir .jupyter
COPY jupyter_notebook_config.py .jupyter/jupyter_notebook_config.py

EXPOSE 8888
ENTRYPOINT ["jupyter", "lab","--ip=0.0.0.0","--allow-root"]

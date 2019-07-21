FROM nvcr.io/nvidia/pytorch:19.06-py3

LABEL maintainer="Makram Jandar <makramjandar@gmail.com>"

RUN \
    apt-get update && \
    apt-get install -y --allow-downgrades --no-install-recommends \
    python-qt4 \
    openssl \
    libpng-dev &&\
    rm -rf /var/lib/apt/lists/* &&\
    mkdir /fastai
    
WORKDIR /fastai

RUN \ 
    git clone https://github.com/fastai/fastai.git . &&\
    /opt/conda/bin/conda env create &&\
    /opt/conda/bin/conda clean -ya

# Clone course-v3
RUN git clone https://github.com/fastai/course-v3.git

ENV PATH /opt/conda/envs/fastai/bin:$PATH

RUN jupyter notebook --generate-config &&\
    # https authentification
    echo "c.NotebookApp.certfile = u'~/.jupyter/cert.pem'" >> ~/.jupyter/jupyter_notebook_config.py &&\
    echo "c.NotebookApp.keyfile = u'~/.jupyter/pkey.key'" >> ~/.jupyter/jupyter_notebook_config.py &&\
    # Set ip to '*' to bind on all interfaces (ips) for the public server
    echo "c.NotebookApp.ip = '*'" >> ~/.jupyter/jupyter_notebook_config.py &&\
    # password jupyter
    echo "c.NotebookApp.password = u'sha1:13f20fce2676:5f388033b2df5ada9140adb045c06b2d6bb238d2'" >> ~/.jupyter/jupyter_notebook_config.py &&\
    # in-line figure when using Matplotlib
    echo "c.IPKernelApp.pylab = 'inline'" >> ~/.jupyter/jupyter_notebook_config.py &&\
    # No token. But, please, please always use jupyter over ssh tunnel
    echo "c.NotebookApp.token = ''" >> ~/.jupyter/jupyter_notebook_config.py &&\
    # It is a good idea to set a known, fixed port for server access
    echo "c.NotebookApp.port = 9999" >> ~/.jupyter/jupyter_notebook_config.py
        
COPY genCert.sh ~/.jupyter/genCert.sh

CMD ["~/.jupyter/genCert.sh", "jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
FROM nvcr.io/nvidia/pytorch:19.06-py3

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/makramjandar/DataScienceToolkit.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0.0-rc1" \
      maintainer="Makram Jandar <makramjandar@gmail.com>"

RUN apt-get update && \
    apt-get install -y --allow-downgrades --no-install-recommends \
    python-qt4 \
    openssl \
    libpng-dev &&\
    rm -rf /var/lib/apt/lists/* &&\
    mkdir /fastai
    
WORKDIR /fastai

RUN git clone https://github.com/fastai/fastai.git . &&\
    /opt/conda/bin/conda env create &&\
    /opt/conda/bin/conda clean -ya

# Clone FastAI Course-v3
RUN git clone https://github.com/fastai/course-v3.git

ENV PATH /opt/conda/envs/fastai/bin:$PATH

# Set Jupyter config
RUN jupyter notebook --generate-config &&\
    # https authentification
    echo "c.NotebookApp.certfile = u'cert.pem'" >> ~/.jupyter/jupyter_notebook_config.py &&\
    echo "c.NotebookApp.keyfile = u'pkey.key'" >> ~/.jupyter/jupyter_notebook_config.py &&\
    # Set ip to '*' to bind on all interfaces (ips) for the public server
    echo "c.NotebookApp.ip = '*'" >> ~/.jupyter/jupyter_notebook_config.py &&\
    # password jupyter
    echo "c.NotebookApp.password = u'sha1:13f20fce2676:5f388033b2df5ada9140adb045c06b2d6bb238d2'" >> ~/.jupyter/jupyter_notebook_config.py &&\
    # in-line figure when using Matplotlib
    echo "c.IPKernelApp.pylab = 'inline'" >> ~/.jupyter/jupyter_notebook_config.py &&\
    # No token. But, please, please always use jupyter over ssh tunnel
    echo "c.NotebookApp.token = ''" >> ~/.jupyter/jupyter_notebook_config.py &&\
    # It is a good idea to set a known, fixed port for server access
    echo "c.NotebookApp.port = 9999" >> ~/.jupyter/jupyter_notebook_config.py &&\
    # generate certif
    openssl req -newkey rsa:2048 -nodes -keyout ~/.jupyter/pkey.key -x509 -days 36500 -out ~/.jupyter/cert.pem \
    -subj "/C=FR/ST=PARIS/L=Earth/O=Jupyter/OU=IT/CN=www.makramjandar.com/emailAddress=makramjandar@gmail.com"

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]

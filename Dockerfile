FROM jupyter/base-notebook:45bfe5a474fa
# Built from... https://hub.docker.com/r/jupyter/base-notebook/
#               https://github.com/jupyter/docker-stacks/blob/master/base-notebook/Dockerfile
# Built from... https://github.com/jupyterhub/zero-to-jupyterhub-k8s/commit/2aa513d92bc31b45231dadf9bdb28ebd55044c4c
# 
# Built from... Ubuntu 18.04

# VULN_SCAN_TIME=2021-04-13_00:03:33

# The jupyter/docker-stacks images contains jupyterhub, jupyterlab and the
# jupyterlab-hub extension already.

# Example install of git and nbgitpuller.
# NOTE: git is already available in the jupyter/minimal-notebook image.
USER root
RUN apt-get update && apt-get install --yes --no-install-recommends \
    dnsutils \
    git \
    # build-dep python-matplotlib \
    iputils-ping \
 && rm -rf /var/lib/apt/lists/*
USER $NB_USER


RUN conda install matplotlib
COPY tutorial_files.py /srv/tutorial_files.py
COPY git_repo_puller.py /srv/git_repo_puller.py
# COPY NotebookPuller.ipynb NotebookPuller.ipynb
COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install --no-cache-dir \
    -r /tmp/requirements.txt
RUN rmdir ~/work/

# Support overriding a package or two through passed docker --build-args.
# ARG PIP_OVERRIDES="jupyterhub==1.3.0"
ARG PIP_OVERRIDES=
RUN if [[ -n "$PIP_OVERRIDES" ]]; then \
        pip install --no-cache-dir $PIP_OVERRIDES; \
    fi

RUN jupyter serverextension enable --py nbgitpuller --sys-prefix

# Uncomment the line below to make nbgitpuller default to start up in JupyterLab
#ENV NBGITPULLER_APP=lab

# conda/pip/apt install additional packages here, if desired.

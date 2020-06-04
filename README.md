# Single User Server

This is the notebook server that is started when someone visits jupyter.demo.globus.org.

Everything here is automatically built using a separate build repo here: 
https://hub.docker.com/repository/docker/nsglobusautobuilds/single-user-server

The nsglobusautobuilds is used to to the extensive permissions required by dockerhub in
order to use automatic builds (Read and write access to everything public and private).

This extends the original single user server listed here:
https://github.com/jupyterhub/zero-to-jupyterhub-k8s/tree/master/images/singleuser-sample

The image here probably lags behind on the most stable version. We also add some Globus
specific features, such as ensuring the latest Globus tools are installed and can be run
with the Globus Tutorial Notebooks:

https://github.com/globus/globus-jupyter-notebooks 

### Remote files

This image depends on remote files in a couple different locations, both on S3 and
Github. S3 contains the manifest of files to fetch, which lists the Github repos to
clone. It's intended this notebook server is configured not to have persistent storage,
and that all storage will be wiped when the server is shut down.

* Notebook Puller -- https://s3.us-east-2.amazonaws.com/globusworldk8.nick.globuscs.info/NotebookPuller.ipynb
* File/Repo Manifest -- https://s3.us-east-2.amazonaws.com/globusworldk8.nick.globuscs.info/gwmanifest.json


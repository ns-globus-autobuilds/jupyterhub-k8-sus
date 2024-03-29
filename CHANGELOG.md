# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [1.1.4](https://github.com/ns-globus-autobuilds/jupyterhub-k8-sus/compare/v1.1.2...v1.1.4) (2021-08-16)


### Bug Fixes

* Patched notebook vulnerability and fixed docker build ([cc34552](https://github.com/ns-globus-autobuilds/jupyterhub-k8-sus/commit/cc34552a83142a176793ad1fd1b092fdadb44794))

### 1.1.2 -- May 10th 2021

* Brought back old tools for pulling notebooks
* Updated git_repo_puller.py to be a bit more flexible
    * This is needed due to networking issues with AWS Calico

### 1.1.1 -- May 6th 2021

* Added git_repo_puller.py for pulling multiple repos
    * Script is also more robust, does not error on first time run like nbpuller


### 1.1.0 -- Apr 26th 2021

* Dist upgrade to Jupyterhub 1.11.0 image
* Added globus automate client
* Added globus search cli


### 1.0.2 -- Oct 12th 2020

* Test autobuilds with tag version

### 1.0.1 -- Oct 9th 2020

* Add minid
* Update image
* (Note: image is still a very old version of the jupyter image) 

### 1.0.0 -- June 4th 2020

* Move from rpwagnerbuilds

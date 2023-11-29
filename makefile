## makefile automates the build and deployment for python projects

PROJ_TYPE =		python
PROJ_MODULES =		git python-resources python-cli python-doc python-doc-deploy

include ./zenbuild/main.mk

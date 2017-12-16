#!/bin/bash

sudo apt-get -y install \
	python3 \
	python-pip \
	python-dev \
	build-essential \
	python-virtualenv \
	screen \
	git \
	vim \

virtualenv jupyter
. jupyter/bin/activate
pip install --upgrade pip
pip install \
	jupyter \
	coconut \

coconut --jupyter

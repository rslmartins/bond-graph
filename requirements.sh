#!/bin/bash

apt-get update && apt-get install -y gfortran \
	libblas-dev \
	liblapack-dev \
	build-essential \
	cmake \
	texlive \
	cm-super \
	texlive-latex-extra \
	dvipng 

git clone https://github.com/LLNL/sundials.git; \
	mkdir ./sundials/build;\
	cd ./sundials/build; \
	cmake -DLAPACK_ENABLE=ON ..; \
	make && make install ; \
	cd ../../

pip3 install -r ./requirements.txt

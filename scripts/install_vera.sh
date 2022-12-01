#!/bin/bash

git clone https://github.com/Epitech/banana-vera.git
cd banana-vera
cmake . -DVERA_LUA=OFF -DPANDOC=OFF -DVERA_USE_SYSTEM_BOOST=ON

make -j
sudo make install

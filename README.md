Diploma work
==============

Bachelor's diploma work at FPMI, BSU

* [Getting Started](#getting-started)

Getting Started
---------------
Documentation are available in the
[docs](https://github.com/Ashes17b/DW/tree/master/docs).

We recommend building on Ubuntu 16.04 LTS (64-bit) 

**Build Dependencies:**

    sudo apt-get update
    sudo apt-get install autoconf cmake make automake libtool git libboost-all-dev libssl-dev g++ libcurl4-openssl-dev conan


**Build Script:**

    git clone https://github.com/Ashes17b/DW.git
    cd DW
    git checkout master
    git submodule update --init --recursive -f
    cd src/bitshares-core/
    mkdir build
    cd build/
    conan install ..
    cmake -DCMAKE_BUILD_TYPE=Release ..
    make -j{i} # Where i is the number of threads

**Upgrade Script:** (prepend to the Build Script above if you built a prior release):

    git remote set-url origin https://github.com/Ashes17b/DW.git
    git checkout master
    git remote set-head origin --auto
    git pull
    git submodule update --init --recursive -f # this command may fail
    git submodule sync --recursive
    git submodule update --init --recursive -f

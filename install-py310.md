## How to install

1. Extract the downloaded archive

```
tar -xf Python-3.10.13.tgz
```

2. Navigate to the Python source directory
```
cd Python-3.10.13
```
3. Configure the build
```
./configure --enable-optimizations
```
4. Build and install Python
```
make -j$(nproc)
sudo make altinstall
```
5. Verify the installation
```
python3.10 --version
```

6. Cleanup (optional)
```
cd ..
rm -rf Python-3.10.13
rm Python-3.10.13.tgz
```

7. install gcc (optional) previously ver 11.4
```shell
# extract files
tar -xvf gcc-9.3.0.tar.gz

# gmp-6.1.0
tar -xvf gmp-6.1.0.tar.xz
mv gmp-6.1.0 gcc-9.3.0/gmp

# mpfr-3.1.4
tar -xvf mpfr-3.1.4.tar.gz
mv mpfr-3.1.4 gcc-9.3.0/mpfr

# mpc-1.0.3
tar -xvf mpc-1.0.3.tar.gz
mv mpc-1.0.3 gcc-9.3.0/mpc

# make a build folder
cd gcc-9.3.0

mkdir gcc-build
cd gcc-build
../configure --prefix=/usr/local/gcc-9.3.0 --disable-multilib --enable-languages=c,c++

# start compile it 
make -j $(nproc)
make install -j $(nproc)

# update config file
ln -s /usr/local/gcc-9.3.0 /usr/local/gcc
export PATH=/usr/local/gcc/bin:$PATH
#export LD_LIBRARY_PATH=/usr/local/gcc/lib64
#export MANPATH=/usr/local/gcc/share/man:$MANPATH

# check version
gcc -v

```
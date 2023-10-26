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
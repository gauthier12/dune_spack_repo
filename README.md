# Dune Spack repository
## Installation
Clone spack git
```
git clone https://github.com/spack/spack.git
source ./share/spack/setup-env.sh
spack bootstrap
```
add dune spack repo
```
cd $HOME
git clone https://github.com/gauthier12/dune_spack_repo.git
spack repo add dune_spack_repo
```
Install dune modules
```
spack install dune-python
```
## Use a module
To use dune-python, load the module
```
source $SPACK_ROOT/share/spack/setup-env.sh
spack load dune-python
```

## Build a new module
### Initialize developement environment 
```
source $SPACK_ROOT/share/spack/setup-env.sh
spack install --only=dependencies dune-newmodule
spack build-env dune-newmodule $SHELL
```
### Initialize dune project
```
export DUNE_CONTROL_PATH=$SPACK_ROOT/opt/spack/linux-archrolling-sandybridge/gcc-9.2.0/
duneproject
```
Answer the questions about the new modules, enter the project folder and compile with standard cmake
```
mkdir build
cd build 
cmake ..
cmake --build .
```

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
Install dune with desired modules
```
spack install dune+desired+modules+.....
```
by example
```
spack install dune+uggrid+grid+functions
```
modules dependencies wil be automatically downloaded and added

## Use 
To use dune, load the module
```
source /PATH/TO/SPACK/share/spack/setup-env.sh
spack load dune
```
if python module was installed, python binding are avalaible after loading the module

## Build a new module
### Load the dune module
```
source /PATH/TO/SPACK/share/spack/setup-env.sh
spack load dune
```
### Initialize dune project
```
duneproject
```
Answer the questions about the new modules, enter the project folder and compile with standard cmake
```
mkdir build
cd build 
cmake ..
cmake --build .
```

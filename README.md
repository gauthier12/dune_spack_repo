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
## Use
To use dune-python, load the module
```
source $SPACK_ROOT/share/spack/setup-env.sh
spack load dune-python
```

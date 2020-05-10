# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install dune
#
# You can edit this file again by typing:
#
#     spack edit dune
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import os
from spack import *


class Dune(CMakePackage):
    """
    DUNE, the Distributed and Unified Numerics Environment is a modular toolbox for solving partial differential equations (PDEs) with grid-based methods.
    """

    homepage = "https://www.dune-project.org"
    url      = "https://www.dune-project.org/download/2.7.0/dune-common-2.7.0.tar.gz"
    list_url = "https://www.dune-project.org/download/"
    list_depth = 1
    
    python_components = [ 'dune' ]


    version('2.7.0', sha256='3c83c583a45325513113148cb94bd978e601907a6591c765f6253342e00f1890', expand=False)

    variant('2d', default=True, description='Build library for 2d')
    variant('3d', default=True, description='Build library for 3d')
    variant('alberta', default=False, description='Build with Alberta support')
    variant('amiramesh', default=False, description='Build with AmiraMesh support')
    variant('arpack', default=True, description='Build ARnoldi PACKage library support')
    variant('blas',   default=True, description='Build with BLAS support')
    variant('doxygen', default=True, description='Create Doxygen documentation')
    variant('extrautils', default=True, description='Enable compilation and installation of extra utilities from the src subdirectory')
    variant('fempy', default=False, description='Support of dune-fempy module')
    variant('gmp', default=True, description='Build with GNU multi-precision library support')
    variant('imagemagick', default=False, description='Imagemagick support')
    variant('jupyter', default=False, description='Build with Jupyter support')
    variant('lapack', default=True, description='Build with LAPACK support')
    variant('metis', default=True, description='Build with METIS library support')
    variant('mkl', default=True, description='Build with Math Kernel library support')
    variant('tbb', default=True, description='Build with Threading Building Blocks library support')
    variant('oldcategory', default=True, description='Enable/Disable the backwards compatibility of the category enum/method in dune-istl solvers, preconditioner, etc.')
    variant('parmetis', default=True, description='Build with ParMETIS support')
    variant('psurface', default=False, description='Build with Psurface support')
    variant('ptscotch', default=True, description='Build with PT-Scotch support')
    variant('selector', default=True, description='Grid selector definition added to config.h')
    variant('shared', default=True, description='Enables the build of shared libraries.')
    variant('sionlib', default=False, description='Build with SIONlib support')
    variant('sphinx', default=True, description='Create Sphinx documentation')
    variant('suitesparse', default=True, description='Build SuiteSparse library support')
    variant('superlu', default=True, description='Build Supernodal LU library support')
    variant('threads', default=True, description='Activate pThread support')
    variant('vc', default=True, description='Build C++ Vectorization library support')
    variant('zlib', default=True, description='Build zlib library support')
    variant('zoltan', default=True, description='Build with Zoltan support')


    variant('alugrid', default=False, description='Build with dune-alugrid module')
    variant('corepy', default=False, description='Build with dune-corepy module')
    variant('functions', default=False, description='Build with dune-functions module')
    variant('geometry', default=False, description='Build with dune-geometry module')
    variant('grid', default=False, description='Build with dune-grid module')
    variant('istl', default=False, description='Build with dune-istl module')
    variant('localfunctions', default=False, description='Build with dune-localfunctions module')
    variant('python', default=False, description='Build with Python and dune-python')
    variant('spgrid', default=False, description='Build with dune-spgrid module')
    variant('typetree', default=False, description='Build with dune-typetree module')
    variant('uggrid', default=False, description='Build with dune-uggrid module')

#Dune common module
    resource(
       name='dune-common',
       git='https://gitlab.dune-project.org/core/dune-common.git',
       branch='releases/2.7',
       )
#Dune geometry module
    resource(
       name='dune-geometry',
       git='https://gitlab.dune-project.org/core/dune-geometry.git',
       branch='releases/2.7',
       when='+geometry')

#Dune grid module
    resource(
       name='dune-grid',
       git='https://gitlab.dune-project.org/core/dune-grid.git',
       branch='releases/2.7',
       when='+grid')

#Dune uggrid module
    resource(
       name='dune-uggrid',
       git='https://gitlab.dune-project.org/staging/dune-uggrid.git',
       branch='releases/2.7',
       when='+uggrid')

#Dune istl module
    resource(
       name='dune-istl',
       git='https://gitlab.dune-project.org/core/dune-istl.git',
       branch='releases/2.7',
       when='+istl')

#Dune localfunctions module
    resource(
       name='dune-localfunctions',
       git='https://gitlab.dune-project.org/core/dune-localfunctions.git',
       branch='releases/2.7',
       when='+localfunctions')

#Dune functions module
    resource(
       name='dune-functions',
       git='https://gitlab.dune-project.org/staging/dune-functions.git',
       branch='releases/2.7',
       when='+functions')

#Dune module
    resource(
       name='dune-python',
       git='https://gitlab.dune-project.org/staging/dune-python.git',
       branch='releases/2.7',
       when='+python')
#Dune module
    resource(
       name='dune-typetree',
       git='https://gitlab.dune-project.org/staging/dune-typetree.git',
       branch='releases/2.7',
       when='+typetree')
#Dune module
    resource(
       name='dune-alugrid',
       git='https://gitlab.dune-project.org/extensions/dune-alugrid.git',
       branch='releases/2.7',
       when='+alugrid')

#Dependence between modules
    module_dependencies={"dune-common":[]}
    module_dependencies["dune-geometry"]=["dune-common"]
    module_dependencies["dune-grid"]=["dune-common","dune-geometry"]
    module_dependencies["dune-uggrid"]=["dune-common"]
    module_dependencies["dune-istl"]=["dune-common"]
    module_dependencies["dune-localfunctions"]=["dune-common","dune-geometry"]
    module_dependencies["dune-functions"]=["dune-grid","dune-typetree","dune-localfunctions","dune-istl"]
    module_dependencies["dune-typetree"]=["dune-common"]
    module_dependencies["dune-python"]=[]
    module_dependencies["dune-alugrid"]=["dune-grid","dune-geometry","dune-common"]

    def build_module_list(self,module_list,name):
        if name in self.module_dependencies.keys():
            for dep in self.module_dependencies[name]:
                self.build_module_list(module_list,dep)
            module_list.append(name)
        return

    extends('python')
    #option
    depends_on('cmake@3.1:', type='build')
    depends_on('mpi')
    depends_on('blas',   when='+blas')
    depends_on('lapack', when='+lapack')
    depends_on('doxygen', type='build', when='+doxygen')
    depends_on('gmp', when='+gmp')
    depends_on('intel-tbb', when='+tbb')
    depends_on('intel-mkl', when='+mkl')
    depends_on('python@3.0:', type=('build', 'run'), when='+python')
    depends_on('py-setuptools', type='build')
    depends_on('py-jupyter', type=('build', 'run'), when='+jupyter')
    depends_on('py-numpy', type=('build', 'run'), when='+python')
    depends_on('py-pip', type=('build', 'run'), when='+python')
    depends_on('py-sphinx', type=('build', 'run'), when='+sphinx')
    depends_on('vc', when='+vc')
    depends_on('pkg-config', type='build')
    depends_on('imagemagick', type='build', when='+imagemagick')
    depends_on('metis', when='+metis')
    depends_on('parmetis', when='+parmetis')
    depends_on('arpack-ng', when='+arpack')
    depends_on('suite-sparse', when='+suitesparse')
    depends_on('superlu', when='+superlu')
    depends_on('alberta', when='+alberta')
    depends_on('psurface', when='+psurface')
    depends_on('amiramesh', when='+amiramesh')
    depends_on('sionlib', when='+sionlib')
    depends_on('zlib', when='+zlib')
    depends_on('scotch+mpi', when='+ptscotch')
    depends_on('zoltan', when='+zoltan')


    def url_for_version(self, version):
        url = "https://www.dune-project.org/download/{1}/dune-common-{1}.tar.gz"
        return url.format(version.up_to(2), version)

    def cmake_args(self):
        """Populate cmake arguments."""
        spec = self.spec
        def variant_bool(feature, on='ON', off='OFF'):
            """Ternary for spec variant to ON/OFF string"""
            if feature in spec:
                return on
            return off 

        def nvariant_bool(feature):
            """Negated ternary for spec variant to OFF/ON string"""
            return variant_bool(feature, on='OFF', off='ON')

        cmake_args = [ 
#            '-DDUNE_BUILD_BOTH_LIBS=%s' % variant_bool('+shared'),
            '-DBUILD_SHARED_LIBS:BOOL=%s' % variant_bool('+shared'),
            '-DDUNE_GRID_EXTRA_UTILS:BOOL=%s' % variant_bool('+extrautils'),
            '-DDUNE_GRID_GRIDTYPE_SELECTOR:BOOL=%s' % variant_bool('+selector'),
            '-DDUNE_ISTL_SUPPORT_OLD_CATEGORY=%s' % variant_bool('+oldcategory'),
            '-DUSE_PTHREADS:BOOL=%s' % variant_bool('+threads'),
        ]
        #self.define_from_variant('DETECT_HDF5', 'hdf5'),
        if '+python' in spec:
            cmake_args.append('-DDUNE_GRID_EXPERIMENTAL_GRID_EXTENSIONS:BOOL=TRUE')
            cmake_args.append('-DPYTHON_INSTALL_LOCATION:STRING="system"')

        return cmake_args

    def _get_needed_resources(self):
#        for variant, resource_list in self.resources.items():
        resources = []
        # Select the resources that are needed for this build
        if self.spec.concrete:
            module_list=[]
            for when_spec, resource_list in self.resources.items():
                if when_spec in self.spec:
                    for res in resource_list:
                        dune_module=res.name
                        self.build_module_list(module_list,dune_module)
#                    resources.extend(resource_list)
            module_list = list(dict.fromkeys(module_list))
            for when_spec, resource_list in self.resources.items():
                for res in resource_list:
                    if(res.name in module_list):
                        resources.extend(resource_list)
        else:
            for when_spec, resource_list in self.resources.items():
                # Note that variant checking is always strict for specs where
                # the name is not specified. But with strict variant checking,
                # only variants mentioned in 'other' are checked. Here we only
                # want to make sure that no constraints in when_spec
                # conflict with the spec, so we need to invoke
                # when_spec.satisfies(self.spec) vs.
                # self.spec.satisfies(when_spec)
                if when_spec.satisfies(self.spec, strict=False):
                    resources.extend(resource_list)
        # Sorts the resources by the length of the string representing their
        # destination. Since any nested resource must contain another
        # resource's name in its path, it seems that should work
        resources = sorted(resources, key=lambda res: len(res.destination))
        return resources

    def cmake(self, spec, prefix):
        os.remove(self.stage.archive_file)
        optFile = open(self.stage.source_path+"/../dune.opts", "w")
        optFile.write('CMAKE_FLAGS="')
        for flag in self.cmake_args():
            optFile.write(flag.replace("\"", "'")+" ")
        optFile.write('-DCMAKE_INSTALL_PREFIX=%s' % prefix)
        optFile.write('"')
        optFile.close()
        set_executable('dune-common/bin/dunecontrol')
        installer = Executable('dune-common/bin/dunecontrol')
        options_file=self.stage.source_path+"/../dune.opts"
        installer('--builddir=%s'%self.build_directory ,  '--opts=%s' % options_file, 'cmake')
        pass

    def install(self, spec, prefix):
        set_executable('dune-common/bin/dunecontrol')
        installer = Executable('dune-common/bin/dunecontrol')
        options_file=self.stage.source_path+"/../dune.opts"
        installer('--builddir=%s'%self.build_directory ,  '--opts=%s' % options_file, 'make', 'install')
        pass

    def build(self, spec, prefix):
        set_executable('dune-common/bin/dunecontrol')
        installer = Executable('dune-common/bin/dunecontrol')
        options_file=self.stage.source_path+"/../dune.opts"
        installer('--builddir=%s'%self.build_directory ,  '--opts=%s' % options_file, 'make')
        pass

    @run_after('install')
    def install_python_components(self):
        if '+python' in self.spec:
            for package in self.python_components:
                build_directory = 'dune-python/python'
                with working_dir(join_path(self.build_directory,'dune-python/python')):
                    setup_py('install', '--prefix={0}'.format(self.prefix))

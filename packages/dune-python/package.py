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
#     spack install dune-python
#
# You can edit this file again by typing:
#
#     spack edit dune-python
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os


class DunePython(CMakePackage):
    """
    Python bindings for the DUNE core modules
    """

    homepage = "https://www.dune-project.org"
#    url      = "https://www.dune-project.org/download/2.6.0/dune-python-2.6.0.tar.gz"
    url = 'https://gitlab.dune-project.org/staging/dune-python/-/archive/releases/2.7/dune-python-releases-2.7.tar.gz'
    list_url = 'https://gitlab.dune-project.org/staging/dune-python/-/archive/releases/'
#    list_url = "https://www.dune-project.org/download/"
    list_depth = 1
#    version('2.7.0', url = 'https://gitlab.dune-project.org/staging/dune-python/-/archive/releases/2.7/dune-python-releases-2.7.tar.gz')

    python_components = [ 'dune' ]

    version('2.7', sha256='432564c8577f5d3c9e9d6b2b3710189fd3ac9551eac61986f5966d2fa2534c46')
    version('2.6', sha256='cc9e9222de850eea659680e41a824bb5d7b300d0e89a8c0855f8d0a31f01ff2d')


    #option
#   ugggrid seems to be a requirement (does not link without)
#    variant('uggrid', default=False, description='Build with dune-uggrid support')

    variant('functions', default=False, description='Build with dune-functions support')
    variant('blas',   default=True, description='Build with BLAS support')
    variant('lapack', default=True, description='Build with LAPACK support')
    variant('gmp', default=True, description='Build with GNU multi-precision library support')
    variant('tbb', default=True, description='Build with Threading Building Blocks library support')
    variant('mkl', default=True, description='Build with Math Kernel library support')
    variant('doxygen', default=True, description='Create Doxygen documentation')
    variant('sphinx', default=True, description='Create Sphinx documentation')
    variant('vc', default=True, description='Build C++ Vectorization library support')
    variant('imagemagick', default=False, description='Imagemagick support')
    variant('metis', default=True, description='Build METIS library support')
    variant('parmetis', default=True, description='Build ParMETIS library support')
    variant('arpack', default=True, description='Build ARnoldi PACKage library support')
    variant('suitesparse', default=True, description='Build SuiteSparse library support')
    variant('superlu', default=True, description='Build Supernodal LU library support')
    variant('alberta', default=False, description='Build with Alberta support')
    variant('psurface', default=False, description='Build with Psurface support')
    variant('amiramesh', default=False, description='Build with AmiraMesh support')
    variant('jupyter', default=False, description='Build with Jupyter support')
    variant('extrautils', default=True, description='Enable compilation and installation of extra utilities from the src subdirectory')
    variant('selector', default=True, description='Grid selector definition added to config.h')
    variant('oldcategory', default=True, description='Enable/Disable the backwards compatibility of the category enum/method in dune-istl solvers, preconditioner, etc.')
    variant('threads', default=True, description='Activate pThread support')
    variant('shared', default=True, description='Enables the build of shared libraries.')
    variant('localfunctions', default=False, description='Support of dune-localfunctions module')
    variant('functions', default=False, description='Support of dune-functions module')
    variant('alugrid', default=False, description='Support of dune-alugrid module')
    variant('fempy', default=False, description='Support of dune-fempy module')
    variant('spgrid', default=False, description='Support of dune-spgrid module')
    variant('typetree', default=False, description='Support of dune-typetree module')

    extends('python')

    #dependencies 
    depends_on('dune-grid+python+shared')
    depends_on('dune-istl+python+shared')
    depends_on('dune-geometry+python+shared')
#    depends_on('dune-uggrid', when='+uggrid')
    depends_on('dune-uggrid+python+shared')
    depends_on('dune-common+python+shared')
    depends_on('dune-localfunctions+python+shared', when='+localfunctions')
    depends_on('dune-functions+python+shared', when='+functions')
    depends_on('dune-alugrid+python+shared', when='+alugrid')
    depends_on('dune-fempy+python+shared', when='+fempy')
    depends_on('dune-spgrid+python+shared', when='+spgrid')
    depends_on('dune-typetree+python+shared', when='+typetree')
    depends_on('cmake@3.1:', type='build')
    depends_on('mpi')
    depends_on('blas',   when='+blas')
    depends_on('lapack', when='+lapack')
    depends_on('doxygen', type='build', when='+doxygen')
    depends_on('gmp', when='+gmp')
    depends_on('intel-tbb', when='+tbb')
    depends_on('intel-mkl', when='+mkl')
    depends_on('python@3.8.2:')
    depends_on('py-setuptools', type='build')
    depends_on('py-numpy')
    depends_on('py-pip')
    depends_on('py-sphinx', type='build', when='+sphinx')
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
    depends_on('py-jupyter', when='+jupyter')

    def url_for_version(self, version):
        url = 'https://gitlab.dune-project.org/staging/dune-python/-/archive/releases/{1}/dune-python-releases-{1}.tar.gz'
        return url.format(version.up_to(2), version)

    patch('AddQuadMathFlags.cmake.patch')
    patch('FindQuadMath.cmake.patch')

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
#        if 'python' in spec:
#            cmake_args.append('-DPYTHON_INSTALL_LOCATION:STRING="system"')

        return cmake_args

    @run_after('install')
    def install_python_components(self):
        for package in self.python_components:
            print(os.path.dirname(os.path.abspath(__file__)))
            build_directory = 'python'
            print(self)
            with working_dir(join_path(self.build_directory,'python')):
                print(working_dir)
                print(os.path.dirname(os.path.abspath(__file__)))
                print(join_path(self.build_directory,'python'))
                setup_py('install', '--prefix={0}'.format(self.prefix))

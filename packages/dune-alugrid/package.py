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
#     spack install dune-alugrid
#
# You can edit this file again by typing:
#
#     spack edit dune-alugrid
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class DuneAlugrid(CMakePackage):
    """ALUGrid is an adaptive, loadbalancing, unstructured implementation of the DUNE grid interface supporting either simplices or cubes."""

    homepage = "https://www.dune-project.org"
    url      = "https://github.com/dune-mirrors/dune-alugrid/archive/v2.6.0.tar.gz"

    version('2.6.0',    sha256='25fa4a5127837a0def2f93ae7fda38c5098dd066536236533015755ad264a870')
    version('2.4.0',    sha256='fd0fab5b2c6e1e0c9f792947dad1f9c2e2d6b65242935474017e0c278bab3ae1')

    #option
    variant('blas',   default=True, description='Build with BLAS support')
    variant('lapack', default=True, description='Build with LAPACK support')
    variant('gmp', default=True, description='Build with GNU multi-precision library support')
    variant('tbb', default=True, description='Build with Threading Building Blocks library support')
    variant('mkl', default=True, description='Build with Math Kernel library support')
    variant('doxygen', default=True, description='Create Doxygen documentation')
    variant('sphinx', default=True, description='Create Sphinx documentation')
    variant('python', default=False, description='Build with Python and dune-python')
    variant('vc', default=True, description='Build C++ Vectorization library support')
    variant('zlib', default=True, description='Build zlib library support')
    variant('imagemagick', default=False, description='Imagemagick support')
    variant('corepy', default=False, description='Build with dune-corepy support')
    variant('uggrid', default=False, description='Build with dune-uggrid support')
    variant('ptscotch', default=True, description='Build with PT-Scotch support')
    variant('metis', default=True, description='Build with METIS support')
    variant('parmetis', default=True, description='Build with ParMETIS support')
    variant('alberta', default=False, description='Build with Alberta support')
    variant('psurface', default=False, description='Build with Psurface support')
    variant('amiramesh', default=False, description='Build with AmiraMesh support')
    variant('sionlib', default=False, description='Build with SIONlib support')
    variant('zoltan', default=True, description='Build with Zoltan support')
    variant('threads', default=True, description='Whether we are using pthreads')
    variant('extrautils', default=True, description='Enable compilation and installation of extra utilities from the src subdirectory')
    variant('selector', default=True, description='Grid selector definition added to config.h')
    variant('shared', default=False, description='Enables the build of shared libraries.')

    #dependencies 
    depends_on('dune-common')
    depends_on('dune-geometry')
    depends_on('dune-grid')
    depends_on('dune-corepy', when='+corepy')
    depends_on('dune-python', when='+python')
    depends_on('dune-uggrid', when='+uggrid')
    depends_on('cmake@3.1:', type='build')
    depends_on('mpi')
    depends_on('blas',   when='+blas')
    depends_on('lapack', when='+lapack')
    depends_on('doxygen', type='build', when='+doxygen')
    depends_on('gmp', when='+gmp')
    depends_on('intel-tbb', when='+tbb')
    depends_on('intel-mkl', when='+mkl')
    depends_on('python@3.0:')
    depends_on('py-sphinx', type='build', when='+sphinx')
    depends_on('vc', when='+vc')
    depends_on('zlib', when='+zlib')
    depends_on('scotch+mpi', when='+ptscotch')
    depends_on('zoltan', when='+zoltan')
    depends_on('metis', when='+metis')
    depends_on('parmetis', when='+parmetis')
    depends_on('pkg-config', type='build')
    depends_on('imagemagick', type='build', when='+imagemagick')
    depends_on('alberta', when='+alberta')
    depends_on('psurface', when='+psurface')
    depends_on('amiramesh', when='+amiramesh')
    depends_on('sionlib', when='+sionlib')

    patch('AddQuadMathFlags.cmake.patch', when='@2.6')
    patch('FindQuadMath.cmake.patch', when='@2.6')

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
            '-DUSE_PTHREADS:BOOL=%s' % variant_bool('+threads'),
        ]
        if 'python' in spec:
            cmake_args.append('-DDUNE_GRID_EXPERIMENTAL_GRID_EXTENSIONS:BOOL=TRUE')
            cmake_args.append('-DPYTHON_INSTALL_LOCATION:STRING="system"')

        return cmake_args


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
#     spack install dune-uggrid
#
# You can edit this file again by typing:
#
#     spack edit dune-uggrid
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class DuneUggrid(CMakePackage):
    """
    dune-uggrid is a fork of the old UG finite element software, wrapped
    as a Dune module, and stripped of everything but the grid data
    structure.
    You need this module if you want to use the UGGrid grid
    implementation from dune-grid.
    """

    homepage = "https://www.dune-project.org"
    url      = "https://github.com/dune-mirrors/dune-uggrid/archive/v2.6.0.tar.gz"

    version('2.7.0',    sha256='bcf4afd386f23cdb7f7ba16cc2fec4918c4afb516761ef7905af8378ea86eb4c')
    version('2.6.0',    sha256='3da75c672c151ca711526f2c0619d6f1ebf8f489c972066ee3b43252ea8daed4')
    version('2.5.2',    sha256='3a484376e625fff880ff9db6be53ccca0080c5ce7229ed31c09e09fa4a4a4afa')
    version('2.5.1',    sha256='55ccb3a4b4aad0c22c2cda6fa2b50325caf5c4493a9e033562fc03cf5a3b3f61')
    version('2.5.0',    sha256='b7f5ac061b6d5f30e22a2acfff205a3fc4751f57f1e301db83c66da2b9105bc9')

    #option
    variant('blas',   default=True, description='Build with BLAS support')
    variant('lapack', default=True, description='Build with LAPACK support')
    variant('gmp', default=True, description='Build with GNU multi-precision library support')
    variant('tbb', default=True, description='Build with Threading Building Blocks library support')
    variant('mkl', default=True, description='Build with Math Kernel library support')
    variant('doxygen', default=True, description='Create Doxygen documentation')
    variant('sphinx', default=True, description='Create Sphinx documentation')
    variant('vc', default=True, description='Build C++ Vectorization library support')
    variant('imagemagick', default=False, description='Imagemagick support')
    variant('2d', default=True, description='Build library for 2d')
    variant('3d', default=True, description='Build library for 3d')
    variant('threads', default=True, description='Activate pThread support')
    variant('shared', default=True, description='Enables the build of shared libraries.')
    variant('python', default=True, description='Build with Python')
    variant('extrautils', default=True, description='Enable compilation and installation of extra utilities from the src subdirectory')
    variant('selector', default=True, description='Grid selector definition added to config.h')

    #dependencies 
    depends_on('dune-common')
    depends_on('cmake@3.1:', type='build')
    depends_on('cmake@2.8.12:', when='@2.6', type='build')
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
    depends_on('pkg-config', type='build')
    depends_on('imagemagick', type='build', when='+imagemagick')

    patch('parallel_CMakeList.patch', when='@2.6')
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
            '-DUSE_PTHREADS:BOOL=%s' % variant_bool('+threads'),
        ]
        if 'python' in spec:
            cmake_args.append('-DPYTHON_INSTALL_LOCATION:STRING="system"')
        if self.spec.variants['build_type'].value == 'Debug':
            cmake_args.append('UG_ENABLE_DEBUGGING:BOOL=True')
        cmake_args.append('-DUG_ENABLE_2D:BOOL=%s' % variant_bool('+2d'))
        cmake_args.append('-DUG_ENABLE_3D:BOOL=%s' % variant_bool('+3d'))

        return cmake_args

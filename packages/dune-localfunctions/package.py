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
#     spack install dune-localfunctions
#
# You can edit this file again by typing:
#
#     spack edit dune-localfunctions
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class DuneLocalfunctions(CMakePackage):
    """
    dune-localfunctions provides interface and implementation for shape
    functions defined on the DUNE reference elements. In addition to the
    shape function, interpolation operators and special keys are
    provided which can be used to assemble global function spaces on
    finite-element grids.
    """

    homepage = "https://www.dune-project.org"
    url      = "https://www.dune-project.org/download/2.7.0/dune-localfunctions-2.7.0.tar.gz"
    list_url = "https://www.dune-project.org/download/"
    list_depth = 1

    version('2.7.0', sha256='0dbb8e559cc9ca3a506116fc49648c990a40e3162cf4659289f1d96d602a30fa')
    version('2.6.0', sha256='14664b007fbc5e3592740075d2aeca6890e6e185f9924da044fe726ea3fc86a5')
    version('2.5.2', sha256='7253fb9186f73bf58d49ecaee22cccd4ad197eff09b07955568307f0cc946958')
    version('2.5.1', sha256='4308d45132f463ca6c37cf59f0ef52b30b13dc01afba782c467e7ed6511dd0c0')
    version('2.5.0', sha256='d92e05fbfcb10750aba0597eca1c43c3842a657bb53ab7f25c33c1e24cc654ea')
    version('2.4.2', sha256='652dea9a47934be62f8c3777a7fda5c1e2d2b2fead5777d180f467acf8472a31')
    version('2.4.1', sha256='569cd4839564f4d419e52a51873c3e2b153f9656d77a37e0b5fb22f15423399f')
    version('2.4.0', sha256='5edb297ac26901232dd0cb2899a56d562192abe1cc6ac79efec57818359112e3')

    #option
    variant('blas',   default=True, description='Build with BLAS support')
    variant('lapack', default=True, description='Build with LAPACK support')
    variant('gmp', default=True, description='Build with GNU multi-precision library support')
    variant('tbb', default=True, description='Build with Threading Building Blocks library support')
    variant('mkl', default=True, description='Build with Threading Building Blocks library support')
    variant('doxygen', default=True, description='Create Doxygen documentation')
    variant('sphinx', default=True, description='Create Sphinx documentation')
    variant('vc', default=True, description='Build C++ Vectorization library support')
    variant('imagemagick', default=False, description='Imagemagick support')
    variant('threads', default=True, description='Activate pThread support')
    variant('shared', default=False, description='Enables the build of shared libraries.')
    variant('python', default=True, description='Build with Python')
    variant('extrautils', default=True, description='Enable compilation and installation of extra utilities from the src subdirectory')
    variant('selector', default=True, description='Grid selector definition added to config.h')

    #dependencies 
    depends_on('dune-common')
    depends_on('dune-geometry')
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
    depends_on('pkg-config', type='build')
    depends_on('imagemagick', type='build', when='+imagemagick')

    patch('AddQuadMathFlags.cmake.patch', when='@2.6')
    patch('FindQuadMath.cmake.patch', when='@2.6')


    def url_for_version(self, version):
        url = "https://www.dune-project.org/download/{1}/dune-localfunctions-{1}.tar.gz"
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
            '-DUSE_PTHREADS:BOOL=%s' % variant_bool('+threads'),
        ]
        if 'python' in spec:
            cmake_args.append('-DDUNE_GRID_EXPERIMENTAL_GRID_EXTENSIONS:BOOL=TRUE')
            cmake_args.append('-DPYTHON_INSTALL_LOCATION:STRING="system"')

        return cmake_args

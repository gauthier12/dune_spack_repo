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
#     spack install dune-geometry
#
# You can edit this file again by typing:
#
#     spack edit dune-geometry
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class DuneGeometry(CMakePackage):
    """
    dune-geometry includes everything related to the DUNE reference
    elements. This includes the reference elements themselves, mappings
    on the reference elements (geometries), and quadratures.
    """

    homepage = "https://www.dune-project.org"
    url      = "https://www.dune-project.org/download/2.7.0/dune-geometry-2.7.0.tar.gz"
    list_url = "https://www.dune-project.org/download/"
    list_depth = 1

    version('2.7.0', sha256='d996c73efa345338766c5e4774e3b06ec1ed27eb745916af35877bbf38dd2cb2')
    version('2.6.0', sha256='7661155a0be3d001db43c6d99f1ee1a04101bc3e666dade82a40a6ed65578a42')
    version('2.5.2', sha256='30e9e6c22206034e3e490d3b0bf841cd49e8ece0d3a2f6df453e8594f546ec0d')
    version('2.5.1', sha256='f3782b27a4622bd7b7bc52fa7561d5bcf4f0dc39d6c161c082047c7b92140076')
    version('2.5.0', sha256='0b8ea21c046b703dbb4dfb1481e5ea74c9ea7487930be66d7a3fd74c854fb08e')
    version('2.4.2', sha256='4fe3d09b1dba6c36b73662af32088639eac5af33e01599469de2b71bd0a8c4e3')
    version('2.4.1', sha256='a6b92785150d309760f95add38d8a12bfd906d994e298cd54e744f34064b4e0f')
    version('2.4.0', sha256='f0f8acb95fd325b9b78f9d1e35d733830865378c4d5d5c34e3ecce687341fe86')

    #option
    variant('blas',   default=True, description='Build with BLAS support')
    variant('lapack', default=True, description='Build with LAPACK support')
    variant('gmp', default=True, description='Build with GNU multi-precision library support')
    variant('tbb', default=True, description='Build with Threading Building Blocks library support')
    variant('mkl', default=True, description='Build with Threading Building Blocks library support')
    variant('doxygen', default=True, description='Create Doxygen documentation')
    variant('sphinx', default=True, description='Create Sphinx documentation')
    variant('python', default=True, description='Build with Python')
    variant('vc', default=True, description='Build C++ Vectorization library support')
    variant('imagemagick', default=False, description='Imagemagick support')
    variant('threads', default=True, description='Activate pThread support')
    variant('shared', default=True, description='Enables the build of shared libraries.')
    variant('extrautils', default=True, description='Enable compilation and installation of extra utilities from the src subdirectory')
    variant('selector', default=True, description='Grid selector definition added to config.h')



    #dependencies 
    depends_on('dune-common')
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
    def url_for_version(self, version):
        url = "https://www.dune-project.org/download/{1}/dune-geometry-{1}.tar.gz"
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


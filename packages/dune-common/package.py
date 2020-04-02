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
#     spack install dune-common
#
# You can edit this file again by typing:
#
#     spack edit dune-common
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class DuneCommon(CMakePackage):
    """
    dune-common provides basic infrastructure classes for all Dune
    modules.
    """

    homepage = "https://www.dune-project.org"
    url      = "https://www.dune-project.org/download/2.7.0/dune-common-2.7.0.tar.gz"
    list_url = "https://www.dune-project.org/download/"
    list_depth = 1

    version('2.7.0', sha256='3c83c583a45325513113148cb94bd978e601907a6591c765f6253342e00f1890')
    version('2.6.0', sha256='1c566abb509ffd29690055acb5a7a69e3eda3848c2171f7af75c1e8743663c05')
    version('2.5.2', sha256='042fc7b9ae4b781e027a48048ea4067deb924ae172e56821f679bc8afe312159')
    version('2.5.1', sha256='fa9b1e538236e761d4eec703343e1345e8da1b75b3d2adbdde5fc53012d05814')
    version('2.5.0', sha256='3a6e20189926f0908316d43b2b130ae89e3662865926325a236c5465640a33c2')
    version('2.4.2', sha256='93e973e1db81950c378cf3ebe6cffca32fb642c7bd5e40a8883ebdc8c6909536')
    version('2.4.1', sha256='e4e9a4d6207484728a8582c5bca14c1479075b655d095790a037e6f0135762a8')
    version('2.4.0', sha256='7c2865e467883adbfdf4b248b8dbf3cd171a47c7498164d2dbe700171fdb7b1f')

    variant('blas',   default=True, description='Build with BLAS support')
    variant('lapack', default=True, description='Build with LAPACK support')
    variant('gmp', default=True, description='Build with GNU multi-precision library support')
    variant('tbb', default=True, description='Build with Threading Building Blocks library support')
    variant('mkl', default=True, description='Build with Math Kernel library support')
    variant('doxygen', default=True, description='Create Doxygen documentation')
    variant('sphinx', default=True, description='Create Sphinx documentation')
    variant('vc', default=True, description='Build C++ Vectorization library support')
    variant('imagemagick', default=False, description='Imagemagick support')
    variant('threads', default=True, description='Activate pThread support')
    variant('shared', default=True, description='Enables the build of shared libraries.')
    variant('python', default=True, description='Build with Python')
    variant('extrautils', default=True, description='Enable compilation and installation of extra utilities from the src subdirectory')
    variant('selector', default=True, description='Grid selector definition added to config.h')



    # FIXME: Add dependencies if required.
    #option
    depends_on('cmake@3.1:', type='build')
    depends_on('mpi')
    depends_on('blas',   when='+blas')
    depends_on('lapack', when='+lapack')
    depends_on('doxygen', when='+doxygen')
    depends_on('gmp', when='+gmp')
    depends_on('intel-tbb', when='+tbb')
    depends_on('intel-mkl', when='+mkl')
    depends_on('python@3.0:', when='+python')
    depends_on('py-sphinx', type='build', when='+sphinx')
    depends_on('vc', when='+vc')
    depends_on('pkg-config', type='build')
    depends_on('imagemagick', type='build', when='+imagemagick')

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
            '-DUSE_PTHREADS:BOOL=%s' % variant_bool('+threads'),
        ]
        if 'python' in spec:
            cmake_args.append('-DPYTHON_INSTALL_LOCATION:STRING="system"')

        return cmake_args

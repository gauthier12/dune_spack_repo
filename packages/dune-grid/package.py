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
#     spack install dune-grid
#
# You can edit this file again by typing:
#
#     spack edit dune-grid
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class DuneGrid(CMakePackage):
    """
    dune-grid provides grid interface and some grid implementations
    """

    homepage = "https://www.dune-project.org"
    url      = "https://www.dune-project.org/download/2.7.0/dune-grid-2.7.0.tar.gz"
    list_url = "https://www.dune-project.org/download/"
    list_depth = 1

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2.7.0', sha256='fa88dd60619df51100327a9128c3f7242a3a13b7ddfbac43a04f7e85c1f8d29d')
    version('2.6.0', sha256='a03145e8fd9b0d585f84ca8b62a65d6fc3e918fb571d48c1eb69f95499dee4ca')
    version('2.5.2', sha256='5763e36a0623f37a2cec14d62631e56468e10c3b4ed68f7a36b9479b13fd87d5')
    version('2.5.1', sha256='228f4bbeb8e810b02389f08307997b1f6290d49265e61281566e50afdadee511')
    version('2.5.0', sha256='a5ce78e6cf59b2968fdf4a638e199bae5c935b43e428b2492d7adf34fb609027')
    version('2.4.2', sha256='b3ab581b48f65da16200486ac56320ed0ea7811f88a5d00a131b23b3299e0c72')
    version('2.4.1', sha256='eeb3858bef485faa2c2f570ebc303742fa0b8581725523ba85fd87c5306353d7')
    version('2.4.0', sha256='e608bb47e7e9965b561c5eaceeb55cdc0a22adc5caf96c2eb67ee0cd1f8db9b4')

    #option
    variant('blas',   default=True, description='Build with BLAS support')
    variant('lapack', default=True, description='Build with LAPACK support')
    variant('gmp', default=True, description='Build with GNU multi-precision library support')
    variant('tbb', default=True, description='Build with Threading Building Blocks library support')
    variant('mkl', default=True, description='Build with Math Kernel library support')
    variant('doxygen', default=True, description='Create Doxygen documentation')
    variant('sphinx', default=True, description='Create Sphinx documentation')
    variant('python', default=True, description='Build with Python and dune-python')
    variant('vc', default=True, description='Build C++ Vectorization library support')
    variant('imagemagick', default=False, description='Imagemagick support')
    variant('uggrid', default=False, description='Build with dune-uggrid support')
    variant('metis', default=True, description='Build with METIS support')
    variant('parmetis', default=True, description='Build with ParMETIS support')
    variant('alberta', default=False, description='Build with Alberta support')
    variant('psurface', default=False, description='Build with Psurface support')
    variant('amiramesh', default=False, description='Build with AmiraMesh support')
    variant('extrautils', default=True, description='Enable compilation and installation of extra utilities from the src subdirectory')
    variant('selector', default=True, description='Grid selector definition added to config.h')
    variant('threads', default=True, description='Activate pThread support')
    variant('shared', default=False, description='Enables the build of shared libraries.')

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
    depends_on('metis', when='+metis')
    depends_on('parmetis', when='+parmetis')
    depends_on('dune-uggrid', when='+uggrid')
    depends_on('alberta', when='+alberta')
    depends_on('psurface', when='+psurface')
    depends_on('amiramesh', when='+amiramesh')
    def url_for_version(self, version):
        url = "https://www.dune-project.org/download/{1}/dune-grid-{1}.tar.gz"
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

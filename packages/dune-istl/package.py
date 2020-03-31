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
#     spack install dune-istl
#
# You can edit this file again by typing:
#
#     spack edit dune-istl
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class DuneIstl(CMakePackage):
    """
    dune-istl is the iterative solver template library which provides
    generic sparse matrix/vector classes and a variety of solvers based
    on these classes. A special feature is the use of templates to
    exploit the recursive block structure of finite element matrices at
    compile time. Available solvers include Krylov methods, (block-)
    incomplete decompositions and aggregation-based algebraic multigrid.
    """

    homepage = "https://www.dune-project.org"
    url      = "https://www.dune-project.org/download/2.7.0/dune-istl-2.7.0.tar.gz"
    list_url = "https://www.dune-project.org/download/"
    list_depth = 1

    version('2.7.0', sha256='c98d218bdf79549bb2e96fc465e9f9a72f5d88b78090812a59dae85cfee3833e')
    version('2.6.0', sha256='5ce06fc396624f654c3f34e333fd5900e992c4596b3230abe68617ed77f64f50')
    version('2.5.2', sha256='9fe33fb60b9c9f98100bfc909eb4d56598bae4f036f01f00b4a9fd2498387178')
    version('2.5.1', sha256='7e183b1361419620e3df7287d962bcbc1860fa8233588f5b25507ef7a20649dc')
    version('2.5.0', sha256='f9af37af1e8186443df384f155d66d2f16e95a909f9574d2bcae85d6d14b95ab')
    version('2.4.2', sha256='7e02eaa3d2d054f056709d1c9a91235b73bc0f96b47630f91c914d349093f572')
    version('2.4.1', sha256='0ea512e538935812cd6f3a9504f3b06fadff5c15d9d1b0dc499a5a913ea02a4d')
    version('2.4.0', sha256='205686b77f7e36d6bc0d2771b1514d98d221b608e5f4efdeeafb1a750e3ca2ba')

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
    variant('metis', default=True, description='Build METIS library support')
    variant('parmetis', default=True, description='Build ParMETIS library support')
    variant('suitesparse', default=True, description='Build SuiteSparse library support')
    variant('superlu', default=True, description='Build Supernodal LU library support')
    variant('arpack', default=True, description='Build ARnoldi PACKage library support')
    variant('imagemagick', default=False, description='Imagemagick support')
    variant('oldcategory', default=True, description='Enable/Disable the backwards compatibility of the category enum/method in dune-istl solvers, preconditioner, etc.')
    variant('threads', default=True, description='Activate pThread support')
    variant('shared', default=False, description='Enables the build of shared libraries.')
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
    depends_on('metis', when='+metis')
    depends_on('parmetis', when='+parmetis')
    depends_on('suite-sparse', when='+suitesparse')
    depends_on('superlu', when='+superlu')
    depends_on('arpack-ng', when='+arpack')
    depends_on('pkg-config', type='build')
    depends_on('imagemagick', type='build', when='+imagemagick')
    def url_for_version(self, version):
        url = "https://www.dune-project.org/download/{1}/dune-istl-{1}.tar.gz"
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
        cmake_args.append('-DDUNE_ISTL_SUPPORT_OLD_CATEGORY=%s' % variant_bool('+oldcategory'))
        if 'python' in spec:
            cmake_args.append('-DPYTHON_INSTALL_LOCATION:STRING="system"')

        return cmake_args

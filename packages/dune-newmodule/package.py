
from spack import *


class DuneNewmodule(CMakePackage):
    """Abstractions for functions and discrete function space bases"""


    homepage = "https://www.dune-project.org"
    url      = "https://gitlab.dune-project.org/staging/"
    list_url = 'https://gitlab.dune-project.org/staging/dune-functions/-/archive/releases/'
    list_depth = 1

    version('2.7', sha256='0')


    #option
    variant('geometry', default=True, description='Build with dune-geometry support')
    variant('grid', default=True, description='Build with dune-grid support')
    variant('istl', default=True, description='Build with dune-istl support')
    variant('localfunctions', default=True, description='Build with dune-localfunctions support')
    variant('uggrid', default=True, description='Build with dune-uggrid support')
    variant('functions', default=True, description='Build with dune-functions support')
    variant('python', default=True, description='Build with dune-python support')
    variant('typetree', default=True, description='Build with dune-typetree support')

    variant('alugrid', default=False, description='Build with dune-alugrid support')

    variant('selector', default=True, description='Grid selector definition added to config.h')
    variant('oldcategory', default=True, description='Enable/Disable the backwards compatibility of the category enum/method in dune-istl solvers, preconditioner, etc.')
    variant('extrautils', default=True, description='Enable compilation and installation of extra utilities from the src subdirectory')
    variant('selector', default=True, description='Grid selector definition added to config.h')
    variant('threads', default=True, description='Activate pThread support')
    variant('shared', default=True, description='Enables the build of shared libraries.')

     #dependencies 
    depends_on('dune-common',type=('build', 'link', 'run'))
    depends_on('dune-alugrid', when='+alugrid')
    depends_on('dune-functions', when='+functions')
    depends_on('dune-geometry', when='+geometry')
    depends_on('dune-istl', when='+istl')
    depends_on('dune-localfunctions', when='+localfunctions')
    depends_on('dune-python', when='+python')
    depends_on('dune-typetree', when='+typetree')
    depends_on('dune-grid+uggrid', when='+grid')
    depends_on('dune-uggrid', when='+uggrid')

    depends_on('cmake@3.1:', type='build')

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
        if 'python' in spec:
            cmake_args.append('-DPYTHON_INSTALL_LOCATION:STRING="system"')

        return cmake_args


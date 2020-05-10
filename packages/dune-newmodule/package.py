from spack import *

class DuneNewmodule(CMakePackage):
    """Abstractions for functions and discrete function space bases"""


    homepage = "https://www.dune-project.org"
    url      = "https://gitlab.dune-project.org/staging/"
    list_url = 'https://gitlab.dune-project.org/staging/dune-functions/-/archive/releases/'
    list_depth = 1

    version('2.7', sha256='0')


    #option

     #dependencies 
    depends_on('dune',type=('build', 'link', 'run'))

    depends_on('cmake@3.1:', type='build')


from skprocrustes.skprocrustes import *
from skprocrustes.version import __version__

__all__ = ['ProcrustesProblem', 'OptimizeResult', 'ProcrustesSolver',      \
           'SPGSolver', 'GKBSolver', 'EBSolver', 'GPISolver',              \
           'spectral_setup', 'spectral_solver', 'eb_solver', 'gpi_solver', \
           'blockbidiag', 'bidiaggs', 'optimality', 'compare_results']

# If you want to use Numpy's testing framerwork, use the following.
# Tests go under directory tests/, benchmarks under directory benchmarks/
from numpy.testing import Tester
test = Tester().test
#bench = Tester().bench

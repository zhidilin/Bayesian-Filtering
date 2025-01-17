import numpy as np
from numpy.linalg import cholesky

def ut_sigmas(M, P, c):
	"""
	UT_SIGMAS - Generate Sigma Points for Unscented Transformation
	
	Syntax:
	  X = ut_sigmas(M,P,c)
	
	In:
	  M - Initial state mean (Nx1 column vector)
	  P - Initial state covariance
	  c - Parameter returned by UT_WEIGHTS
	
	Out:
	  X - Matrix where 2N+1 sigma points are as columns
	
	Description:
	  Generates sigma points and associated weights for Gaussian
	  initial distribution N(M,P). For default values of parameters
	  alpha, beta and kappa see UT_WEIGHTS.
	
	See also UT_WEIGHTS UT_TRANSFORM UT_SIGMAS
	

	Copyright (C) 2006 Simo S�rkk�
	
	$Id$
	
	This software is distributed under the GNU General Public
	Licence (version 2 or later); please refer to the file
	Licence.txt, included with the software, for details.
	"""

	#  A = schol(P)
	A = cholesky(P)
	X = np.hstack([np.zeros(M.shape), A, -A])
	X = np.sqrt(c)*X + np.tile(M, X.shape[1])

	return X

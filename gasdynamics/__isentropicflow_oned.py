import numpy as np 
from copy import copy
#### GASDYNAMICS V1.0

# VARIABLE NOMENCLATURE:
#	- M: mach number
#	- nu: prandtl-meyer function
#	- T: temperature
#	- p: pressure
#	- rho: density
def mach_angle(M,degrees=0):
	""" Computes mach angle for M > 1

		ARGS:
			M (float): mach number of interest

			*optional
			degrees (bool): whether to return answer in degrees or rad (rad by default)

		OUTPUTS:
			mu (float): mach angle
	"""
	mu = np.arcsin(1/M)
	if (degrees):
		return mu*180/np.pi
	else:
		return mu

def prandtl_meyer_angle(M,gamma,degrees=0):
	""" Computes prandtl-meyer function for M > 1

		ARGS:
			M (float): mach number of interest
			gamma (float): ratio of specific heats 

			*optional
			degrees (bool): whether to return answer in deegrees or rad (rad by default)

		OUTPUTS:
			nu (float): prandtl-meyer angle
	"""
	nu = np.sqrt((gamma+1)/(gamma-1))*np.arctan(np.sqrt((gamma-1)/(gamma+1)*(M**2-1))) - np.arctan(np.sqrt(M**2-1))
	if (degrees):
		return nu*180/np.pi 
	else:
		return nu

def isentropic_ratios(M_1,M_2,gamma):
	""" Computes isentropic flow ratios between two points in flow returning fundamental flow properties ratios

		ARGS:
			M_1 (float): mach at one point in flow
			M_2 (float): mach at second point in flow
			gamma (float): ratio of specific heats

		OUTPUTS:
			T_ratio,p_ratio,rho_ratio (tuple of floats): val_2/vaL_1 where T = temp, p = pressure, rho = density
	"""
	T_ratio = (1+(gamma-1)/2*M_1**2)/(1+(gamma-1)/2*M_2**2)
	p_ratio = T_ratio**(gamma/(gamma-1))
	rho_ratio = T_ratio**(1/(gamma-1))	
	#a_ratio = np.sqrt(T_ratio)
	return T_ratio,p_ratio,rho_ratio


def expansion_ratio(M_1,M_2,gamma):
	""" Computes area expansion ratio given two mach numbers in flow

		ARGS:
			M_1 (float): mach number at one point in flow
			M_2 (float): mach number at second point in flow
			gamma (float): ratio of specific heats 

		OUTPUTS:
			epsilon (float): area of expansion ration A_2 / A_1 
	"""
	return M_1/M_2*((2+(gamma-1)*M_2**2)/(2+(gamma-1)*M_1**2))**((gamma+1)/(2*(gamma-1)))

# Important rocket relations
# IS THIS FUNCTION NECESSARY??
def PR_expansion_mach(PR,gamma):
	# returns mach number given pressure ratio
	return np.sqrt(((PR)**((gamma-1)/gamma)-1)*2/(gamma-1))

import numpy as np
from copy import copy 
def standard_atmosphere(altitude):
	""" Computes US 1976 Standard Atmosphere values for altitudes given in altitude

		ARGS:
			altitude (list): list of altitudes for which standard atmospheric values are to be computed for
							 (note that for a specific altitude, argument must still be a list)

		OUTPUTS:
			p_atm_range (list): list of atmospheric pressures in Pascals
			T_atm_range (list): list of temperatures in Kelvin
			rho_atm_range (list): list of densities in kg/m**3
	"""
	# 1976 US Standard Atmosphere

	ps = 101325
	rhos = 1.225
	Ts = 288.15

	R = 287.0531
	g_0 = 9.80665
	a = -6.5/1000
	earth_radius = 6.356766*10**6
	altitude = copy(altitude)
	p_atm_range = copy(altitude)
	T_atm_range = copy(altitude)
	rho_atm_range = copy(altitude)
	for i in range(len(altitude)):
		h = earth_radius/(earth_radius + altitude[i])*altitude[i] #geopotential alt.
		#h = 20000

		if (h<=11000):
		# gradient (troposphere) region
			T_atm = Ts + a*h;
			p_atm = ps*(T_atm/Ts)**-(g_0/(a*R))
			rho_atm = rhos*(T_atm/Ts)**-(1+g_0/(a*R))
		else:
		# contant temperature (stratosphere)region ~20000m (65616.8ft), should check
			# values at boundary
			T_atm = Ts + a*11000
			p1 = ps*(T_atm/Ts)**(-g_0/(a*R))
			rho1 = rhos*(T_atm/Ts)**-(1+g_0/(a*R))

			# values at elevation
			p_atm = p1*np.exp(-g_0/(R*T_atm)*(h-11000))
			rho_atm = rho1*np.exp(-g_0/(R*T_atm)*(h-11000))
		p_atm_range[i] = p_atm
		T_atm_range[i] = T_atm 
		rho_atm_range[i] = rho_atm 


	return (p_atm_range,T_atm_range,rho_atm_range)
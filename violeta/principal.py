
# .. ................................................................................... .. #
# .. Proyecto: UrbanLab - Plataforma de ayuda para micro y pequeñas empresas             .. #
# .. Archivo: principal.py - flujo principal de uso                                      .. #
# .. Desarrolla: ITERA LABS, SAPI de CV                                                  .. #
# .. Licencia: Todos los derechos reservados                                             .. #
# .. Repositorio: https://github.com/IFFranciscoME/Urban_Lab.git                         .. #
# .. ................................................................................... .. #


# Importing and initializing main Python libraries
import proceso as pr
import datos as dat
import entradas as ent
import visualizaciones as vs
from time import time
import matplotlib.pyplot as plt

# Start time
#t0 = time()

if __name__ == "__main__":
	
	# Using function: read_file (original)
	df_pymes_or = dat.read_file(ent.path_data_pyme, ent.sheet_data_pyme)
	
	# Using function: clean_data
	df_pymes = dat.clean_data_pymes(df_pymes_or)
	"""
	# Using metric_quantification with stress conditions
	metric_s = pr.metric_quantification(df_pymes, ent.conditions_stress, 'Estres')
	
	# Using metric_quantification with adaptability conditions
	metric_a = pr.metric_quantification(df_pymes, ent.conditions_adaptability, 'Adaptabilidad')
	
	# Visualizations
	fig  = vs.map_metric(metric_s, 'Estres')
	fig2 = vs.map_metric(metric_a, 'Adaptabilidad')
	
	'''
	#fig.show()
	#fig2.show()
	
	'''
	"""
	# .. ............................................................................... .. #
	# .. ............................................................................... .. #
	
	# Leer base de datos de precios original
	df_prices_or = dat.read_file(ent.path_data_prices, ent.sheet_data_prices)
	
	# limpiar base de datos
	df_prices = dat.clean_data_prices(df_prices_or)
	
	# Fragmentar por series de tiemo
	time_series = dat.series_tiempo(df_prices)
	
	# Predictions
	predictions = [pr.f_predict(time_series[s]) for s in range(len(time_series))]
	
	# Linea recta -> 228
	dif, no_info = [], []
	i = 0
	for numb in predictions:
		if len(numb) == 2:
			dif.append(numb[1] - numb[0])
		else:
			no_info.append(i)
		i+=1
	
	# Checar singularidades
	n = 13
	time_series[no_info[n]].plot()
	plt.title(time_series[no_info[n]].name)
		
	'''
	# End time
	#t1 = time()
	
	#print('el tiempo transcurrido fue: ' + str(t1-t0))
	'''
	
	
	
	
	
		
		
	
	
	
	
	
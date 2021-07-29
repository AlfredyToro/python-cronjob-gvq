import query

###1. Consulto la de la base ind tabla de log para ver cual fue la ultima carga exitosa
lastLoadTime = query.lastSuccessLoadDate()
print('last successfull load date', lastLoadTime)
views = query.getViewGvq(lastLoadTime)	
if views:
	query.insertLogInd("")
	query.insertViewInd(views)
else:
	query.insertLogInd("No new views found")
#result = query.lastSuccessLoadDate()
#print('data found', result)

###2. Si hay carga exitosa tomo la fech año/mes y le sumo un mes, solo cargo datos para ese mes
###3. Si no hay carga exitosa necesito cargar toda la data
###4. escenario 1 cargo el nuevo mes:
###		Consulto solo 1 mes de la data de la vista
###		por cada registro genero una nueva entrada en la base de Ind
###		si termino bien, escribo el exito y la fecha
###		si termino mal, escribo el fallo, la fecha y el motivo
###5. escenario 2 cargo toda la data 
###		Consulto toda la data de la vista
###		por cada registro genero una nueva entrada en la base de Ind
###		si termino bien, escribo el exito y la fecha
###		si termino mal, escribo el fallo, la fecha y el motivo


 

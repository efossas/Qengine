import requests

def checkBlockContainer(configuration,name):
	url = configuration[name]
	
	bounced = False
	try:
		response = requests.get(url + '/')
		if response.status_code != 200:
			bounced = True
	except:
		bounced = True
	
	if bounced:	
		print 'Could not contact ' + name + ' at ' + url
		return False
	return True

def loadblocks(configuration):
	BLOCKS = {}
	
	if checkBlockContainer(configuration,'PYTHON2_URL'):
		import qpython2
		qpython2.PYTHON2_URL = configuration['PYTHON2_URL']
		BLOCKS['python2'] = qpython2.process_python2_code
		print 'PYTHON2 enabled'
	
	if checkBlockContainer(configuration,'SAGE_URL'):
		import qsage
		qsage.SAGE_URL = configuration['SAGE_URL']
		BLOCKS['sage'] = qsage.process_sage_code
		print 'SAGE enabled'
	
	return BLOCKS
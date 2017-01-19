from django import template
 
register = template.Library()

def tdelta(value, arg):
	tds=[]
	if not value:
		td = 'kosong'
	else:
		if arg: 
			td = "haha" 
			tds = value[arg]
		else: 
			td = "hihi" + "prot" 

	print ("TD => "+td)
	return tds

register.filter('tdelta', tdelta)

def tauthor(value, arg):
	tds=[]
	if not value:
		td = 'kosong'
	else:
		if arg: 
			td = "haha" 
			tds = value[arg]
		else: 
			td = "hihi" + "prot" 

	print ("TD => "+td)
	return tds

register.filter('tauthor', tauthor)

def taff(value, arg):
	tds=[]
	if not value:
		td = 'kosong'
	else:
		if arg: 
			td = "haha" 
			tds = value[arg]
		else: 
			td = "hihi" + "prot" 

	print ("TD => "+td)
	return tds

register.filter('taff', taff)
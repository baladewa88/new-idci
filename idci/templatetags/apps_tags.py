from django import template
 
register = template.Library()
 
def tdelta(value, arg):
    if not value: 
        td = 'kosong'
    else:  
        if arg: 
            td = value + pret
        else: 
            td = value + prot 
    print ("TD => "+td)
    return td    
register.filter('tdelta', tdelta)
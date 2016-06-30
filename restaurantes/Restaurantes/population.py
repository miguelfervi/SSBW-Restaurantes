import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Restaurantes.settings')

import django
django.setup()

from app_restaurantes.models import Restaurante


def populate():

	p = Restaurante (id="1",nombre="Mirador de Axia", direccion="Calle Limonada", email = "jamon@gmail.com", me_gusta =0, imagen ="http://www.casacuevarural.com/fotografiasrestaurante/Restaurante-Don-Fadrique_128.jpg" )
	p.save()

	q = Restaurante (id="2",nombre="Meson La Capital", direccion="Calle Jamones", email = "pepe@gmail.com", me_gusta =0, imagen="http://www.granadarestaurantes.es/wp-content/uploads/2010/12/RESTAURANTE_CHIKITO_11.jpg")
	q.save()


	# muestro el nombre de los restaurantes para comprobarlo
	for c in Restaurante.objects.all():
            print "- {0}".format(str(c))

	return 0


if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()

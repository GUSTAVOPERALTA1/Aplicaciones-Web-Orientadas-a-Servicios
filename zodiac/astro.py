import web
import json
import random
futuro = {}
urls = (
    '/(.*)','astro',)
app = web.application(urls, globals())


class zodiaco():
	def GET(self, zodiac):
		try:
			dia = int(zodiac[0:2])
			mes = int(zodiac[3:5])
			print(dia, mes)


			if dia >= 22 and mes == 12 or mes == 1 and dia <= 19:
				futuro = {}
				futuro["SIGNO"] = "CAPRICORNIO"
				futuro["FECHA"] = "22 DE DIC/19 DE ENE"
				futuro["TU HOROSCOPO"] = (random.choice(['Tienes una gran necesidad de sentirte aceptado y parte de un grupo, sin embargo no dudas ni un segundo en decir lo que sientes,porque prefieres estar rodeado de personas honestas que de falsas. Todos dicen que no se debe juzgar un libro por su portada sin embargo, tu siempre lo haces al momento de buscar una pareja, pero una vez que te enamoras, te entregas por completo. Mientras estas soltero eres una persona que puede llegar a hacer promesas que no cumplirá y tambien llegas a venderte de más, que onda contigo, no te gustan las personas falsas pero eres más feca que un billete de 2 pesos.'])) 
				futuro["ELEMENTO"] = "TIERRA"
				futuro["NUMERO DE LA SUERTE"] = '3, 16 y 25'
				futuro["COLOR"] = "GRIS"				 
				result = json.dumps(futuro)
				return result

			elif dia >= 20 and mes == 1 or dia <= 18 and mes == 2:
				futuro = {}
				futuro["SIGNO"] = "ACUARIO"
				futuro["FECHA"] = "2O DE ENE/18 DE FEB"
				futuro[
				    "TU HOROSCOPO"] = (random.choice([ "Eres muy seguro de ti mismo y por lo tanto siempre tienes foco de atencion, generas confianza aunque muy en el fondo eres inseguro. Si tu pareja quiere un poco más de atencion vas a optar por dejarla, porque no puedes prestar más atencion de la que te prestas a ti mismo. El narcismo ni en Marte es bueno mi bro."]))
				futuro["ELEMENTO"] = "FUEGO"
				futuro["NUMERO DE LA SUERTE"] = "31, 11, 52, 5, 15, 25"
				futuro["COLOR"] = "ROJO"
				result = json.dumps(futuro)
				return result

			elif dia >= 19 and mes == 2 or dia <= 20 and mes == 3:
				futuro = {}
				futuro["SIGNO"] = "PISCIS"
				futuro["FECHA"] = "19 DE FEB/20 DE MAR"
				futuro[
				    "TU HOROSCOPO"] = (random.choice(["Eres una persona soñadora en exceso, pero cuando algo te sale mal tiendes a quejarte. Date cuenta que en la vida no siempre tendras lo que quieres. Tiendes a disfrutar mucho tu vida y eso es un punto que habla bien de ti, pero limitas tu experiencia de vida al no entregarte al amor, te gusta jugar con los sentimientos de las demas personas, eso te quita el punto de buena persona que te habia dado."]))
				futuro["ELEMENTO"] = " AGUA"
				futuro["NUMERO DE LA SUERTE"] = "19, 2 y 5"
				futuro["COLOR"] = "AZUL"

				result = json.dumps(futuro)
				return result

			elif dia >= 21 and mes == 3 or dia <= 19 and mes == 4:
				futuro = {}
				futuro["SIGNO"] = "ARIES"
				futuro["Fecha"] = "21 DE MAR/19 DE ABR"
				futuro[
				    "TuHoroscopo"] = (random.choice(["Eres una persona de retos, con alma aventurera y que siempre busca aprender algo nuevo. Muy bonito. Pero debido a esa energia tambien sueles ser algo agresivo pero si alguien te hace algo te ofendes de inmediato, relajate mi amigo, comete un Snickers"])) 
				futuro["Elemento"] = "FUEGO"
				futuro["Numero"] = "7, 17 y 21"
				futuro["Color"] = "ROJO"

				result = json.dumps(futuro)
				return result

			elif dia >= 20 and mes == 4 or dia <= 21 and mes == 5:
				futuro = {}
				futuro["SIGNO"] = "TAURO"
				futuro["FECHA"] = "20 DE ABR/21 DE MAY"
				futuro[
				    "TuHoroscopo"] = (random.choice(["Suenles ser una persona perfeccionista con corazon aventurero que le gusta tener breves romances hasta encontrar a su alma gemela (pero como la vas a encontrar si brincas como chapulin), eres receloso si alguien te hace algo, deberias calmarte y aprender a perdonar. Son los más tercos de todos los signos. Tipico de Tauro"]))
				futuro["ELEMENTO"] = "TIERRA"
				futuro["NUMERO"] = "4, 6 y 11"
				futuro["COLOR"] = "VERDE"
            
				result = json.dumps(futuro)
				return result

			elif dia >= 21 and mes == 5 or dia <= 20 and mes == 6:
				futuro = {}
				futuro["SIGNO"] = "GEMINIS"
				futuro["FECHA"] = "21 DE MAY/20 DE JUN"
				futuro[
				    "TU HOROSCOPO"] = (random.choice(["Los geminis son bipolares y las relaciones con ellos pueden ser muy complicadas porque siempre buscan su propio beneficio, asi que mejor buscan algo más casual, tienden a ser los manipuladores aunque en realidad no saben ni como controlar su vida sentimental y quiere manipular la de los demas JA JA"]))
				futuro["ELEMENTO"] = "AIRE"
				futuro["NUMERO DE LA SUERTE"] = "22, 55, 36, 26, 44 y 34"
				futuro["COLOR"] = "AMARILLO"
 
				result = json.dumps(futuro)
				return result

			elif dia >= 21 and mes == 6 or dia <= 22 and mes == 7:
				futuro = {}
				futuro["SIGNO"] = "CANCER"
				futuro["FECHA"] = "21 DE JUN/22 DE JUL"
				futuro[
				    "TU HOROSCOPO"] = (random.choice(["Tiendes a vivir en el pasado, recordando relaciones anteriores, pero si estas en una actual visualizas tu futuro. Yo te aconsejo que te alejes de eso. El pasado ya no existe y el futuro es un quizas, lo real es el presente, enfocate ahí. Eres amable y demasiado tierno como para aceptar los golpes y patadas de la vida, eres como un conejito esponjoso con una manada de lobos detras, así que trata de quitarte esa venda de los ojos que si no el mundo te traga vivo :D"]))
				futuro["TU ELEMENTO"] = "AGUA"
				futuro["NUMERO DE LA SUERTE"] = "31, 32, 9, 15, 1 y 28"
				futuro["COLOR"] = "BLANCO" 

				result = json.dumps(futuro)
				return result

			elif dia >= 23 and mes == 7 or dia <= 22 and mes == 8:
				futuro = {}
				futuro["SIGNO"] = "LEO"
				futuro["FECHA"] = "23 DE JUL/22 DE AGO"
				futuro[
				    "TU HOROSCOPO"] = (random.choice(["Eres un lider nato y cuando entras en la sala todas las miradas estan en ti, todo esto afecta en que NUNCA quieras aceptar tus errores, bajate de tu nube que el mundo no gira al rededor de tu melena"]))
				futuro["ELEMENTO"] = "FUEGO"
				futuro["NUMERO DE LA SUERTE"] = "20, 27, 36, 1, 23 y 8"
				futuro["COLOR"] = "NARANJA"
				result = json.dumps(futuro)
				return result

			elif dia >= 23 and mes == 8 or dia <= 22 and mes == 9:
				futuro = {}
				futuro["SIGNO"] = "VIRGO"
				futuro["FECHA"] = "23 DE AGO/22 DE SEP"
				futuro[
				    "TU HOROSCOPO"] = (random.choice(["Los virgo son personas extremadamente ordenadas y piensan de forma estructurada y logica. (Aunque no sirve de mucho porque por experiencia propia, nunca sale como se espera jaja) Son personas bastante sencillas en cuestion de no pensar mucho, aunque en realidad la mente vuela como una locomotora con alas. A la hora de encontrar una pareja se conforman con cualquiera que los valore"])) 
				futuro["ELEMENTO"] = "TIERRA"
				futuro["NUMERO DE LA SUERTE"] = "56, 44, 17, 13, 45 y 24"
				futuro["COLOR"] = "MARRON"
				result = json.dumps(futuro)
				return result

			elif dia >= 23 and mes == 9 or dia <= 22 and mes == 10:
				futuro = {}
				futuro["SIGNO"] = "LIBRA"
				futuro["FECHA"] = "23 DE SEP/22 DE OCT"
				futuro[
				    "TU HOROSCOPO"] = (random.choice(["Te cuesta muchisimo tomar una decision, necesitan tener todas las situaciones de su vida en equilibro para estar bien. Tu peor enemigo eres tu mismo, podrias trabajar mas en tu seguridad propia. Son indecisos al tener una pareja así que primero deben conocerla muy bien"])) 
				futuro["ELEMENTO"] = "AIRE"
				futuro["NUMERO DE LA SUERTE"] = "2, 8 y 19"
				futuro["COLOR"] = "ROSA"
				result = json.dumps(futuro)
				return result
      
      elif dia >= 23 and mes == 10 or dia <= 21 and mes == 11:
				futuro = {}
				futuro["SIGNO"] = "ESCORPION"
				futuro["FECHA"] = "23 DE OCT/22 DE NOV"
				futuro[
				    "TU HOROSCOPO"] = (random.choice(["No hay nada ni nadie más intenso y curioso que un Escorpio. Son personas muy introvertidas, reflexivas y, a menudo, existencialistas. Los Escorpio necesitan estar absolutamente seguros de algo antes de hacerlo. Raramente hacen caso a alguien más que a ellos mismos y les cuesta mucho centrarse en una sola cosa, por lo que suelen tener intereses muy variados. Su imaginación y gran sentido de la competitividad los hace imparables en el ámbito creativo."])) 
				futuro["ELEMENTO"] = "AGUA"
				futuro["NUMERO DE LA SUERTE"] = "4, 13 y 21"
				futuro["COLOR"] = "ROJO"
				result = json.dumps(futuro)
				return result

      elif dia >= 22 and mes == 11 or dia <= 21 and mes == 12:
				futuro = {}
				futuro["SIGNO"] = "SAGITARIO"
				futuro["FECHA"] = "22 DE NOV/21 DE DIC"
				futuro[
				    "TU HOROSCOPO"] = (random.choice(["Los Sagitario tienen una gran confianza en sí mismos y a menudo son el alma de la fiesta. Casi siempre caen bien por la energía positiva que desprenden y su visión optimista del futuro es contagiosa. Los nacidos bajo este signo forjan amistades nuevas con mucha facilidad y son personas muy sociables en quienes, generalmente, se puede confiar."])) 
				futuro["ELEMENTO"] = "FUEGO"
				futuro["NUMERO"] = "9, 14 y 23"
				futuro["COLOR"] = "VIOLETA"
				result = json.dumps(futuro)
				return result
      


        
		except:
			futuro = {}
			futuro["TU FUTURO"] = "EL FUTURO: " + str(zodiaco)
			futuro["ERROR"] = "PON BIEN TUS DATOS POR FAVOR :3"
			futuro[
			    "TE DIREMOS QUE PASARA ANTES DE QUE PASE"] = "FECHA DE NACIMIENTO:  DD/MM/AAAA"
			result = json.dumps(futuro)
			return result


if __name__ == "__main__":
	app.run()
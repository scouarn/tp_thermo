import numpy as np
import matplotlib.pyplot as plt


#constantes
T0 = 350.0
T1 = 290.0

L  = 10.0
dx = 0.1

tf = 50.0
dt = 0.001




def main() :

	#vérification humaine si problème avec le dt/dx^2 trop grand
	if (delta := dt/(dx*dx) ) > 0.1 :
		input(f'Delta = {delta}, continuer ?')


	n_x = int(L/dx) #nombre de valeurs de X
	n_t = int(tf/dt) #nombre de valeurs de t
	

	#matrice de données : theth[x][t]
	thet = np.zeros((n_x, n_t))

	#conditions initiales (theth[x][0] = 0)
	thet[:, 0].fill(0)

	#conditions limites (theth[0][t] = T0-T1 et theth[L][t] = 0)
	thet[0].fill(T0-T1)
	thet[-1].fill(0)


	#équa diff
	d_theth = lambda x, t : (thet[x+1][t-1] + thet[x-1][t-1] - 2*thet[x][t-1])/(dx*dx)


	#méthode d'euler
	for t in range(1, n_t) : #argument des ranges : ignorer les conditions initiales/limites

		#traité comme un système de n_x équations
		for x in range(1, n_x-1) :
		 	thet[x][t] = thet[x][t-1] + d_theth(x,t) * dt

		#pourcentage de complétion
		print(f'Simulation {round(t/n_t*100)}%', end='\r')
	print("\nOK")


	#affichage histogramme 2D
	plt.imshow(thet, extent=(0, tf, 0, L), cmap='inferno', interpolation='nearest', aspect='auto')
	cb = plt.colorbar()
	
	cb.set_label('Différence de température')
	plt.xlabel('Temps')
	plt.ylabel('Position')
	plt.title('Évolution de la température dans une barre métalique')

	plt.show()





if __name__ == '__main__' :
	main()
#iprb: Probablidad de que 1 par cualqier producirá un ser con al menos uno de los alelos Dominante
hD=float(raw_input('Introduce k= '))	#k homocigótico dominante YY
he=float(raw_input('Introduce m= '))	#m heterocigótico Yy
hr=float(raw_input('Introduce n= '))	#n homocigótico recesivo yy
tot=hD+he+hr

#mediante un diagrama de combinaciones
prob=(hD/tot)*((hD-1)/(tot-1))+(hD/tot)*(he/(tot-1))+(hD/tot)*(hr/(tot-1))	#probabilidad cuando un padre homodominante
prob+=(he/tot)*(hD/(tot-1))+(he/tot)*((he-1)/(tot-1))*0.75+(he/tot)*(hr/(tot-1))*0.5	#probabilidad cuando un padre heterocigoto
prob+=(hr/tot)*(hD/(tot-1))+(hr/tot)*(he/(tot-1))*0.5	#probabilidad cuando un padre homorecesivo

print prob
raw_input()
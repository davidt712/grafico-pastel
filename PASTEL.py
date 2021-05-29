import matplotlib.pyplot as plot

#GRAFICO DE PASTEL 1
LUGARES = ["ANCASH", "APURIMAC", "CALLAO", "HUANCAVELICA", "HUANUCO", "ICA", "JUNIN", "LIMA", "PASCO"]
cantidad = [1614, 699, 900, 663, 1256, 792, 1644, 8542, 352]
explode = (0., 0., 0, 0, 0, 0, 0, 0.1, 0)

fig3, ax3 = plot.subplots()
ax3.pie (cantidad, explode=explode, labels=LUGARES, autopct='%1.1f%%', shadow=True, startangle=90)
ax3.axis('equal')
plot.title('VACUNAS HOMBRES')
plot.legend()
plot.savefig('grafica_pastel.png')
plot.show()

#GRAFICO DE PASTEL 2
LUGARES = ["ANCASH", "APURIMAC", "CALLAO", "HUANCAVELICA", "HUANUCO", "ICA", "JUNIN", "LIMA", "PASCO"]
cantidad = [1668, 710, 1013, 681, 1237, 837, 1737, 9287, 367]
explode = (0, 0, 0, 0, 0, 0, 0, 0.1, 0)

fig4, ax4 = plot.subplots()
ax4.pie (cantidad, explode=explode, labels=LUGARES, autopct='%1.1f%%', shadow=True, startangle=90, center=(0, 0))
ax4.axis('equal')
plot.title('VACUNAS MUJERES')
plot.legend()
plot.savefig('grafica_pastel.png')
plot.show()
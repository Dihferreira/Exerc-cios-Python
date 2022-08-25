lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = lar * alt
t = area / 2
print('Sua parede tem {}x{} e sua área é de {}m²,'.format(lar, alt, area))
print('Para pintar essa parede, vc precisara de {}l de tinta.'.format(t))
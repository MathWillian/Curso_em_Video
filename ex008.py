m = float(input('Uma distância em metros: '))
cm = m * 100
mm = m * 100
dam = m * 0.1
hm = m * 0.01
km = m * 0.001
print('A medida de {}m corresponde a {:.0f}cm, {:.0f}mm, {}dam, {}hm e {}km'.format(m, cm, mm, dam, hm, km))

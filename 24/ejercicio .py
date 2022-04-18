tabla_de_control='TRWAGMYFPDXNUZSQVHLCKE'

nif='12345678'
control_dijital=tabla_de_control[int(nif) %23]
whole_nif = nif +control_dijital

print(whole_nif)





























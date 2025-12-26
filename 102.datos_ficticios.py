from faker import Faker
faake = Faker()
print(faake.name())
print(faake.address())
print(faake.text())
print(faake.phone_number())
print(faake.date_of_birth())
print('*'*25)
#con localicalizacion espeicificas
faker_es = Faker('es_ES')
print(faker_es.name())
print(faker_es.address())



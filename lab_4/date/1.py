import datetime

vremya_smerti=datetime.datetime.now()
print(vremya_smerti)

beskunburyn=vremya_smerti.day-5
uakyt=datetime.datetime(vremya_smerti.year, vremya_smerti.month, beskunburyn)
print(uakyt)
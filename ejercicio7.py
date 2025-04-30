#pregunta si una persona tiene licencia y si lleva casco o no lleva casco, si no tienen liciencia o no lleva casco no puede conducir
licen = input("have you license for drive? (Yes/No): ").lower()
casc = input("have you head helmet for drive? (Yes/No): ").lower()

if licen != "Yes" or casc != "Yes":
    print("you can not drive")
else:
    print("you can drive")


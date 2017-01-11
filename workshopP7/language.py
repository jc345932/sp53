from workshopP7.programminglanguage import Programminglanguage

def main():
    ruby = Programminglanguage("Ruby", "Dynamic", True, 1995)
    python = Programminglanguage("Python", "Dynamic", True, 1991)
    vb = Programminglanguage("Visual Basic", "Static", False, 1991)
    dynamic = []
    print(ruby)
    print(python)
    print(vb)
    print("The dynamic lanuages are:")
    if ruby.is_dynamic:
        dynamic.append(ruby.name)
    if python.is_dynamic:
        dynamic.append(python.name)
    if vb.is_dynamic:
        dynamic.append(vb.name)
    print(dynamic)
main()


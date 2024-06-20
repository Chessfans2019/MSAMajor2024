import automobile

def main():
    #create automobile object
    auto1 = automobile.Automobile("Ford", "Focus", "1234", 2.2, "Ronaldo", 2013)
    auto2 = automobile.Automobile("Honda", "Accord", "23456", 3.0, "Messi", 2017)

    print(f"{auto1.make} {auto1.model}: {auto1.year}")

main()
if __name__ == "__main__":

    greenhouseCountries = []
    greenCountries = []
    with open('/Users/rafaelriosgarcia/Desktop/pythonCode/Tec/greenhousedata.csv','r') as f:
        r = f.read().splitlines()
        r.pop(0)
        for j in r:
            lin = j.split(',')
            greenhouseCountries.append([float(lin[2]),int(lin[1]),str(lin[0])])

        for i in greenhouseCountries:
            if i[1] == 2010:
                greenCountries.append(i)
        order = sorted(greenCountries, reverse = True)
    print()
    print("5 paises productores de gases de invernadero en 2010:", "\n1.-", order[0], "\n2.-", order[3], "\n3.-",order[6], "\n4.-", order[9], "\n5.-", order[12])
    print()

    countries = []
    with open('/Users/rafaelriosgarcia/Desktop/pythonCode/Tec/populationbycountry19802010millions.csv', 'r') as p:
        reader = p.read().splitlines()
        reader.pop(0)
        for i in reader:
            line = i.split(',')
            countries.append([float(line[31]),str(line[0])])
    sortedCountries = sorted(countries, reverse = True)

    print()
    print("Lo 5 paises más poblados en 2010: ","\n1.- ",sortedCountries[1],"\n2.- ",sortedCountries[2],"\n3.- ",sortedCountries[3],"\n4.- ",sortedCountries[4],"\n5.- ",sortedCountries[5])
    print()

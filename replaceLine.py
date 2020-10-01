if __name__ == "__main__":

    char1 = 'NA'
    char2 = '0'
    filename = "/Users/rafaelriosgarcia/Desktop/pythonCode/Tec/populationbycountry19802010millions.csv"
    filer = open(filename, "r")
    filew = open(filename + ".mod", "w")
    buff = filer.read()
    rbuff = buff.replace(char1, char2)
    filew.write(rbuff)
    filer.close()
    filew.close()

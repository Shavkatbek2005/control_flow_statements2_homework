def main(n):
    if n>0 and n<=31:
        return "Yanvar"
    elif n>31 and n<=60:
        return "Febral"
    elif n>60 and n<=91:
        return "Mart"
    elif n>91 and n<=121:
        return "April"
    elif n>121 and n<=152:
        return "May"
    elif n>152 and n<=182:
        return "Iyun"
    elif n>182 and n<=213:
        return "Iyul"
    elif n>213 and n<=244:
        return "Avgust"
    elif n>244 and n<=274:
        return "Sentabr"
    elif n>274 and n<=305:
        return "Oktabr"
    elif n>305 and n<=335:
        return "Noyabr"
    elif n>335 and n<=366:
        return "Dekabr"
    else:
        return "Bunday oy Mavjud emas"
print(main(34))
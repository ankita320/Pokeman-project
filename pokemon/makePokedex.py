#! /usr/bin/python3
print("Content-Type: text/html\n\n")


def homePage():
    tab = " " * 4
    site = '''
<DOCTYPE HTML>
    <html>
        <head>
            ?HEAD?
            <title>
                ?TITLE?
            </title>
            <style>
                ?STYLE?
            </style>
        </head>
        <body>
            ?BODY?
        </body>
    </html>'''


    site = site.replace("?TITLE?", "Pokemon")
    head = ""

    h1 = "<h1>Pokemon Reviews</h1>\n"
    p = tab * 2 + "<p>I think pokemans are cool even though I haven't really played with them that much. I heard Pikachu is really popular though, so I think that's my favorite! I also heard of Kirby which is also cool!</p>\n"

    technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''
#make navbar
    poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
    ahref = "<a href=\"LINK\">_DD_</a>\n"
    navbar = '''
        <button><a href= "home.html">Home</a></button>
        <button><a href = "all.html">All Pokeman</a></button>
        <button><a href = "top.html">Top 10</a></button>
        <div class="dropdown">
        <button><a href = "types.html">Types</a></button>
    <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''
#loop for 
    T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    data += p

    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(homePage())

home = open("home.html", "w")
print(homePage(), file = home)
home.close()

def allPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[0:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
<DOCTYPE HTML>
    <html>
        <head>
            ?HEAD?
            <title>
                ?TITLE?
            </title>
            <style>
                ?STYLE?
            </style>
        </head>
        <body>
            ?BODY?
        </body>
    </html>'''


        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>All Pokemon</h1>\n"
        p = tab * 2 + "<p>These are all of the 151 Pokemon</p>\n"
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

        <button><a href= "home.html">Home</a></button>
        <button><a href = "all.html">All Pokeman</a></button>
        <button><a href = "top.html">Top 10</a></button>
        <div class="dropdown">
        <button><a href = "types.html">Types</a></button>
    <div class="dropdown-options">\n''' + ahref  + '''</div>
</div>
'''

    T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    data += p
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num)):
        img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
        tdata = td.replace("_TDATA0_", img)
        tdata = tdata.replace("_TDATA1_", str(num[i]))
        tdata = tdata.replace("_TDATA2_", str(name[i]))
        tdata = tdata.replace("_TDATA3_", str(type1[i]))
        tdata = tdata.replace("_TDATA4_", str(type2[i]))
        tdata = tdata.replace("_TDATA5_", str(total[i]))
        tdata = tdata.replace("_TDATA6_", str(hp[i]))
        tdata = tdata.replace("_TDATA7_", str(attack[i]))
        tdata = tdata.replace("_TDATA8_", str(defense[i]))
        tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
        tdata = tdata.replace("_TDATA10_", str(spdef[i]))
        tdata = tdata.replace("_TDATA11_", str(speed[i]))
        tdata = tdata.replace("_TDATA12_", str(gen[i]))
        tdata = tdata.replace("_TDATA13_", str(legend[i]))
        data += td.replace(td, tdata)
        data = data[:len(data)]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)



alls = open("all.html", "w")
print(allPage(), file = alls)
alls.close()


def typesPage():

    tab = " " * 4
    site = '''
<DOCTYPE HTML>
    <html>
        <head>
            ?HEAD?
            <title>
                ?TITLE?
            </title>
            <style>
                ?STYLE?
            </style>
        </head>
        <body>
            ?BODY?
        </body>
    </html>'''


    site = site.replace("?TITLE?", "Pokemon")
    head = ""

    h1 = "<h1>Pokemon Reviews</h1>\n"
    p = tab * 2 + "<p>I think pokemans are cool even though I haven't really played with them that much. I heard PIkachu is really popular though, so I think that's my favorite! I also heard of Kirby which is also cool!</p>\n"

    technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

    poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
    ahref = "<a href=\"LINK\">_DD_</a>\n"
    navbar = '''

        <button><a href= "home.html">Home</a></button>
        <button><a href = "all.html">All Pokeman</a></button>
        <button><a href = "top.html">Top 10</a></button>
        <div class="dropdown">
        <button><a href = "types.html">Types</a></button>
    <div class="dropdown-options">\n''' + ahref  + '''</div>
</div>
'''

    T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    data += p

    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)

types = open("types.html", "w")
print(typesPage(), file = types)
types.close()

def topPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

    tab = " " * 4
    site = '''<DOCTYPE HTML>
    <html>
        <head>
        ?HEAD?
            <title>
            ?TITLE?
            </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
    </html>'''


    site = site.replace("?TITLE?", "Pokemon")
    head = ""

    h1 = "<h1>My Top 10 Pokemon</h1>\n"
    p = tab * 2 + "<p>I chose these off of their looks, and which looked the most unique!</p>\n"
    th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
    td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

    th1 = th.replace("_TTITLE0_", "Image")
    th1 = th1.replace("_TTITLE1_", "Number")
    th1 = th1.replace("_TTITLE2_", "Name")
    th1 = th1.replace("_TTITLE3_", "Type 1")
    th1 = th1.replace("_TTITLE4_", "Type 2")
    th1 = th1.replace("_TTITLE5_", "Total")
    th1 = th1.replace("_TTITLE6_", "HP")
    th1 = th1.replace("_TTITLE7_", "Attack")
    th1 = th1.replace("_TTITLE8_", "Defense")
    th1 = th1.replace("_TTITLE9_", "Sp. Attack")
    th1 = th1.replace("_TTITLE10_", "Sp. Defense")
    th1 = th1.replace("_TTITLE11_", "Speed")
    th1 = th1.replace("_TTITLE12_", "Generation")
    th1 = th1.replace("_TTITLE13_", "Legend")

    technical = '''
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
    <!-- link the webpage's stylesheet -->
    <link rel="stylesheet" href="./style1.css" />
'''

    poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
    ahref = "<a href=\"LINK\">_DD_</a>\n"
    navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

    T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    data += p
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(1,151, 15):
        img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
        tdata = td.replace("_TDATA0_", img)
        tdata = tdata.replace("_TDATA1_", str(num[i]))
        tdata = tdata.replace("_TDATA2_", str(name[i]))
        tdata = tdata.replace("_TDATA3_", str(type1[i]))
        tdata = tdata.replace("_TDATA4_", str(type2[i]))
        tdata = tdata.replace("_TDATA5_", str(total[i]))
        tdata = tdata.replace("_TDATA6_", str(hp[i]))
        tdata = tdata.replace("_TDATA7_", str(attack[i]))
        tdata = tdata.replace("_TDATA8_", str(defense[i]))
        tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
        tdata = tdata.replace("_TDATA10_", str(spdef[i]))
        tdata = tdata.replace("_TDATA11_", str(speed[i]))
        tdata = tdata.replace("_TDATA12_", str(gen[i]))
        tdata = tdata.replace("_TDATA13_", str(legend[i]))
        data += td.replace(td, tdata)
        data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)

top = open("top.html", "w")
print(topPage(), file = top)
top.close()


def fightingPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>'''

        style = '''


'''
        site = site.replace("?STYLE?", style)
        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Fighting Pokemon</h1>\n"
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''


        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        if str(type1[i]).lower() == "fighting" or str(type2[i]).lower() == "fighting":            
            img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
            tdata = td.replace("_TDATA0_", img)
            tdata = tdata.replace("_TDATA1_", str(num[i]))
            tdata = tdata.replace("_TDATA2_", str(name[i]))
            tdata = tdata.replace("_TDATA3_", str(type1[i]))
            tdata = tdata.replace("_TDATA4_", str(type2[i]))
            tdata = tdata.replace("_TDATA5_", str(total[i]))
            tdata = tdata.replace("_TDATA6_", str(hp[i]))
            tdata = tdata.replace("_TDATA7_", str(attack[i]))
            tdata = tdata.replace("_TDATA8_", str(defense[i]))
            tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
            tdata = tdata.replace("_TDATA10_", str(spdef[i]))
            tdata = tdata.replace("_TDATA11_", str(speed[i]))
            tdata = tdata.replace("_TDATA12_", str(gen[i]))
            tdata = tdata.replace("_TDATA13_", str(legend[i]))
            data += td.replace(td, tdata)
            data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)



def flyingPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site =  '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>
'''

        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Flying Pokemon</h1>\n"
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        if str(type1[i]).lower() == "flying" or str(type2[i]).lower() == "flying":
            img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
            tdata = td.replace("_TDATA0_", img)
            tdata = tdata.replace("_TDATA1_", str(num[i]))
            tdata = tdata.replace("_TDATA2_", str(name[i]))
            tdata = tdata.replace("_TDATA3_", str(type1[i]))
            tdata = tdata.replace("_TDATA4_", str(type2[i]))
            tdata = tdata.replace("_TDATA5_", str(total[i]))
            tdata = tdata.replace("_TDATA6_", str(hp[i]))
            tdata = tdata.replace("_TDATA7_", str(attack[i]))
            tdata = tdata.replace("_TDATA8_", str(defense[i]))
            tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
            tdata = tdata.replace("_TDATA10_", str(spdef[i]))
            tdata = tdata.replace("_TDATA11_", str(speed[i]))
            tdata = tdata.replace("_TDATA12_", str(gen[i]))
            tdata = tdata.replace("_TDATA13_", str(legend[i]))
            data += td.replace(td, tdata)
            data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(flyingPage())



def poisonPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>'''


        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Poison Pokemon</h1>\n"
     
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
   
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        if str(type1[i]).lower() == "poison" or str(type2[i]).lower() == "poison":
            img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
            tdata = td.replace("_TDATA0_", img)
            tdata = tdata.replace("_TDATA1_", str(num[i]))
            tdata = tdata.replace("_TDATA2_", str(name[i]))
            tdata = tdata.replace("_TDATA3_", str(type1[i]))
            tdata = tdata.replace("_TDATA4_", str(type2[i]))
            tdata = tdata.replace("_TDATA5_", str(total[i]))
            tdata = tdata.replace("_TDATA6_", str(hp[i]))
            tdata = tdata.replace("_TDATA7_", str(attack[i]))
            tdata = tdata.replace("_TDATA8_", str(defense[i]))
            tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
            tdata = tdata.replace("_TDATA10_", str(spdef[i]))
            tdata = tdata.replace("_TDATA11_", str(speed[i]))
            tdata = tdata.replace("_TDATA12_", str(gen[i]))
            tdata = tdata.replace("_TDATA13_", str(legend[i]))
            data += td.replace(td, tdata)
            data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(poisonPage())



def groundPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>'''


        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Ground Pokemon</h1>\n"
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        if str(type1[i]).lower() == "ground" or str(type2[i]).lower() == "ground":
            img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
            tdata = td.replace("_TDATA0_", img)
            tdata = tdata.replace("_TDATA1_", str(num[i]))
            tdata = tdata.replace("_TDATA2_", str(name[i]))
            tdata = tdata.replace("_TDATA3_", str(type1[i]))
            tdata = tdata.replace("_TDATA4_", str(type2[i]))
            tdata = tdata.replace("_TDATA5_", str(total[i]))
            tdata = tdata.replace("_TDATA6_", str(hp[i]))
            tdata = tdata.replace("_TDATA7_", str(attack[i]))
            tdata = tdata.replace("_TDATA8_", str(defense[i]))
            tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
            tdata = tdata.replace("_TDATA10_", str(spdef[i]))
            tdata = tdata.replace("_TDATA11_", str(speed[i]))
            tdata = tdata.replace("_TDATA12_", str(gen[i]))
            tdata = tdata.replace("_TDATA13_", str(legend[i]))
            data += td.replace(td, tdata)
            data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(groundPage())



def rockPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>'''


        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Rock Pokemon</h1>\n"
     
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
   
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        if str(type1[i]).lower() == "rock" or str(type2[i]).lower() == "rock":
            img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
            tdata = td.replace("_TDATA0_", img)
            tdata = tdata.replace("_TDATA1_", str(num[i]))
            tdata = tdata.replace("_TDATA2_", str(name[i]))
            tdata = tdata.replace("_TDATA3_", str(type1[i]))
            tdata = tdata.replace("_TDATA4_", str(type2[i]))
            tdata = tdata.replace("_TDATA5_", str(total[i]))
            tdata = tdata.replace("_TDATA6_", str(hp[i]))
            tdata = tdata.replace("_TDATA7_", str(attack[i]))
            tdata = tdata.replace("_TDATA8_", str(defense[i]))
            tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
            tdata = tdata.replace("_TDATA10_", str(spdef[i]))
            tdata = tdata.replace("_TDATA11_", str(speed[i]))
            tdata = tdata.replace("_TDATA12_", str(gen[i]))
            tdata = tdata.replace("_TDATA13_", str(legend[i]))
            data += td.replace(td, tdata)
            data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(rockPage())



def bugPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>'''


        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Bug Pokemon</h1>\n"
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        if str(type1[i]).lower() == "bug" or str(type2[i]).lower() == "bug":
            img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
            tdata = td.replace("_TDATA0_", img)
            tdata = tdata.replace("_TDATA1_", str(num[i]))
            tdata = tdata.replace("_TDATA2_", str(name[i]))
            tdata = tdata.replace("_TDATA3_", str(type1[i]))
            tdata = tdata.replace("_TDATA4_", str(type2[i]))
            tdata = tdata.replace("_TDATA5_", str(total[i]))
            tdata = tdata.replace("_TDATA6_", str(hp[i]))
            tdata = tdata.replace("_TDATA7_", str(attack[i]))
            tdata = tdata.replace("_TDATA8_", str(defense[i]))
            tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
            tdata = tdata.replace("_TDATA10_", str(spdef[i]))
            tdata = tdata.replace("_TDATA11_", str(speed[i]))
            tdata = tdata.replace("_TDATA12_", str(gen[i]))
            tdata = tdata.replace("_TDATA13_", str(legend[i]))
            data += td.replace(td, tdata)
            data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(bugPage())



def ghostPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>'''


        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Ghost Pokemon</h1>\n"
     
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
  
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        if str(type1[i]).lower() == "ghost" or str(type2[i]).lower() == "ghost":
            img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
            tdata = td.replace("_TDATA0_", img)
            tdata = tdata.replace("_TDATA1_", str(num[i]))
            tdata = tdata.replace("_TDATA2_", str(name[i]))
            tdata = tdata.replace("_TDATA3_", str(type1[i]))
            tdata = tdata.replace("_TDATA4_", str(type2[i]))
            tdata = tdata.replace("_TDATA5_", str(total[i]))
            tdata = tdata.replace("_TDATA6_", str(hp[i]))
            tdata = tdata.replace("_TDATA7_", str(attack[i]))
            tdata = tdata.replace("_TDATA8_", str(defense[i]))
            tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
            tdata = tdata.replace("_TDATA10_", str(spdef[i]))
            tdata = tdata.replace("_TDATA11_", str(speed[i]))
            tdata = tdata.replace("_TDATA12_", str(gen[i]))
            tdata = tdata.replace("_TDATA13_", str(legend[i]))
            data += td.replace(td, tdata)
            data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(ghostPage())



def steelPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>'''


        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Steel Pokemon</h1>\n"
        
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        if str(type1[i]).lower() == "steel" or str(type2[i]).lower() == "steel":
            img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
            tdata = td.replace("_TDATA0_", img)
            tdata = tdata.replace("_TDATA1_", str(num[i]))
            tdata = tdata.replace("_TDATA2_", str(name[i]))
            tdata = tdata.replace("_TDATA3_", str(type1[i]))
            tdata = tdata.replace("_TDATA4_", str(type2[i]))
            tdata = tdata.replace("_TDATA5_", str(total[i]))
            tdata = tdata.replace("_TDATA6_", str(hp[i]))
            tdata = tdata.replace("_TDATA7_", str(attack[i]))
            tdata = tdata.replace("_TDATA8_", str(defense[i]))
            tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
            tdata = tdata.replace("_TDATA10_", str(spdef[i]))
            tdata = tdata.replace("_TDATA11_", str(speed[i]))
            tdata = tdata.replace("_TDATA12_", str(gen[i]))
            tdata = tdata.replace("_TDATA13_", str(legend[i]))
            data += td.replace(td, tdata)
            data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(steelPage())



def firePage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>'''


        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Fire Pokemon</h1>\n"
       
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1

    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        if str(type1[i]).lower() == "fire" or str(type2[i]).lower() == "fire":
            img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
            tdata = td.replace("_TDATA0_", img)
            tdata = tdata.replace("_TDATA1_", str(num[i]))
            tdata = tdata.replace("_TDATA2_", str(name[i]))
            tdata = tdata.replace("_TDATA3_", str(type1[i]))
            tdata = tdata.replace("_TDATA4_", str(type2[i]))
            tdata = tdata.replace("_TDATA5_", str(total[i]))
            tdata = tdata.replace("_TDATA6_", str(hp[i]))
            tdata = tdata.replace("_TDATA7_", str(attack[i]))
            tdata = tdata.replace("_TDATA8_", str(defense[i]))
            tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
            tdata = tdata.replace("_TDATA10_", str(spdef[i]))
            tdata = tdata.replace("_TDATA11_", str(speed[i]))
            tdata = tdata.replace("_TDATA12_", str(gen[i]))
            tdata = tdata.replace("_TDATA13_", str(legend[i]))
            data += td.replace(td, tdata)
            data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(firePage())



def grassPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>'''


        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Grass Pokemon</h1>\n"
       
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        if str(type1[i]).lower() == "grass" or str(type2[i]).lower() == "grass":
            img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
            tdata = td.replace("_TDATA0_", img)
            tdata = tdata.replace("_TDATA1_", str(num[i]))
            tdata = tdata.replace("_TDATA2_", str(name[i]))
            tdata = tdata.replace("_TDATA3_", str(type1[i]))
            tdata = tdata.replace("_TDATA4_", str(type2[i]))
            tdata = tdata.replace("_TDATA5_", str(total[i]))
            tdata = tdata.replace("_TDATA6_", str(hp[i]))
            tdata = tdata.replace("_TDATA7_", str(attack[i]))
            tdata = tdata.replace("_TDATA8_", str(defense[i]))
            tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
            tdata = tdata.replace("_TDATA10_", str(spdef[i]))
            tdata = tdata.replace("_TDATA11_", str(speed[i]))
            tdata = tdata.replace("_TDATA12_", str(gen[i]))
            tdata = tdata.replace("_TDATA13_", str(legend[i]))
            data += td.replace(td, tdata)
            data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(grassPage())



def waterPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>'''


        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Water Pokemon</h1>\n"
        
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        if str(type1[i]).lower() == "water" or str(type2[i]).lower() == "water":
            img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
            tdata = td.replace("_TDATA0_", img)
            tdata = tdata.replace("_TDATA1_", str(num[i]))
            tdata = tdata.replace("_TDATA2_", str(name[i]))
            tdata = tdata.replace("_TDATA3_", str(type1[i]))
            tdata = tdata.replace("_TDATA4_", str(type2[i]))
            tdata = tdata.replace("_TDATA5_", str(total[i]))
            tdata = tdata.replace("_TDATA6_", str(hp[i]))
            tdata = tdata.replace("_TDATA7_", str(attack[i]))
            tdata = tdata.replace("_TDATA8_", str(defense[i]))
            tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
            tdata = tdata.replace("_TDATA10_", str(spdef[i]))
            tdata = tdata.replace("_TDATA11_", str(speed[i]))
            tdata = tdata.replace("_TDATA12_", str(gen[i]))
            tdata = tdata.replace("_TDATA13_", str(legend[i]))
            data += td.replace(td, tdata)
            data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(waterPage())



def electricPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>'''


        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Electric Pokemon Reviews</h1>\n"
        
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        if str(type1[i]).lower() == "electric" or str(type2[i]).lower() == "electric":
            img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
            tdata = td.replace("_TDATA0_", img)
            tdata = tdata.replace("_TDATA1_", str(num[i]))
            tdata = tdata.replace("_TDATA2_", str(name[i]))
            tdata = tdata.replace("_TDATA3_", str(type1[i]))
            tdata = tdata.replace("_TDATA4_", str(type2[i]))
            tdata = tdata.replace("_TDATA5_", str(total[i]))
            tdata = tdata.replace("_TDATA6_", str(hp[i]))
            tdata = tdata.replace("_TDATA7_", str(attack[i]))
            tdata = tdata.replace("_TDATA8_", str(defense[i]))
            tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
            tdata = tdata.replace("_TDATA10_", str(spdef[i]))
            tdata = tdata.replace("_TDATA11_", str(speed[i]))
            tdata = tdata.replace("_TDATA12_", str(gen[i]))
            tdata = tdata.replace("_TDATA13_", str(legend[i]))
            data += td.replace(td, tdata)
            data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(electricPage())



def psychicPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>'''


        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Psychic Pokemon Reviews</h1>\n"
        
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        if str(type1[i]).lower() == "psychic" or str(type2[i]).lower() == "psychic":
            img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
            tdata = td.replace("_TDATA0_", img)
            tdata = tdata.replace("_TDATA1_", str(num[i]))
            tdata = tdata.replace("_TDATA2_", str(name[i]))
            tdata = tdata.replace("_TDATA3_", str(type1[i]))
            tdata = tdata.replace("_TDATA4_", str(type2[i]))
            tdata = tdata.replace("_TDATA5_", str(total[i]))
            tdata = tdata.replace("_TDATA6_", str(hp[i]))
            tdata = tdata.replace("_TDATA7_", str(attack[i]))
            tdata = tdata.replace("_TDATA8_", str(defense[i]))
            tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
            tdata = tdata.replace("_TDATA10_", str(spdef[i]))
            tdata = tdata.replace("_TDATA11_", str(speed[i]))
            tdata = tdata.replace("_TDATA12_", str(gen[i]))
            tdata = tdata.replace("_TDATA13_", str(legend[i]))
            data += td.replace(td, tdata)
            data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(psychicPage())



def icePage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>'''


        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Ice Pokemon Reviews</h1>\n"
        
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        if str(type1[i]).lower() == "ice" or str(type2[i]).lower() == "ice":
            img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
            tdata = td.replace("_TDATA0_", img)
            tdata = tdata.replace("_TDATA1_", str(num[i]))
            tdata = tdata.replace("_TDATA2_", str(name[i]))
            tdata = tdata.replace("_TDATA3_", str(type1[i]))
            tdata = tdata.replace("_TDATA4_", str(type2[i]))
            tdata = tdata.replace("_TDATA5_", str(total[i]))
            tdata = tdata.replace("_TDATA6_", str(hp[i]))
            tdata = tdata.replace("_TDATA7_", str(attack[i]))
            tdata = tdata.replace("_TDATA8_", str(defense[i]))
            tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
            tdata = tdata.replace("_TDATA10_", str(spdef[i]))
            tdata = tdata.replace("_TDATA11_", str(speed[i]))
            tdata = tdata.replace("_TDATA12_", str(gen[i]))
            tdata = tdata.replace("_TDATA13_", str(legend[i]))
            data += td.replace(td, tdata)
            data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(icePage())



def dragonPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>'''


        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Dragon Pokemon Reviews</h1>\n"
        
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        if str(type1[i]).lower() == "dragon" or  str(type2[i]).lower() == "dragon":
            img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
            tdata = td.replace("_TDATA0_", img)
            tdata = tdata.replace("_TDATA1_", str(num[i]))
            tdata = tdata.replace("_TDATA2_", str(name[i]))
            tdata = tdata.replace("_TDATA3_", str(type1[i]))
            tdata = tdata.replace("_TDATA4_", str(type2[i]))
            tdata = tdata.replace("_TDATA5_", str(total[i]))
            tdata = tdata.replace("_TDATA6_", str(hp[i]))
            tdata = tdata.replace("_TDATA7_", str(attack[i]))
            tdata = tdata.replace("_TDATA8_", str(defense[i]))
            tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
            tdata = tdata.replace("_TDATA10_", str(spdef[i]))
            tdata = tdata.replace("_TDATA11_", str(speed[i]))
            tdata = tdata.replace("_TDATA12_", str(gen[i]))
            tdata = tdata.replace("_TDATA13_", str(legend[i]))
            data += td.replace(td, tdata)
            data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(dragonPage())



def normalPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>'''


        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Normal Pokemon Reviews</h1>\n"
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        if str(type1[i]).lower() == "normal" or str(type2[i]).lower() == "normal":
            img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
            tdata = td.replace("_TDATA0_", img)
            tdata = tdata.replace("_TDATA1_", str(num[i]))
            tdata = tdata.replace("_TDATA2_", str(name[i]))
            tdata = tdata.replace("_TDATA3_", str(type1[i]))
            tdata = tdata.replace("_TDATA4_", str(type2[i]))
            tdata = tdata.replace("_TDATA5_", str(total[i]))
            tdata = tdata.replace("_TDATA6_", str(hp[i]))
            tdata = tdata.replace("_TDATA7_", str(attack[i]))
            tdata = tdata.replace("_TDATA8_", str(defense[i]))
            tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
            tdata = tdata.replace("_TDATA10_", str(spdef[i]))
            tdata = tdata.replace("_TDATA11_", str(speed[i]))
            tdata = tdata.replace("_TDATA12_", str(gen[i]))
            tdata = tdata.replace("_TDATA13_", str(legend[i]))
            data += td.replace(td, tdata)
            data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(normalPage())



def fairyPage():
    f = open("/home/students/2025/asaha50/Downloads/pokemon/pokemon.csv", "r")
    poke_file = f.read()
    poke_list = poke_file.split("\n")

    poke_2dlist = []
    num = []
    name = []
    type1 = []
    type2 = []
    total = []
    hp = []
    attack = []
    defense = []
    spAtk = []
    spdef = []
    speed = []
    gen = []
    legend = []

    for row in poke_list[1:]:
        row = row.split(",")
        poke_2dlist.append(row)

    for subList in poke_2dlist[:len(poke_2dlist) - 1]:
        num.append(subList[0])
        name.append(subList[1])
        type1.append(subList[2])
        type2.append(subList[3])
        total.append(subList[4])
        hp.append(subList[5])
        attack.append(subList[6])
        defense.append(subList[7])
        spAtk.append(subList[8])
        spdef.append(subList[9])
        speed.append(subList[10])
        gen.append(subList[11])
        legend.append(subList[12])

        tab = " " * 4
        site = '''
        <DOCTYPE HTML>
        <html>
        <head>
        ?HEAD?
        <title>
        ?TITLE?
        </title>
        <style>
        ?STYLE?
        </style>
        </head>
        <body>
        ?BODY?
        </body>
        </html>'''


        site = site.replace("?TITLE?", "Pokemon")
        head = ""

        h1 = "<h1>Fairy Pokemon Reviews</h1>\n"
       
        th = "<tr><th>_TTITLE0_</th><th>_TTITLE1_</th><th>_TTITLE2_</th><th>_TTITLE3_</th><th>_TTITLE4_</th><th>_TTITLE5_</th><th>_TTITLE6_</th><th>_TTITLE7_</th><th>_TTITLE8_</th><th>_TTITLE9_</th><th>_TTITLE10_</th><th>_TTITLE11_</th><th>_TTITLE12_</th><th>_TTITLE13_</th></tr>"
        td = tab + "<tr><td>_TDATA0_</td><td>_TDATA1_</td><td>_TDATA2_</td><td>_TDATA3_</td><td>_TDATA4_</td><td>_TDATA5_</td><td>_TDATA6_</td><td>_TDATA7_</td><td>_TDATA8_</td><td>_TDATA9_</td><td>_TDATA10_</td><td>_TDATA11_</td><td>_TDATA12_</td><td>_TDATA13_</td></tr>\n" + (tab * 2)

        th1 = th.replace("_TTITLE0_", "Image")
        th1 = th1.replace("_TTITLE1_", "Number")
        th1 = th1.replace("_TTITLE2_", "Name")
        th1 = th1.replace("_TTITLE3_", "Type 1")
        th1 = th1.replace("_TTITLE4_", "Type 2")
        th1 = th1.replace("_TTITLE5_", "Total")
        th1 = th1.replace("_TTITLE6_", "HP")
        th1 = th1.replace("_TTITLE7_", "Attack")
        th1 = th1.replace("_TTITLE8_", "Defense")
        th1 = th1.replace("_TTITLE9_", "Sp. Attack")
        th1 = th1.replace("_TTITLE10_", "Sp. Defense")
        th1 = th1.replace("_TTITLE11_", "Speed")
        th1 = th1.replace("_TTITLE12_", "Generation")
        th1 = th1.replace("_TTITLE13_", "Legend")

        technical = '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lora:ital@0;1&family=Montserrat:wght@300&family=Poppins:wght@200&family=Raleway:wght@300&display=swap" rel="stylesheet">
        <!-- link the webpage's stylesheet -->
        <link rel="stylesheet" href="./style1.css" />
'''

        poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
        ahref = "<a href=\"LINK\">_DD_</a>\n"
        navbar = '''

<button><a href= "home.html">Home</a></button>
<button><a href = "all.html">All Pokeman</a></button>
<button><a href = "top.html">Top 10</a></button>
<div class="dropdown">
<button><a href = "types.html">Types</a></button>
        <div class="dropdown-options">\n''' + ahref  + '''</div>

</div>
'''

        T17 = " "
    for i in range(17):
        TDD = ahref.replace("_DD_", poke_type[i])
        TDD = TDD.replace("LINK", (poke_type[i]) + ".html")
        T17 += ahref.replace(ahref, TDD)
    navbar = navbar.replace("<a href=\"LINK\">_DD_</a>", T17)

    data = ""
    data += technical
    data += navbar
    data += h1
    
    data += "<table border = 1>"
    data += th1

        #data
        #images
    for i in range(len(num) - 1):
        if str(type1[i]).lower() == "fairy" or str(type2[i]).lower() == "fairy":
            img = "<img src = \"./" + "img/front/" + str(int(i+1)) + ".png" + "\" height= \"100px\">" + "\n" + "<img src = \"./" + "img/back/" + str(int(i+1)) + ".png" + "\" height= \"100px\">"
            tdata = td.replace("_TDATA0_", img)
            tdata = tdata.replace("_TDATA1_", str(num[i]))
            tdata = tdata.replace("_TDATA2_", str(name[i]))
            tdata = tdata.replace("_TDATA3_", str(type1[i]))
            tdata = tdata.replace("_TDATA4_", str(type2[i]))
            tdata = tdata.replace("_TDATA5_", str(total[i]))
            tdata = tdata.replace("_TDATA6_", str(hp[i]))
            tdata = tdata.replace("_TDATA7_", str(attack[i]))
            tdata = tdata.replace("_TDATA8_", str(defense[i]))
            tdata = tdata.replace("_TDATA9_", str(spAtk[i]))
            tdata = tdata.replace("_TDATA10_", str(spdef[i]))
            tdata = tdata.replace("_TDATA11_", str(speed[i]))
            tdata = tdata.replace("_TDATA12_", str(gen[i]))
            tdata = tdata.replace("_TDATA13_", str(legend[i]))
            data += td.replace(td, tdata)
            data = data[:len(data)-9]
    data += "\n</table>"


    site = site.replace("?BODY?", data)
    site = site.replace("?HEAD?", head)
    return(site)
print(fairyPage())

for i in range(17):
    poke_type = ["Fighting" , "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Grass", "Water", "Electric", "Psychic", "Ice", "Dragon", "Normal",  "Fairy"]
    poke_type_func = [fightingPage(), flyingPage(), poisonPage(),groundPage(),rockPage(),bugPage(),ghostPage(),steelPage(),firePage(),grassPage(),waterPage(),electricPage(), psychicPage(), icePage(), dragonPage(), normalPage(), fairyPage()]
    poke_type[i] = open(poke_type[i] + ".html", "w")
    print(poke_type_func[i], file = poke_type[i])
    poke_type[i].close()

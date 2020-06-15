import webbrowser

while True:

    command = input('youtube(y), google(g):   ')

    if command == "y":
        com2 = input("youtube search:    ")
        webbrowser.open('https://www.youtube.com/results?search_query=' + com2)

    elif command == "g":
        com = input('google search:  ')
        webbrowser.open('http://google.com/?#q=' + com)




    
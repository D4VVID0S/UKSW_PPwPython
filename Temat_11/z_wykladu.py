import matplotlib.pyplot as plt
import numpy as np

def podstawy():
    # dane do narysowania
    x_values = [0,1,2,3,4,5]
    y_values = [0,1,4,9,16,25]

    # domyślne polecenie plot tworzy linie
    plt.plot(x_values, y_values)

    # legenda osi
    plt.title("Potęgi drugiego stopnia")
    plt.xlabel("Potęgowana liczba")
    plt.ylabel("Potęga stopnia 2")

    # Wyświetl wykres
    plt.show()

def przepis_na_wykres():
    # x axis values
    x = [1,2,3]
    # y axis valies
    y = [2,4,1]

    # plotting the points
    plt.plot(x,y)

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')

    # givig a title to the graph
    plt.title('My first graph!')

    # function to show the plot
    plt.show()

def wiele_krzywych():
    # line 1 points
    x1 = [1,2,3]
    y1 = [2,4,1]
    # plotting the line 1 points
    plt.plot(x1, y1, label='line 1')

    # line 2 points
    x2 = [1,2,3]
    y2 = [4,1,3]
    # plotting the line 2 points
    plt.plot(x2, y2, label='line 2')

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    # giving a title
    plt.title('Two lines on the same graph!')
    # show a legend on the plot
    plt.legend()

    plt.show()

def tuning():
    x = [1,2,3,4,5,6]
    y = [2,4,1,5,2,6]

    plt.plot(x, y, color='orange', linestyle='dashed', linewidth=2, marker='o', markerfacecolor='red', markersize=22)

    # setting x and y axis range
    plt.ylim(1,8)
    plt.xlim(1,8)

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('some cool customizations!')

    plt.show()

def rysowanie_rownan():
    # setting the x - coordinates
    x = np.arange(0,2*(np.pi),0.1) # numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
    # print("O to wartosci zawarte w x: ", x) # Do zobaczenia jakie wartości kryją się pod x
    # setting the y - coordinates
    y = np.sin(x)

    plt.plot(x,y)

    plt.title("Funckja SIN(x)!")

    plt.show()

def zapis_do_pliku():
    y1 = []
    y2 = []
    x = range(-100,100,10) # (start, end, step)

    for i in x: y1.append(i**2)
    for i in x: y2.append(-i**2)

    plt.plot(x,y1)
    plt.plot(x,y2)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(-2000,2000) # granice wykresu
    plt.axhline(0) # pozioma linia w zerze
    plt.axvline(0) # pionowa linia w zerze

    plt.savefig('kwadratowe.png') # zapisz obrazek do pliku

    plt.show()

def wykresy_slupkowe():
    values = [5,6,3,7,2]
    names = ['A','B','C','D','E']

    # create a bar chart
    plt.bar(names,values,color='green')
    plt.show()

def poziome_slupki():
    values = [5,6,3,7,2]
    names = ['A','B','C','D','E']

    # create a horizontal bar chart by using plt.barh (adding an h to the function name)
    plt.barh(names,values,color='red')
    plt.show()

def mieszane_kolory_slupkow():
    height = [10,24,36,40,5]
    names = ['one','two','three','four','five']

    # plotting a bar chart
    c1 = ['red','green']
    # we can also use this for color
    c2 = ['b','g']

    # the bar chart will alternate the colors of the bars
    plt.bar(names,height,width=0.8,color=c1)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('My bar chart!')
    plt.show()

def histogram():
    x = [2,1,6,4,2,4,8,9,4,2,4,10,6,4,5,7,7,3,2,7,5,3,5,9,2,1]

    '''
    plot for a histogram
    bins - ile ma być słupków
    alpha - słupki mogą być półprzezroczyste
    '''
    plt.hist(x,bins=100,color='blue',alpha=0.5)
    plt.show()

def histogram_part2():
    ages=[2,5,70,40,30,45,50,45,43,40,44,60,7,13,57,18,90,77,32,21,20,40]

    # setting the range and number of intervals
    range = (0,100)
    bins = 10

    '''
    rwidth - szerokość słupka
    histtype - {'bar', 'barstacked', 'step', 'stepfilled'}, default: 'bar'
    '''
    plt.hist(ages,bins,range,color='green',histtype='bar',rwidth=0.2)
    
    plt.xlabel('Age')
    plt.ylabel('No. of people')
    plt.title('My histogram')
    plt.show()

def wlasny_histogram():
    ages=[2,5,70,40,30,45,50,45,43,40,44,60,7,13,57,18,90,77,32,21,20,40]
    range = (0,100)
    bins = 10
    
    # pierwsza cwiartka
    # 'bar' is a traditional bar-type histogram. If multiple data are given the bars are arranged side by side.
    plt.subplot(2,2,1)
    plt.hist(ages,bins,range,color='red',histtype='bar',rwidth=0.8)
    plt.xlabel('Age')
    plt.ylabel('No. of people')
    plt.title('Bar histogram')
    
    # druga cwiartka
    # 'barstacked' is a bar-type histogram where multiple data are stacked on top of each other.
    plt.subplot(2,2,2)
    plt.hist(ages,bins,range,color='blue',histtype='barstacked',rwidth=0.8)
    plt.xlabel('Age')
    plt.ylabel('No. of people')
    plt.title('Barstacked histogram')

    # trzecia cwiartka
    # 'step' generates a lineplot that is by default unfilled.
    plt.subplot(2,2,3)
    plt.hist(ages,bins,range,color='green',histtype='step',rwidth=0.8)
    plt.xlabel('Age')
    plt.ylabel('No. of people')
    plt.title('Step histogram')

    # czwarta cwiartka
    # 'stepfilled' generates a lineplot that is by default filled.
    plt.subplot(2,2,4)
    plt.hist(ages,bins,range,color='orange',histtype='stepfilled',rwidth=0.8)
    plt.xlabel('Age')
    plt.ylabel('No. of people')
    plt.title('Stepfilled histogram')

    plt.show()

def wykresy_punktowe():
    x_values = np.random.randint(0,10000,size=100)
    y_values = np.random.randint(0,10000,size=100)

    # stwórz wykres punktowy
    # s = 30 - ustawia rozmiar 'size' punktów
    plt.scatter(x_values,y_values,s=30,color='blue')
    plt.show()

def punktowy_part2():
    x = np.arange(1,11)
    y = [2,4,5,7,6,8,9,11,12,12]

    # plotting points as a scatter plot
    plt.scatter(x,y,label='star',color='green',marker='*',s=30)

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('My scatter plot')
    plt.legend()
    plt.show()

def wykres_kolowy():
    # defining labels
    activities = ['eat','sleep','work','play']

    # portion covered by each layer
    slices = [3,7,8,6]

    # color for each label
    colors = ['r','y','g','b']

    '''
    plotting the pie chart
    startangle - The angle by which the start of the pie is rotated, counterclockwise from the x-axis.
    shadow - Draw a shadow beneath the pie.
    explode - If not None, is a len(x) array which specifies the fraction of the radius with which to offset each wedge. (rozdiela kawałki chartu)
    radius - The radius of the pie.
    autopct - places a lable inside the wedge. 1.1f% places the % the wedge takes in the pie formatting to 1 decimal place
    '''
    plt.pie(slices,labels=activities,colors=colors,startangle=30,shadow=True,explode=(0.1,0.1,0.1,0.1),radius=1.2,autopct='%1.2f%%')

    plt.legend()
    plt.show()


def main():
    # podstawy()
    # przepis_na_wykres()
    # wiele_krzywych()
    # tuning()
    # rysowanie_rownan()
    # zapis_do_pliku()
    # wykresy_slupkowe()
    # poziome_slupki()
    # mieszane_kolory_slupkow()
    # histogram()
    # histogram_part2()
    # wlasny_histogram()
    # wykresy_punktowe()
    # punktowy_part2()
    wykres_kolowy()


if __name__ == "__main__":
    main()
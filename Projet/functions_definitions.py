def printgraph(x,y,xname,yname,unit1, unit2):
    plt.figure(figsize=(7, 5))
    plt.plot(x,y,'-o', mfc="w")
    
    # Show a straight line
    # plt.axline((x[0], y[0]), (x[1], y[1]))

    plt.title(f'{yname} as a function of {xname}')
    plt.xlabel(f"{xname} [{unit1}]")
    plt.ylabel(f"{yname} [{unit2}]")

    plt.text(max(x)*0.5, max(y)*0.9, f"$x_{{max}}={max(x):.6e}$\n$y_{{max}} = {max(y):.6e}$")
    
    plt.show()

    return None


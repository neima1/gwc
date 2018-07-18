import filters

def main():

    filename = input("Enter file name:\n")
    im = filters.load_img(filename)
    filters.show_img(im,filename)
    #filters.obamicon(im, filename)

main()

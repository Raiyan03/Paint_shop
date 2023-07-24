def computeSquareArea(length):
    a = length**2
    return a

def computeRectangleArea(length, width):
    b = length*width
    return b

def computeWindowsDoorsArea():
    c = 0
    num_windows_door = int(input("How many windows and doors does the room contain\n"))
    for i in range(num_windows_door):
        print("Enter length for wall", i+1, "in feet:")
        length = float(input())
        print("Enter width for wall", i+1, "in feet:")
        width = float(input())
        c += computeRectangleArea(length, width)
    return c

def computeSquareWallsArea():
    d = float(input("Please enter the side length of the wall:\n"))        #Length of one side
    area_windows_door = computeWindowsDoorsArea()
    area_square_wall = (4*computeSquareArea(d)) - area_windows_door
    return area_square_wall

def computeRectangleWallsArea():
    e = float(input("Please enter the length of the room in feet:\n"))     #Length
    f = float(input("Please enter the width of the room in feet:\n"))      #Width
    g = float(input("Please enter the height of the room in feet:\n"))     #Height
    area_rectangel_wall = (2*(computeRectangleArea(f,g) + computeRectangleArea(e,g)) - computeWindowsDoorsArea())
    return area_rectangel_wall

def customWallsArea():
    area_wall = 0
    area_ = 0
    num_walls = int(input("How many walls are there in the room:\n"))
    for j in range(num_walls):
         print("Enter the height of wall", j+1, "in feet:")
         h = float(input())   #height
         print("Enter the length of wall", j+1, "in feet:")
         l = float(input())   #length
         area_ += computeRectangleArea(l,h)
    area_wall = area_ - computeWindowsDoorsArea()
    return area_wall

def computeGallons(x):
    paint = x / 350
    return paint

def PaintPrice(y):
    paint = computeGallons(y)
    price = paint * 42
    return price

def computRoomArea(no_room):

    area_list = []
    req_paint_list = []
    price_list = []
    for k in range(no_room):
        print("For Room: ", k+1, "\nSelect the shape of the room:\n1 - Rectangular\n2 - Square\n3 - Custom (More or less than 4 walls, all "
          "square or rectangles)")
        ch = int(input())
        match ch:
            case 1:
                area = computeRectangleWallsArea()
                area_list.append(area)
                req_paint = computeGallons(area)
                req_paint_list.append(req_paint)
                price = PaintPrice(area)
                price_list.append(price)
            case 2:
                area = computeSquareWallsArea()
                area_list.append(area)
                req_paint = computeGallons(area)
                req_paint_list.append(req_paint)
                price = PaintPrice(area)
                price_list.append(price)
            case 3:
                area = customWallsArea()
                area_list.append(area)
                req_paint = computeGallons(area)
                req_paint_list.append(req_paint)
                price = PaintPrice(area)
                price_list.append(price)
            case _:
                print("You've entered an invalid choice.")
            
        print("For room: ",k+1,"The area to be painted", area_list[k], "square ft will require", req_paint_list[k], "gallons to paint. This will cost the customer $", price_list[k])
        print("-"*80)
    total_area = sum(area_list)
    total_paint = sum(req_paint_list)
    total_price = sum(price_list)
    print()
    print("\n\nArea to be painted is", total_area ,"square ft and will require", total_paint, "gallons to paint. This will cost the customer $",total_price)





print("Welcome to Shiny Paint Company for indoor painting\n")

no_room = int(input("How many rooms do you want to paint\n"))
print("\nThank you!\n")
computRoomArea(no_room)
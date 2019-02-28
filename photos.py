def read(file_name):
    """reading input files"""
    
    f = open(file_name)

    f1 = f.readlines()

    pics = {}

    number_of_photos = f1.pop(0)

    counter = 0

    for x in f1:
        pic = {
            "orientation": x[0],
            "number_of_tags": int(x[2]),
            "tags": set(x[4:-1].split(" "))
        }
        pics[counter] = pic
        counter += 1

    return pics


def create_slides():
    """function to create slideshow of the photos"""
    pics =  read("filesin/e_shiny_selfies.txt")
    slides = []
    vertical = []
    for pic, values in pics.items():
        if values['orientation'] == 'H':
            slides.append(pic)
        else:
            vertical.append(pic)

    # sorted_list = []
    # 
    # for x in slides:
    #     elements_x = len(pics[x]['tags'])
    #     elements_x1 = len(pics[x + 1]['tags'])
    #     intersection = len(pics[x]['tags'].intersection(pics[x + 1]['tags']))
    #
    #     min = min(elements_x-intersection, elements_x1-intersection, intersection)

    if len(vertical) % 2 == 0:
        vertical_pairs = [vertical[i:i+2] for i in range(0, len(vertical), 2)]
    else:
        vertical.pop()
        vertical_pairs = [vertical[i:i+2] for i in range(0, len(vertical), 2)]

    for v in vertical_pairs:
        slides.append(v)

    return slides

def commom_elements():
    slides = create_slides()

    f = open('file_out/e_shiny_selfies.txt', 'w')

    f.write(str(len(slides)) + '\n')

    for slide in slides:
        if type(slide) == int:
            f.write(str(slide) + '\n')
        else:
            f.write(str(slide[0]) + " " + str(slide[1]) + '\n')

    return "We are done"

if __name__ == '__main__':
    # create_slides()
    commom_elements()

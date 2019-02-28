def read(file_name):
    f = open(file_name)

    f1 = f.readlines()

    pics = {}

    number_of_photos = f1.pop(0)

    counter = 0

    for x in f1:
        pic = {
            "orientation": x[0],
            "number_of_tags": int(x[2]),
            "tags": list(x[4:-1].split(" "))
        }
        pics[counter] = pic
        counter += 1

    return pics


def commom_elements():
    tags = read_file("filename")
    for item in tags:
        item = set(item)


if __name__ == '__main__':
    read("filesin/a_example.txt")

def read_file(filename):
    with open(filename, 'r') as f:
        photos = f.readline()
        photos_dict = {}

        for i in range(int(photos)):
            line = f.readline()
            orientation = line.split()[0]
            num_tags = int(line.split()[1])
            tags = []
            for n in range(num_tags):
                tags.append(line.split()[n+2])
            photos_dict[i] = {"orientation": orientation,
                                "tags": tags}
        print(photos_dict)
        return photos_dict

def commom_elements():
    tags = read_file("filename")
    for item in tags:
        item = set(item)


if __name__=='__main__':
    read_file("filesin/a_example.txt")
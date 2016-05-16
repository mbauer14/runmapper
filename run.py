from PIL import Image, ImageDraw
import argparse


# Picture dimensions
X_DIM = 400
Y_DIM = 400

def graph(output):
    """
    Graphs the data to the file
    """

    # Test for now
    img = Image.new("RGB", (400,400), "black")
    pixelMap = img.load()

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pixelMap[x,y] = (
                    int((float(x)/img.size[0]) * 255),
                    int((float(y)/img.size[1]) * 255),
                    100
            )

    # write to stdout
    img.save(output, "PNG")


def initParser():
    """
    Initializes the argument parser to take any options.
    """
    parser = argparse.ArgumentParser(
            description='Create a visualization of gpx data.')
    parser.add_argument('--data', type=str,
            help='The location of the data which contains activities.csv')
    parser.add_argument('--output', type=str,
            help='The name of the output file.',
            default='output.png')
    return parser


def main():
    parser = initParser()
    args = parser.parse_args()

    # Read the data and process into correct format

    # Graph the data
    graph(args.output)


if __name__ == "__main__":
    main()

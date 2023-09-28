import numpy
import matplotlib.pyplot as plt


# open the CSV file and read its contents into a list
data_file = open("mnist_dataset/mnist_test.csv", 'r')
data_list = data_file.readlines()
data_file.close()

print(len(data_list))

for n in range(len(data_list)):
    print(data_list[n])
    all_values = data_list[n].split(',')
    image_array = numpy.asfarray(all_values[1:]).reshape((28, 28))
    plt.imshow(image_array, cmap='Greys', interpolation='None')
    plt.show()



# Nodegraph Draw Tutorial

This is a simple Python application that allows the user to input graph data and visualize it using NetworkX and Matplotlib.

## Installation

To use this application, you will need to have Python 3.x installed on your computer. You can download Python from the official website at https://www.python.org/downloads/.

You will also need to install the following libraries:

- tkinter
- networkx
- matplotlib

To install these libraries, you can use the following command:
```cmd
pip install tkinter networkx matplotlib
```

## Usage

To run the application, simply run the main.py file using Python:
```
python main.py
```
Or use /dist/Draw_GraphImage.exe

This will open a window where you can enter the graph data.

## Example

1. Write Graph data > each line mean (start_node, end_node, distance)
```
5 7 9
3 7 4
3 6 6
2 5 8
5 1 9
1 3 6
6 5 1
2 7 4
2 3 5
6 4 2
7 1 5
5 4 4
4 1 3
5 3 9
7 6 4
2 1 3
4 3 9
6 2 7
4 2 8
6 1 10
```
<img src="https://user-images.githubusercontent.com/126951066/235958963-01cfbf08-5cc3-40e2-92f4-3be790dcb01b.PNG" width="200" height="400">


2. Click Submit
<img src="https://user-images.githubusercontent.com/126951066/235959181-7078d034-2e49-48a4-8391-82693abcecfc.PNG" width="200" height="150">

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This project was inspired by the NetworkX tutorial at https://networkx.github.io/documentation/stable/tutorial.html.

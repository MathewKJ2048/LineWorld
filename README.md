# LineWorld

An open source program to render meshes in 3D, written using pygame.

![torus](https://github.com/MathewKJ2048/LineWorld/blob/main/screenshots/torus.png)

## Controls:

`w` - move forward along the x-axis  
`x` - move backward along the x-axis  
`a` - move forward along the y-axis  
`d` - move backward along the y-axis  
`z` - move forward along the z-axis  
`e` - move backward along the z-axis  

`t` - move ward in the current direction  
`b` - move ward in the current direction  

`j` - increase the polar angle (theta)  
`l` - decrease the polar angle (theta)  
`i` - increase the azimuthal angle (phi)  
`k` - decrease the azimuthal angle (phi)  


## Installation:

1) Ensure that python version 3 is installed.
2) Ensure that [pygame](https://www.pygame.org/news) is installed.
3) Download all the .py files in this repository.
4) Run `main.py`

## Creating meshes:

Different meshes can be created using the API provided in `write.py`. An example of a toroidal mesh
is given in `scratch.py`.

A mesh is a list of structures, where a structure is one of the three following objects:
- *Line*, defined by a list of two points. A line can be generated using the `add_line(point1, point2)` function in `write.py`.
- *Curve*, defined by a list of two or more points. A curve can be generated using the `add_curve(points)` function in `write.py`, where `points` is a list of points.
- *Surface*, defined by a list of two or more lists of two or more points. A surface can be generated using the `add_surface(points)` function in `write.py`, where `points` is a list of lists of points.

Once all the structures have been defined, the `write()` function can be called to write the mesh into `mesh.json`, from where the mesh is loaded everytime `main.py` is run.

---

### License: GPLv3

### Author: [Mathew K J](https://github.com/MathewKJ2048)

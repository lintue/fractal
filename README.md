![Julia](media/julia-1.png)

# APOTHEOSIS: A Simple Program for Creating Fractals

### CONTEXT

TO DO. To put simply, my intention is to develop a simple program for creating fractals -- an intuitive tool with which to learn about fractal geometry and emergent complexity.

### IMPLEMENTATION

Currently building basic functionality.

TO DO: add more sets; GIF output; image post-processing tools; browser implementation.

### INSTALLATION

Clone repository:

```
git clone https://github.com/pixel-tree/apotheosis.git
```

Create virtualenv:

e.g.

```
cd apotheosis
virtualenv -p python3.6 .
source ./bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

### USE

Run program:

```
python fractal.py --pattern i --dimensions X Y --scale j --save True/False
```

Arguments (defaults in main script):

--pattern, -p

*String expected. Name of set, e.g., Julia.*

--dimensions, -d

*Two integers. Width height, e.g., 1200 900.*

--scale, -s

*Integer expected. Try 1-10.*

--save, -w

*Boolean. True/False.*

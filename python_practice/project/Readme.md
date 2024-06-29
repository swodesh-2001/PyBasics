# Complex number project

For the python basic practice task, I tried to create a simple complex number project. Just to utilize the gist ideas of all the concepts that I have mentioned in the documentation.

I have provided the required dependency for this simple project. 

## Installing Dependency

```bash
$ pip install -r requirements.txt 
```

> Note there is no additional , extra modules required in fact , the requirement.txt is given to just showcase the use of passing the dependency file to others.


## Sample Commands to run the file

### To see the overall gist of project

```bash
python main.py --help
```


### Reading Operation
```bash
python main.py read --filename complex.txt
```

### Writing Operation
```bash
python main.py write --filename complex.txt --rvalue 0.25 --ivalue -0.25
```

### Arithmetic Operation Between Two Numbers
```bash
python main.py operation --op multiply --real1 25 --imag1 0.25 --real2 0.35 --imag2 0.31
```
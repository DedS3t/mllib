
  

## A simple ML library meant built for learning purposes

  

- [x] MSE

  

- [x] Build Linear Regression

  

- [ ] Add Multi-Variate Support (in progress: works sometimes)

  

- [ ] More...

  

  

### How to use

* Clone the repo

```bash

git clone https://github.com/DedS3t/mllib

```

* Second cd into directory

```bash

cd mllib

```

* Now run to get your directory ready

```

python setup.py bdist_wheel

```

* Now use pip to install

```

pip install .

```

#### Congrats now you are able to use the lib anywhere

  

### Docs

* Linear regression
	- ```.fit``` train model
	- ```.betas``` the coefficients 
```
from mllib.models.LinearRegression import LinearRegression
reg = LinearRegression(cost="mse")
reg.fit(X, y)
```

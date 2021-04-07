### Basic Use Instructions

---
`from RecFeatureSelect import feature_selector`<br>
`import pandas as pd`<br>
<br>
`covariance, feature_importance, raw_data = pd.read_csv(...) #csv data` <br>
`threshold = 0.8` <br>
`feature_selector(covariance, feature_importance, threshold, raw_data)` 

### Import Instructions

---

To import the package to the base conda environment in the shell (for example, to use in Jupyter notebooks):

`/opt/anaconda3/bin/pip install RecFeatureSelect`

You may need to change the location of the base conda env (for example, type `which python` in the base env). 

Once in the Jupyter notebook, import the main class as follows:

`from RecFeatureSelect import feature_selector`

You can type `?feature_selector` for info. 



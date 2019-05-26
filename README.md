# workshop
workshop material (mostly notebooks)

## contents

### introduction to Jupyter
[orcs-basics notebook](orcs-basics.ipynb)

**goal**: extract and fit a spectrum from a SITELLE cube of data

- import orcs library
- load your cube
- get the deep frame
- select the region you want to extract with ds9 (in XY coords and RADEC)
- extract the spectrum
- fit the spectrum


### intermediate examples
[orcs-intermediate notebook](orcs-intermediate.ipynb)

**goal**: make a fit with dependant parameters (aka *covarying* parameters)

- understanding outputs
- understanding input parameters
  - covarying radial velocity / expansion velocity
  - constrain line ratios
- try different line models

# PYTHON 2/3 SPHERICAL TRIGONOMETRY FUNCTIONS PACKAGE
based on original [spherical trigonometry scripts pack](http://gis-lab.info/qa/sphere-geodesic-direct-problem.html)

## USAGE
### Import package to your script:
```python
import python_spheric as s
```
### Set units
```python
s.set_units('nm') #or 'km'(by default). Otherwise no changes been taken
```
### Direct issue solution
is the "direct" geodesic issue, solve the coordinates of second point by given coordinates of first point, distance and azimuth
```python
s.direct(55,61,200,270) #latitude, longitude, distance, azimuth 
```
will produce tuple of (latitude, longitude, reverse azimuth)
> (54.95970446208453, 57.8662593013991, 87.43341127393373)

### Inverse issue solution
Is the "inverse" geodesic issue, solve the distance, azimuth and reverse azimuth between two points with assigned coordinates
```python
s.inverse(55,61,54.9597,57.866) #latitude1, longitude1, latitude2, longitude2
```
will produce tuple of azimuth, reverse azimuth, distance
> (270.0000703898066, 87.43326932644362, 200.01656014835072)

### Conversation from decimal to IVAC2 (Icarus Versatile ATC Client 2)
```python
s.to_ivac(54.9597,'lat') #coords, type(lat or lon)
```
will produce IVAC2 format coordinate
> 'N54573492'

and for "longitudes"
```python
s.to_ivac(57.866,'lon')
```
> 'E057515760'

### Conversation from IVAC2 (Icarus Versatile ATC Client 2) to decimal

```python
s.from_ivac('E057515760')
```
produce the decimal representation of given coordinate
> 57.866

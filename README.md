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

### Angular issue
solves angular issue: return coordinates of third point of spherical triangle by given coordinates of two points and azimuths to third point from each of two points
```python
s.angular(55,61,55,50,290,80) #latitude1, longitude1, latitude2, longitude2, azimuth_from_1_to_3, azimuth_from_2_to_3
```
> (55.543913134236334, 58.20411810045331)

### Linear issue
solves linear issue: return coordinates of third point of spherical triangle by given coordinates of two points and distances to third point from each of two points
```python
s.linear(55,61,55,60,30,40,1) #latitude1, longitude1, latitude2, longitude2, distance_from_1_to_2, distance_from_2_to_3, 1: right of 1-2 line(CW), 0: left of 1-2 line (CCW)
```
>(55.12911870348598, 60.586321710092335)


### Distance calculation
return distance between two points (as a part of inverse issue)
```python
s.distance(55,61,54.9597,57.866) #latitude1, latitude2, longitude1, longitude2
```
> 200.01656014835072

### Azimuth calculation
return initial azimuth from first point to second point (as a part of inverse issue)
```python
s.azimuth(55,61,54.9597,57.866)
```
> 270.0000703898066

### Bearing calculation
returns bearing (also known as reverse azimuth) from second to first point (as a part of inverse issue)
```python
s.bearing(55,61,54.9597,57.866)
```
> 87.43326932644362

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


# Primality Test Example

## Docker build
```
docker build -t ainize/primality-test .
```
## Docker run
```
docker run -p 80:80 -d ainize/primality-test
```

## How to use
The primality test application is running on localhost
```
localhost/?number=${ANY_POSITIVE_INTEGER}
```
Mersenne prime number 170141183460469231731687303715884105727 is used in this example.
The below result will be shown on your browser.
```
Number 170141183460469231731687303715884105727 is prime.
```

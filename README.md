[![Run on Ainize](https://ainize.ai/static/images/run_on_ainize_button.png)](https://ainize-cloud-run.web.app/redirect?git_repo=github.com/ainize-team/ainize-run-primality-test-example)

# Primality Test Example
A simple online prime number tester based on [Miller–Rabin primaliity test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) algorithm.

## Docker build
```
docker build -t ${YOUR_DOCKER_HUB_ID}/primality-test .
```
## Docker run
```
docker run -p 80:80 -d ${YOUR_DOCKER_HUB_ID}/primality-test
```
Now the server is available at http://localhost. To learn how to query the server, see the next section.

Note that the docker image can be deployed using any docker-based deploy platform (e.g. [ainize.ai](https://ainize.ai)).

## How to query
Now the primality test application is running on http://localhost/?number=${ANY_POSITIVE_INTEGER}.
If Mersenne prime number 170141183460469231731687303715884105727 is used, the result will be shown on your browser as below.
```
Number 170141183460469231731687303715884105727 is prime.
```

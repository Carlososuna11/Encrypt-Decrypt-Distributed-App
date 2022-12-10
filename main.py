import ray
from client.client import main

if __name__ == '__main__':
    ray.init(address='auto')
    main()

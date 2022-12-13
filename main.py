import ray
from client.main import main

if __name__ == '__main__':
    ray.init(address='auto')
    main()

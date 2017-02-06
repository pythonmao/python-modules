import test_docker

client = test_docker.DockerDriver()
print 'container list'
print client.list()

from dotmap import DotMap

server = DotMap({
    "ip": "192.168.0.18",
    "port": 8000
})

nacos = DotMap({
    "ip": "192.168.0.14",
    "port": 8848,
    "serviceName": "exApi-service",
})

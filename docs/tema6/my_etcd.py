from etcd3 import Client

etcd = Client()

etcd.get('foo')
etcd.put('bar', 'doot')
etcd.delete('bar')

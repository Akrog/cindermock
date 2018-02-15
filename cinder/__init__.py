import modulefaker

modulefaker.fake_module('cinder')
del globals()['modulefaker']

import os

from qubell.api.testing import *

@environment({
    "default": {}
})
class OracleTestCase(BaseComponentTestCase):
    name = "ATG"
    meta = os.path.realpath(os.path.join(os.path.dirname(__file__), '../meta.yml')) 
    destroy_interval = int(os.environ.get('DESTROY_INTERVAL', 1000*60*60*2))
    apps = [{
        "name": name,
        "settings": {"destroyInterval": destroy_interval},
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../component-oracle-atg.yml'))
    }]
    @classmethod
    def timeout(cls):
        return 60

    @instance(byApplication=name)
    def test_database_port(self, instance):
        import requests
        store = instance.returnValues['atg.url']
        r = requests.get(store)
        assert r.status_code == 200

from _config import config_dict
from read import EmailFetcher


class TestEmailFetcher:

    def test_connect(self):
        connection = EmailFetcher(config_dict).connect()
        assert connection.state == 'AUTH'
        assert connection.host == config_dict['HOSTNAME']



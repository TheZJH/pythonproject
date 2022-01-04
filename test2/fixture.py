import pytest


@pytest.fixture()
def fixtureFunc():
    return 'fixtureFunc'


def test_fixture(fixtureFunc):
    print('我调用了'.format(fixtureFunc))


if __name__ == '__main__':
    pytest.main(['-v', 'test_fixture.py'])

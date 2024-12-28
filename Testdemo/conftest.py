import pytest

@pytest.fixture(scope="class")
def setup():
    print("i will be executing First")
    yield
    print("i will execute Last")

@pytest.fixture()
def dataload():
    print('user profile data is being created')
    return ["Revanchist", "Hai" , "yaar"]

@pytest.fixture(params=[("chrome","Ganesh"),("FireFox","Revathi","Chaterbox"),"IE"])
def crossBrowser(request):
    return  request.param


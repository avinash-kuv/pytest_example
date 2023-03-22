import pytest
import time

class TestClass(object):
    
    test = None

    @pytest.mark.dependency()
    def test_a(self, setup):
        TestClass.test = setup.execute_script("var network = performance.getEntries() || {}; return network;")

        print(setup.title)
        setup.quit()
        
        # assert False

    def test_b(self):
        print("test b")

    @pytest.mark.dependency(depends=["TestClass::test_a"])
    def test_c(self):
        for item in TestClass.test:
            pytest.shared = item['name']

    @pytest.mark.dependency(depends=["TestClass::test_b"])
    def test_d(self):
        print("test d")

    @pytest.mark.dependency(depends=["TestClass::test_b", "TestClass::test_c"])
    def test_e(self):
        print("test e")

    def test_f(self):
        print("test f")


# class TestClassNamed(object):

#     @pytest.mark.dependency(name="a")
#     @pytest.mark.xfail(reason="deliberate fail")
#     def test_a(self):
#         assert False

#     @pytest.mark.dependency(name="b")
#     def test_b(self):
#         pass

#     @pytest.mark.dependency(name="c", depends=["a"])
#     def test_c(self):
#         pass

#     @pytest.mark.dependency(name="d", depends=["b"])
#     def test_d(self):
#         pass

#     @pytest.mark.dependency(name="e", depends=["b", "c"])
#     def test_e(self):
#         pass
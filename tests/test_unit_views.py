try:
    from run import app
    import unittest

except Exception as e:
    print ("Some Modules are Missing {}".format(e))

class FlaskTestCase(unittest.TestCase):

    #Check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    #Check for  under construction pages
    def test_error(self):
        tester = app.test_client(self)
        response = tester.get("/login")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    #Check for my name
    def test_about(self):
        tester = app.test_client(self)
        response = tester.get("/about")
        self.assertTrue(b'Biraj' in response.data)


if __name__ == "__main__":
    unittest.main()
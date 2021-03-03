import os
import tempfile

# [Note] In testing move this file to the same directory where "buggy.py" is.
try:
    from buggy import app
    import unittest

except Exception as e:
    print("Some modules are Missing {} ".format(e))


class FlaskTest(unittest.TestCase):

# [----- Index.html -----]
    # Check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check if content return is text/html
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    # Check for Data returned
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/")

        # <h3> prediction header specific to index.html
        self.assertTrue(b'<h3>Prediction Results:</h3>' in response.data)

# [----- About.html -----]

    # Check for response 200
    def test_about(self):
        tester = app.test_client(self)
        response = tester.get("/About.html")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check if content return is text/html
    def test_about_content(self):
        tester = app.test_client(self)
        response = tester.get("/About.html")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    # Check for Data returned
    def test_about_data(self):
        tester = app.test_client(self)
        response = tester.get("/About.html")

        # <h1> header specific to About.html
        self.assertTrue(b'<h1 class="pageTitle">About</h1>' in response.data)

# [----- Manual.html -----]

    # Check for response 200
    def test_manual(self):
        tester = app.test_client(self)
        response = tester.get("/Manual.html")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check if content return is text/html
    def test_manual_content(self):
        tester = app.test_client(self)
        response = tester.get("/Manual.html")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    # Check for Data returned
    def test_manual_data(self):
        tester = app.test_client(self)
        response = tester.get("/Manual.html")

        # <h1> header specific to Manual.html
        self.assertTrue(b'<h1 class="pageTitle">Manual</h1>' in response.data)

if __name__ == "__main__":
    unittest.main()
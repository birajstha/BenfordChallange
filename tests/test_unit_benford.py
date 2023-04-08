try:
    from run import app
    import unittest
    from birajwebapp.benfordapp.calc_benford import validate_benford, benfords_law, calculate_benfords_law_distribution

except Exception as e:
    print ("Some Modules are Missing {}".format(e))

class BenfordTestCase(unittest.TestCase):

    def test_validate_benford(self):
        test_data = benfords_law()
        result = validate_benford(test_data)
        self.assertEqual(result, True)

    def test_calculate_benfords_law_distribution(self):
        test_data = [123, 32, 300000, 45454545, 999]
        expected, observed = calculate_benfords_law_distribution(test_data)
        self.assertIsNotNone(observed)

if __name__ == "__main__":
    unittest.main()
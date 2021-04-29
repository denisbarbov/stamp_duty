import unittest

from main import calculateStampDutyLowerThreshold, calculateStampDuty

class Test(unittest.TestCase):
    def test_middle_threshold_accurate(self):
        res = calculateStampDutyLowerThreshold(600000)
        self.assertEqual(res, 5000)
        
    def test_middle_threshold_accurate1(self):
        res = calculateStampDutyLowerThreshold(666666)
        self.assertEqual(res, 8333.300000000001)
        
    def test_middle_thres_not(self):
        res = calculateStampDutyLowerThreshold(700000)
        self.assertNotEqual(res, 23255)
        
    def test_middle_threshold_err(self):
        res = calculateStampDutyLowerThreshold(500000)
        self.assertRaises(ValueError)

    def test_middle_threshold_errs(self):
        res = calculateStampDutyLowerThreshold(0)
        self.assertRaises(ValueError)
        
    def test_final_number_lower_range(self):
        res = calculateStampDuty(200000)
        self.assertEqual(res, 'You will pay no stamp duty.')
    
    def test_final_number_middle_range(self):
        res = calculateStampDuty(750000)
        self.assertEqual(res, 'You will pay £12500.0 in stamp duty.')
    
    def test_final_number_upper_range(self):
        res = calculateStampDuty(1600000)
        self.assertEqual(res, 'You will pay £90750.0 in stamp duty.')
        
    def test_final_number_err(self):
        res = calculateStampDuty(0)
        self.assertRaises(ValueError)
        
    def test_final_number_err_str(self):
        res = calculateStampDuty('house')
        self.assertRaises(TypeError)

if __name__=='__main__':
    unittest.main()

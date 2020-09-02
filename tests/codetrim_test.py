import unittest

import codetrim.codetrim as ct 


class CodeTrimTest(unittest.TestCase):
  
    def test_filter_codes(self):
        out = ct.filter_codes(["""/** aaa 
 88
 */"""])
        print("out ", out)
        self.assertEqual("",out)



 
if __name__=='__main__':
    unittest.main()

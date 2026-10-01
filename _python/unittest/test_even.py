import unittest

def isEven(n):
  if n % 2 == 0:
    return True
  else:
    return False

class IsEvenTests(unittest.TestCase):
  def testTwo(self):
    self.assertEqual(isEven(2), True)
    return self
  def testThree(self):
    self.assertFalse(isEven(3))
    return self
  def setUp(self):
    print(f'running setUp')
    return self
  def tearDown(self):
    print("running tearDown tasks")
    
if __name__ == '__main__':
  unittest.main()
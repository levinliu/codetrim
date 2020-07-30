import unittest

import codetrim.group_renamer as gr



class GroupRenamerTest(unittest.TestCase):
  
  def test_group_rename(self):
    p = '/tmp/org.levin.sample/src/main/scala/org/levin/sample/Hello.scala'
    fg = 'org.levin.sample'
    tg = 'org.tech0730.code'  
    new_path = gr.regroup_path(p, fg, tg)
    exp = '/tmp/org.levin.sample/src/main/scala/org/tech0730/code/Hello.scala'
    print("act ", new_path)
    self.assertEqual(exp,new_path)



 
if __name__=='__main__':
    unittest.main()

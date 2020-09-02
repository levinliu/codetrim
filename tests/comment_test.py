import unittest

import codetrim.comment as cm 


class CommentTest(unittest.TestCase):
  
    def test_comment_start(self):
        is_c = cm.comment_start("""/** aaa 
 88
 */""")
        exp = True
        print("act ", is_c)
        self.assertEqual(exp,is_c)
        self.assertEqual(False,cm.comment_start("//"))
        self.assertEqual(False, cm.comment_endwith_start(" aa // test"))
        self.assertEqual(True, cm.comment_endwith_start(" aa /*x* aa"))
        self.assertEqual(False, cm.comment_endwith_start(" a / b"))

    def test_has_line_comment(self):
        self.assertEqual(True, cm.has_line_comment(" aa // comment"))

    def test_comment_end(self):
        self.assertEqual(True,cm.comment_end("aaa */"))
        self.assertEqual(False,cm.comment_end(" aaa *  /"))
        self.assertEqual(True, cm.comment_startwith_end(" b  */ aaa"))
        self.assertEqual(True, cm.comment_startwith_end("   */  a"))
        self.assertEqual(False, cm.comment_startwith_end("  aa // bb "))

    def test_comment_line(self):
        self.assertEqual(True, cm.comment_line("// hello"))

    def test_has_inner_comment(self):
        self.assertEqual(True, cm.has_inner_comment("val a = {/* test*/ 0}"))

    def test_filter_codes(self):
        lines = [ "val a=0", "/** start", "hello"," test */", "val b=0"]
        out = cm.filter_codes(lines)
        exp = ["val a=0", "val b=0"]
        print("act=", out)
        self.assertEqual(exp, out)
        lines = [ "a=0;", "  /** comment *", " * test", " test *", "i */a=0"]
        out = cm.filter_codes(lines)
        print("act=", out)
        exp = ["a=0;", "a=0\n"]
        self.assertEqual(exp, out)
        lines = [ "a=0;", "   /* test comment */   ", "b=1"]
        out = cm.filter_codes(lines)
        exp = ["a=0;", "b=1"]
        self.assertEqual(exp, out)
        lines = ["val a = if(b>0){ /*b>0 */ 100 }"]
        out = cm.filter_codes(lines)        
        exp = ["val a = if(b>0){  100 }"]
        self.assertEqual(exp, out)

 
if __name__=='__main__':
    unittest.main()
